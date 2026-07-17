import sys
import os
from datetime import datetime
from typing import ClassVar, Iterator

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.llms import CustomLLM, CompletionResponse, LLMMetadata
from llama_index.core.llms.callbacks import llm_completion_callback

from src.claude_client import ClaudeClient

load_dotenv()

DATA_FOLDER = "data"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OUTPUT_DIR = "outputs/supply_chain_briefs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading documents for Supply Chain Agent...")
documents = SimpleDirectoryReader(DATA_FOLDER).load_data()
print(f"✅ Loaded {len(documents)} documents.")

Settings.embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)

class ClaudeLLMWrapper(CustomLLM):
    context_window: ClassVar[int] = 200000
    num_output: ClassVar[int] = 4000
    model_name: ClassVar[str] = "claude-sonnet-4-5-20250929"

    def __init__(self):
        super().__init__()
        self._client = ClaudeClient(model=self.model_name)

    @property
    def metadata(self) -> LLMMetadata:
        return LLMMetadata(
            context_window=self.context_window,
            num_output=self.num_output,
            model_name=self.model_name,
        )

    @llm_completion_callback()
    def complete(self, prompt: str, **kwargs) -> CompletionResponse:
        response = self._client.chat(prompt)
        return CompletionResponse(text=response)

    @llm_completion_callback()
    def stream_complete(self, prompt: str, **kwargs) -> Iterator[CompletionResponse]:
        response = self.complete(prompt, **kwargs)
        yield response

Settings.llm = ClaudeLLMWrapper()

index = VectorStoreIndex.from_documents(documents)

# ====================== OPTIMIZED RETRIEVAL ======================
query_engine = index.as_query_engine(similarity_top_k=5)   # Reduced from 8 → 5


def analyze_supply_chain_impact(change_description: str) -> str:
    system_prompt = """You are a senior Aerospace Supply Chain & Procurement Analyst for the Eurus Systems MAAP program.

Analyze the supply chain and procurement impact of the proposed change. Be concise but thorough.

Use this structure:

## Supply Chain & Procurement Impact Brief

**Proposed Change:**  
[Clear restatement]

**Overall Supply Chain Impact Level:** High / Medium / Low + justification

**Key Suppliers & Parts Affected:**  
- List major affected parts and their suppliers

**Procurement & Lead Time Impact:**  
- Changes to lead times and long-lead item risks

**Make vs Buy Implications:**  
- Any shift in make/buy strategy or new supplier needs

**Risk Profile Changes:**  
- New or elevated supply chain risks and mitigation strategies

**Cost & Schedule Implications:**  
- Impact on material cost and program timeline

**Recommendations & Mitigations:**  
[Clear, actionable recommendations]

**Confidence Level:** X/10
"""

    # More targeted retrieval query
    retrieval = query_engine.query(
        f"Focus on supply chain, procurement, suppliers, lead times, and make-vs-buy implications for this change.\n\nChange: {change_description}"
    )

    final_prompt = f"""{system_prompt}

**Proposed Change:**  
{change_description}

**Relevant Context:**  
{retrieval}

Generate the Supply Chain & Procurement Impact Brief following the structure above."""

    response = Settings.llm.complete(final_prompt)
    return response.text


def save_brief(change_description: str, brief: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/Supply_Chain_Impact_Brief_{timestamp}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Supply Chain & Procurement Impact Brief\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**Proposed Change:** {change_description}\n\n")
        f.write(brief)
    return filename


if __name__ == "__main__":
    print("\n=== MAAP-1 Supply Chain & Procurement Impact Agent (Optimized) ===")
    change = input("Proposed Change: ").strip()
    if change.lower() not in ["quit", "exit", "q"]:
        brief = analyze_supply_chain_impact(change)
        print(brief)
        filepath = save_brief(change, brief)
        print(f"\n✅ Saved to: {filepath}")
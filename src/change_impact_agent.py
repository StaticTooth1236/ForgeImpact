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

# ====================== SETUP ======================
DATA_FOLDER = "data"
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
OUTPUT_DIR = "outputs/change_briefs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading documents...")
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


# ====================== OPTIMIZED AGENT ======================
def analyze_change_impact(change_description: str) -> str:
    system_prompt = """You are a senior Aerospace Change Impact Analyst for the Eurus Systems MAAP program.

Analyze the proposed change and produce a clear, professional Change Impact Brief.

Use this structure:

## Change Impact Brief

**Proposed Change:**  
[Clear restatement]

**Overall Impact Level:** High / Medium / Low + one-sentence justification

**Key Affected Areas:**  
- List the main areas impacted

**Impact Summary:**  
[Concise 3-5 sentence overview]

**Detailed Impacts:**
- **Configuration & Design:** ...
- **Bill of Materials & Supply Chain:** ...
- **Manufacturing & Production:** ...
- **Schedule (IMS):** ...
- **Risks & Certification:** ...

**Recommendations & Mitigations:**  
[Clear, actionable recommendations]

**Confidence Level:** X/10
"""

    # More targeted retrieval query
    retrieval = query_engine.query(
        f"Find relevant sections about this engineering change and its impacts on design, manufacturing, supply chain, and schedule.\n\nChange: {change_description}"
    )

    final_prompt = f"""{system_prompt}

**Proposed Change:**  
{change_description}

**Relevant Context from Program Documents:**  
{retrieval}

Generate the Change Impact Brief following the exact structure above. Be concise but thorough."""

    response = Settings.llm.complete(final_prompt)
    return response.text


def save_brief(change_description: str, brief: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/Change_Impact_Brief_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Change Impact Brief\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**Proposed Change:** {change_description}\n\n")
        f.write(brief)
    
    return filename


# ====================== INTERACTIVE ======================
if __name__ == "__main__":
    print("\n=== MAAP Change Impact Analyst (Optimized) ===")
    print("Type a proposed engineering change (or 'quit' to exit)\n")

    while True:
        change = input("Proposed Change: ").strip()
        if change.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        if not change:
            continue

        print("\nAnalyzing impact...\n")
        try:
            brief = analyze_change_impact(change)
            print(brief)
            
            filepath = save_brief(change, brief)
            print(f"\n✅ Brief saved to: {filepath}\n")
            print("="*70 + "\n")
        except Exception as e:
            print(f"Error: {e}\n")
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
OUTPUT_DIR = "outputs/risk_schedule_briefs"
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
def analyze_risk_schedule_impact(change_description: str) -> str:
    system_prompt = """You are a senior Aerospace Program Risk & Schedule Analyst for the Eurus Systems MAAP program.

Analyze how the proposed change affects **schedule (IMS)** and **risk profile**. Be concise but thorough.

Use this structure:

## Risk & Schedule Impact Brief

**Proposed Change:**  
[Clear restatement]

**Overall Schedule Impact Level:** High / Medium / Low + one-sentence justification

**Key Milestones Affected:**  
- List specific milestones from the IMS that are impacted

**Critical Path & Buffer Impact:**  
- How this affects the critical path and schedule margin

**Risk Profile Changes:**  
- New or elevated risks
- Overall change in program risk posture

**Manufacturing Ramp Implications:**  
- Impact on LRIP / FRP timeline

**Recommendations & Mitigations:**  
[Clear, actionable recommendations]

**Confidence Level:** X/10
"""

    # More targeted retrieval query
    retrieval = query_engine.query(
        f"Focus on schedule (IMS), milestones, risks, and manufacturing ramp implications for this change.\n\nChange: {change_description}"
    )

    final_prompt = f"""{system_prompt}

**Proposed Change:**  
{change_description}

**Relevant Context from Program Documents:**  
{retrieval}

Generate the Risk & Schedule Impact Brief following the exact structure above."""

    response = Settings.llm.complete(final_prompt)
    return response.text


def save_brief(change_description: str, brief: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/Risk_Schedule_Impact_Brief_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# Risk & Schedule Impact Brief\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**Proposed Change:** {change_description}\n\n")
        f.write(brief)
    
    return filename


# ====================== INTERACTIVE ======================
if __name__ == "__main__":
    print("\n=== MAAP Risk & Schedule Impact Agent (Optimized) ===")
    print("Enter a proposed change (or type 'quit' to exit)\n")

    while True:
        change = input("Proposed Change: ").strip()
        if change.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break
        if not change:
            continue

        print("\nAnalyzing risk and schedule impact...\n")
        try:
            brief = analyze_risk_schedule_impact(change)
            print(brief)
            
            filepath = save_brief(change, brief)
            print(f"\n✅ Brief saved to: {filepath}\n")
            print("="*70 + "\n")
        except Exception as e:
            print(f"Error: {e}\n")
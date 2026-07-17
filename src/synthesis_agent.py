import sys
import os
from datetime import datetime
from typing import Dict, ClassVar, Iterator

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
OUTPUT_DIR = "outputs/synthesis_reports"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading documents for Synthesis Agent...")
documents = SimpleDirectoryReader(DATA_FOLDER).load_data()

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
query_engine = index.as_query_engine(similarity_top_k=6)

def synthesize_change_analysis(
    change_description: str, 
    agent_outputs: Dict[str, str]
) -> str:
    """
    Takes outputs from multiple specialized agents and produces an
    Executive Summary + PMP-style Project Plan.
    """

    # Combine all agent outputs into context
    combined_context = ""
    for agent_name, output in agent_outputs.items():
        combined_context += f"\n\n=== {agent_name} Agent Output ===\n{output}\n"

    system_prompt = """You are a senior Aerospace Program Manager responsible for synthesizing cross-functional change impact analysis.

Your job is to create a clear, leadership-ready deliverable based on input from multiple specialized agents.

Use this exact structure:

## Executive Summary

**Proposed Change:**  
[Clear, concise restatement]

**Overall Program Impact Level:** High / Medium / Low + one-sentence justification

**Key Findings Across Functions:**
- Change Impact
- Risk & Schedule
- Supply Chain & Procurement
- Manufacturing & Production
(Highlight the most important 3–5 points)

**Recommended Decision:**  
Approve / Approve with Conditions / Reject + brief rationale

**Top Risks & Opportunities:**
- List the highest priority risks and any notable opportunities

---

## Project Plan (PMP Style)

### 1. Change Description & Objectives
### 2. Key Actions, Owners & Timeline
### 3. Major Milestones & Dependencies
### 4. Resource & Budget Implications
### 5. Risk Mitigation Plan
### 6. Recommended Next Steps & Decision Gates

**Confidence Level:** X/10  
(Explain any areas of uncertainty)
"""

    synthesis_prompt = f"""{system_prompt}

**Original Proposed Change:**  
{change_description}

**Combined Analysis from Domain Experts:**  
{combined_context}

Now generate the Executive Summary + Project Plan following the structure above. Be concise but actionable."""

    response = Settings.llm.complete(synthesis_prompt)
    return response.text


def save_synthesis_report(change_description: str, report: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{OUTPUT_DIR}/Synthesis_Report_{timestamp}.md"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# MAAP-1 Change Analysis - Executive Synthesis\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"**Proposed Change:** {change_description}\n\n")
        f.write("---\n\n")
        f.write(report)
    
    return filename


# ====================== STANDALONE TEST ======================
if __name__ == "__main__":
    print("\n=== MAAP-1 Synthesis Agent (Standalone Test) ===\n")
    
    change = input("Proposed Change: ").strip()
    if not change or change.lower() in ["quit", "exit"]:
        print("Exiting...")
        exit()

    # For testing, we'll use dummy agent outputs
    # In real use, this will come from the Coordinator
    dummy_outputs = {
        "Change Impact": "High impact on structure and certification...",
        "Risk & Schedule": "Medium schedule risk with 3-4 month engineering cycle...",
        "Supply Chain": "Medium-high supply chain impact...",
        "Manufacturing": "Medium manufacturing impact..."
    }

    print("\nSynthesizing analysis...")
    report = synthesize_change_analysis(change, dummy_outputs)
    
    print("\n" + report)
    
    filepath = save_synthesis_report(change, report)
    print(f"\n✅ Synthesis report saved to: {filepath}")
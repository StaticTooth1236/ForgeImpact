import sys
import os
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

print("Loading documents from data/ folder...")
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

print("Creating vector index...")
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine(similarity_top_k=5)

print("\n=== MAAP-1 RAG System Ready (with Citations) ===")
print("Type your question (or 'quit' to exit)\n")

while True:
    question = input("Question: ").strip()
    if question.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    if not question:
        continue

    print("\nThinking...")
    try:
        response = query_engine.query(question)
        
        print(f"\nAnswer:\n{response.response}\n")
        
        if response.source_nodes:
            print("Sources:")
            for i, node in enumerate(response.source_nodes[:5], 1):
                file_name = node.metadata.get("file_name", "Unknown")
                print(f"  {i}. {file_name} (Score: {node.score:.3f})")
            print()
    except Exception as e:
        print(f"❌ Error: {e}\n")
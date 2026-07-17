import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

def build_rag_index():
    documents = SimpleDirectoryReader("data").load_data()
    index = VectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir="./storage")
    print("✅ RAG index built successfully!")
    return index

if __name__ == "__main__":
    index = build_rag_index()
    
    # Retrieval only
    retriever = index.as_retriever(similarity_top_k=3)
    nodes = retriever.retrieve("What is the MAAP-1 system?")
    
    print("\nRetrieved Information:")
    for i, node in enumerate(nodes):
        print(f"\n--- Chunk {i+1} ---")
        print(node.text[:600] + "...")
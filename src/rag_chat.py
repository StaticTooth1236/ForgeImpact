import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from src.llm_client import LLMClient

Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

llm = LLMClient()

def main():
    print("=== MAAP-1 RAG Chat (Groq Powered) ===\nType 'quit' to exit.\n")
    
    while True:
        q = input("Question: ")
        if q.lower() in ['quit', 'exit']:
            break
        
        # Retrieve relevant chunks
        retriever = index.as_retriever(similarity_top_k=4)
        nodes = retriever.retrieve(q)
        context = "\n\n".join([node.text for node in nodes])
        
        # Use your working Groq LLMClient to synthesize a good answer
        prompt = f"""Use the following context to answer the question accurately.

Context:
{context}

Question: {q}

Answer:"""
        
        response = llm.chat(prompt)
        print("Answer:", response, "\n")

if __name__ == "__main__":
    main()
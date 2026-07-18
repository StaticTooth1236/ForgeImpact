"""
MAAP-1 RAG System
-----------------
This file is a LIBRARY first, and a chat app second.

- Other scripts import from it:   from src.rag_system import query_rag, format_context
- Run it directly for a Q&A REPL: python3 src/rag_system.py

IMPORTANT: Nothing heavy runs at import time. All document loading and index
building happens lazily inside get_index(). The interactive chat loop lives
behind the `if __name__ == "__main__":` guard, so importing this module from
synthesis_agent.py is safe and instant.
"""

import os
import sys
import threading

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv

load_dotenv()

DATA_FOLDER = "data"
PERSIST_DIR = "storage/rag_index"   # delete this folder to force a rebuild after changing data/
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

_index = None  # cached so the index is loaded/built only once per process
_index_lock = threading.Lock()  # prevents parallel threads from building it twice


def get_index():
    """Load the vector index from disk if it exists; otherwise build and persist it.

    Thread-safe: when multiple agent threads call query_rag() at once, exactly
    one thread loads the embedding model and builds/loads the index; the rest
    wait at the lock and then reuse the cached result.
    """
    global _index
    if _index is not None:
        return _index

    with _index_lock:
        # Double-check: another thread may have finished while we waited.
        if _index is not None:
            return _index
        _index = _build_or_load_index()
    return _index


def _build_or_load_index():
    # Imports live inside the function so `import rag_system` stays instant.
    from llama_index.core import (
        VectorStoreIndex,
        SimpleDirectoryReader,
        Settings,
        StorageContext,
        load_index_from_storage,
    )
    from llama_index.embeddings.huggingface import HuggingFaceEmbedding

    Settings.embed_model = HuggingFaceEmbedding(model_name=EMBEDDING_MODEL)
    Settings.llm = None  # retrieval only — LlamaIndex never calls an LLM for us

    if os.path.exists(os.path.join(PERSIST_DIR, "docstore.json")):
        print(f"[rag] Loading existing index from {PERSIST_DIR} ...")
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    else:
        print(f"[rag] Building index from {DATA_FOLDER}/ (first run only) ...")
        documents = SimpleDirectoryReader(DATA_FOLDER).load_data()
        print(f"[rag] Loaded {len(documents)} source documents.")
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print(f"[rag] Index built and saved to {PERSIST_DIR}.")

    return index


def query_rag(question: str, top_k: int = 5, file_filter: str = None) -> list:
    """
    Retrieve the most relevant chunks for a question.

    Returns a list of dicts: {"file_name": str, "text": str, "score": float}

    file_filter: if provided, only return chunks whose source file name contains
    this string (matched by filename stem, so "_continuation" variants count).
    When filtering, we score a very wide net of chunks (cheap, local math) so
    quiet documents still surface their best content instead of being drowned
    out by semantically loud ones.
    """
    index = get_index()
    retrieve_k = 300 if file_filter else top_k
    retriever = index.as_retriever(similarity_top_k=retrieve_k)
    nodes = retriever.retrieve(question)

    stem = None
    if file_filter:
        stem = file_filter.lower().removesuffix(".md")

    results = []
    for node in nodes:
        file_name = node.metadata.get("file_name", "Unknown")
        if stem and stem not in file_name.lower():
            continue
        results.append({
            "file_name": file_name,
            "text": node.get_content(),
            "score": node.score if node.score is not None else 0.0,
        })
        if len(results) >= top_k:
            break
    return results


def format_context(results: list) -> str:
    """Format retrieval results into a labeled context block for a prompt."""
    if not results:
        return "(no relevant content found in program documents)"
    blocks = [
        f"[Source: {r['file_name']} | relevance {r['score']:.2f}]\n{r['text']}"
        for r in results
    ]
    return "\n\n---\n\n".join(blocks)


# ---------------------------------------------------------------------------
# Interactive Q&A REPL — only runs when you execute this file directly.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    from src.claude_client import ClaudeClient

    claude = ClaudeClient()
    get_index()  # warm up before first question

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
            results = query_rag(question, top_k=5)
            context = format_context(results)
            prompt = (
                f"Program document excerpts:\n\n{context}\n\n"
                f"Question: {question}\n\n"
                "Answer using only the excerpts above. Cite source file names."
            )
            answer = claude.chat(
                prompt,
                system_prompt="You are a precise aerospace program analyst for the MAAP-1 program.",
            )
            print(f"\nAnswer:\n{answer}\n")
            print("Sources:")
            for i, r in enumerate(results, 1):
                print(f"  {i}. {r['file_name']} (Score: {r['score']:.3f})")
            print()
        except Exception as e:
            print(f"❌ Error: {e}\n")
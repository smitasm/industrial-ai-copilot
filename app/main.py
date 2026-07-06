from config.settings import (
    PDF_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model
from rag.vector_store import create_vector_store
from rag.retriever import get_retriever
from rag.llm import get_llm
from rag.rag_chain import ask_question

def main():

    print("=" * 70)
    print("Industrial AI Copilot")
    print("=" * 70)

    documents = load_documents(PDF_PATH)

    print(f"✅ Total Pages Loaded : {len(documents)}")

    chunks = split_documents(
        documents,
        CHUNK_SIZE,
        CHUNK_OVERLAP
    )

    print(f"✅ Total Chunks : {len(chunks)}")

    print("\nLoading Embedding Model...")
    embedding_model = get_embedding_model()

    print("\n Creating Vector Store...")
    vector_store =create_vector_store(
        chunks,
        embedding_model
    )
    print("✅ Vector Store Created ")
    print("\nCollection count: ",vector_store._collection.count()
          
          )   
    print(f"\n Creating Retriever...")
    retriever = get_retriever(vector_store)
    print("✅ Retriever Created ")

    print("\nLoading LLM...")
    llm = get_llm()
    print("✅ LLM Loaded ")

    question = input("/nAsk your question: ")
    answer = ask_question(
        question, 
        retriever,
        llm
    )
    print("\n " + "=" *80)
    print("\nANSWER: ")
    print("\n " + "=" *80)
    print(answer)

if __name__ == "__main__":
    main()
    

from rag.embeddings import get_embedding_model
from rag.vector_store import load_vector_store
from rag.retriever import get_retriever
from rag.llm import get_llm
from rag.rag_chain import ask_question


def main():

    print("=" * 80)
    print("INDUSTRIAL AI COPILOT")
    print("=" * 80)

    print("\nLoading embedding model...")
    embedding_model = get_embedding_model()

    print("Loading vector database...")
    vector_store = load_vector_store(embedding_model)

    print("Creating retriever...")
    retriever = get_retriever(vector_store)

    print("Loading LLM...")
    llm = get_llm()

    print("\n✅ AI Copilot Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() in ["exit", "quit"]:

            print("\nGoodbye!")
            break

        answer = ask_question(
            question,
            retriever,
            llm,
        )

        print("\nAssistant:")
        print(answer)
        print("-" * 80)


if __name__ == "__main__":
    main()
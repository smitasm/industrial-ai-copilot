from rag.embeddings import get_embedding_model
from rag.vector_store import load_vector_store
from rag.retriever import get_retriever
from rag.llm import get_llm
from agents.planner_agent import PlannerAgent
from agents.retrieval_agent import RetrievalAgent
from agents.memory_agent import MemoryAgent
from agents.report_agent  import ReportAgent
from agents.vision_agent import VisionAgent
from graph.workflow import Workflow


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

    # Create Retrieval Agent (only once)
    retrieval_agent = RetrievalAgent(
        retriever=retriever,
        llm=llm
    )

    vision_agent = VisionAgent()
    report_agent = ReportAgent()
    memory_agent = MemoryAgent()
    planner = PlannerAgent()

    workflow = Workflow(
    planner_agent=planner,
    retrieval_agent=retrieval_agent,
    report_agent= report_agent,
    memory_agent= memory_agent,
    vision_agent= vision_agent
)

    print("\n✅ AI Copilot Ready!")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ")

        if question.lower() in ["exit", "quit"]:
            print("\nGoodbye!")
            break

        state = workflow.run(question)

       
        print("\n Assistant :")
        print(state["result"]["answer"])

       ## if(result["debug"]):
       ##     print_debug_info(result)

        


if __name__ == "__main__":
    main()
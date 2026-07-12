import time

from rag.prompt import RAG_PROMPT
from rag.retriever import retrieve_with_scores


def ask_question(
        question,
        retriever,
        llm,
        debug=False
):

    vector_store = retriever.vectorstore

    total_start = time.perf_counter()

    # ---------------- Retrieval ----------------

    retrieval_start = time.perf_counter()

    docs_with_scores = retrieve_with_scores(
        vector_store,
        question,
        k=5
    )

    retrieval_time = (
        time.perf_counter() - retrieval_start
    )

    docs = [
        doc
        for doc, score in docs_with_scores
    ]

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = RAG_PROMPT.invoke({
        "context": context,
        "question": question
    })

    # ---------------- LLM ----------------

    llm_start = time.perf_counter()

    response = llm.invoke(prompt)

    llm_time = (
        time.perf_counter() - llm_start
    )

    total_time = (
        time.perf_counter() - total_start
    )

    if debug:

        return {

            "agent": "Retrieval Agent",

            "answer": response.content,

            "debug": {

                "question": question,

                "context": context,

                "docs_with_scores": docs_with_scores,

                "prompt": prompt,

                "metrics": {

                    "retrieval_time": retrieval_time,

                    "llm_time": llm_time,

                    "total_time": total_time

                }

            }

        }

    return {

        "agent": "Retrieval Agent",

        "answer": response.content,

        "debug": None

    }
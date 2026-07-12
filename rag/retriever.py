from langchain_core.documents import Document


def get_retriever(vector_store, k=5):
    return vector_store.as_retriever(
        search_kwargs={"k": k}
    )


def retrieve_with_scores(vector_store, question, k=5):
    """
    Returns:
    [
        (Document, score),
        (Document, score),
        ...
    ]
    """
    return vector_store.similarity_search_with_score(
        question,
        k=k
    )
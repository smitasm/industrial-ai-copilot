from langchain_chroma import Chroma


def get_retriever(
    vector_db: Chroma,
    k: int = 5
):
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
    )

    return retriever


def retrieve_with_scores(
    vector_db: Chroma,
    question: str,
    k: int = 5
):
    """
    Returns:
        [
            (Document, score),
            (Document, score),
            ...
        ]
    """

    return vector_db.similarity_search_with_score(
        query=question,
        k=k
    )
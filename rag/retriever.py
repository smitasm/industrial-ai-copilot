from langchain_chroma import Chroma

def get_retriever(
    vector_db: Chroma,
    k: int=5
):
    retriever = vector_db.as_retriever(
    search_type="similarity",
    search_kwargs={"k": k})

    return retriever
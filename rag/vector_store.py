from pathlib import Path

from langchain_chroma import Chroma

VECTOR_DB_PATH = "vector_store"


def create_vector_store(
    chunks,
    embedding_model,
    persist_directory=VECTOR_DB_PATH,
):
    """
    Create and persist a Chroma vector database.
    """

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
    )

    return vector_db


def load_vector_store(
    embedding_model,
    persist_directory=VECTOR_DB_PATH,
):
    """
    Load an existing Chroma vector database.
    """

    return Chroma(
        persist_directory=persist_directory,
        embedding_function=embedding_model,
    )


def vector_store_directory_exists() -> bool:
    """
    Check whether the vector database directory exists.
    """

    if not Path(VECTOR_DB_PATH).exists():
        return False

    return any(Path(VECTOR_DB_PATH).iterdir())


def is_collection_populated(vector_store) -> bool:
    """
    Returns True if the Chroma collection contains vectors.
    """

    return vector_store._collection.count() > 0
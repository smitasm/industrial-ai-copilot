from config.settings import (
    PDF_PATH,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

from rag.loader import load_documents
from rag.splitter import split_documents
from rag.embeddings import get_embedding_model

from rag.vector_store import (
    create_vector_store,
    load_vector_store,
    vector_store_directory_exists,
    is_collection_populated,
)


def main():

    print("=" * 80)
    print("INDEXING PIPELINE")
    print("=" * 80)

    print("\nLoading embedding model...")
    embedding_model = get_embedding_model()

    # -------------------------------------------------------
    # Check whether an index already exists
    # -------------------------------------------------------

    if vector_store_directory_exists():

        print("Existing vector database found.")

        vector_store = load_vector_store(embedding_model)

        if is_collection_populated(vector_store):

            print("Index already populated.")
            print("Skipping indexing.")

            return

    # -------------------------------------------------------
    # Build a new index
    # -------------------------------------------------------

    print("\nLoading PDF...")

    documents = load_documents(PDF_PATH)

    print(f"✅ Total Pages Loaded : {len(documents)}")

    print("\nSplitting document...")

    chunks = split_documents(
        documents,
        CHUNK_SIZE,
        CHUNK_OVERLAP,
    )

    print(f"✅ Total Chunks : {len(chunks)}")

    print("\nCreating Vector Store...")

    create_vector_store(
        chunks,
        embedding_model,
    )

    print("\n✅ Indexing completed successfully.")


if __name__ == "__main__":
    main()
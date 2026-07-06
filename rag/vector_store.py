from langchain_chroma import Chroma

def create_vector_store(chunks,embedding_model,persist_directory="vector_store"):
    vector_db= Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory
    )
    return vector_db

    
from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents, chunk_size, chunk_overlap):
    """
    Split documents into semantic chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    return splitter.split_documents(documents)
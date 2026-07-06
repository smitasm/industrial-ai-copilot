from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_documents(pdf_path: Path):
    """
    Load PDF documents.

    Args:
        pdf_path: Path to PDF file

    Returns:
        List of LangChain Document objects
    """

    loader = PyPDFLoader(str(pdf_path))

    return loader.load()
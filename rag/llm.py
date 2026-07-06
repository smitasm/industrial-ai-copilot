from langchain_ollama import ChatOllama

def get_llm():
    llm = ChatOllama(
        model="phi3:mini",
        temperature=0
    )
    return llm

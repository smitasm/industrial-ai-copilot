from rag.rag_chain import ask_question

class RetrievalAgent:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def run(self, question, debug=False):
        result = ask_question(
            question= question,
            retriever= self.retriever,
            llm= self.llm,
            debug= debug

        )
        return result
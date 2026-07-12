from rag.prompt import RAG_PROMPT

def ask_question(
        question,
        retriever,
        llm,
        debug=False
):
    docs=retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = RAG_PROMPT.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(prompt)
    if debug:
        return {
            "agent" : "Retrival agent",
            "answer" : response.content,
            "debug" :{
            "context" : context,
            "docs" : docs,
            "prompt" : prompt
            }
        }

    return {
        "agent" : "Retrieval agent",
        "answer" : response.context,
        "debug" : None
    }

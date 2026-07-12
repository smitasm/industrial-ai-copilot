class MemoryAgent:
    def __init__(self):
        print("Memory agent is initiazed")

    def run(self, question, debug=False):
        result = {
            "agent" : "MemoryAgent",
            "answer": "Memory agent is under development"
        }

        if debug:
            result["debug"] ={}
        return result
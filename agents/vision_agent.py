class VisionAgent:

    def __init__(self):
        print("Vision Agent Initialized")

    def run(self, question, debug=False):

        result = {
            "agent": "VisionAgent",
            "answer": "Vision Agent is under development."
        }

        if debug:
            result["debug"] = {}

        return result
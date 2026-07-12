class ReportAgent:
    def __init__(self):
        print("Report agebt initialized")

    def run(self, question, debug=False):
        result ={
            "agent" : "ReportAgent",
            "answer" : "Reprot agent is under developement"
        }
        if debug:
            result["debug"] ={}
        return result
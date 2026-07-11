class PlannerAgent:

    def __init__(
        self,
        retrieval_agent,
        memory_agent=None,
        vision_agent=None,
        report_agent=None
    ):
        self.retrieval_agent = retrieval_agent
        self.memory_agent = memory_agent
        self.vision_agent = vision_agent
        self.report_agent = report_agent

    def route(self, question: str):

        """
        Decide which agent should handle the request.
        Version 1 uses simple rules.
        """

        question = question.lower()

        if "image" in question or "photo" in question:
            return "vision"

        if "report" in question:
            return "report"

        if "previous" in question or "summarize" in question:
            return "memory"

        return "retrieval"

    def run(self, question):

        agent = self.route(question)

        if agent == "retrieval":
            return self.retrieval_agent.run(
                question,
                debug=True
            )

        elif agent == "memory":

            return {
                "agent": "MemoryAgent",
                "answer": "Memory Agent not implemented."
            }

        elif agent == "vision":

            return {
                "agent": "VisionAgent",
                "answer": "Vision Agent not implemented."
            }

        elif agent == "report":

            return {
                "agent": "ReportAgent",
                "answer": "Report Agent not implemented."
            }
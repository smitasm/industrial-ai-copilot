class PlannerAgent:
    """
    Decides which agent should handle a user request.
    """

    def __init__(self):
      print("Planner Agent Initialized")
      
    def route(self, question: str) -> str:
        """
        Decide which agent should handle the request.
        Version 1 uses simple keyword-based routing.
        """

        question = question.lower()

        if "image" in question or "photo" in question:
            return "vision"

        if "report" in question:
            return "report"

        if "previous" in question or "summarize" in question:
            return "memory"

        return "retrieval"

    
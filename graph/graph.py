from langgraph.graph import StateGraph, END
from graph.state import GraphState
from agents.planner_agent import PlannerAgent
from agents.retrieval_agent import RetrievalAgent

class IndustrialCopilotGraph:
    def __init__(self):
        self.planner = PlannerAgent
        self.retrieval_agent = RetrievalAgent
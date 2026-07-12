from langgraph.graph import StateGraph, START, END

from graph.state import GraphState

class Workflow:
    def __init__(self, planner_agent, retrieval_agent, memory_agent, report_agent, vision_agent):
        self.planner_agent = planner_agent
        self.retrieval_agent = retrieval_agent
        self.memory_agent = memory_agent
        self.report_agent = report_agent
        self.vision_agent = vision_agent
        self.graph = StateGraph(GraphState)

        self.graph.add_node(
            "planner", self.planner_node
        )
        self.graph.add_node(
            "retrieval", self.retrieval_node
        )
        self.graph.add_node(
             "vision", self.vision_node
        )
        self.graph.add_node(
             "report", self.report_node
        )
        self.graph.add_node(
             "memory", self.memory_node
        )
        self.graph.add_edge(START, "planner")

        self.graph.add_conditional_edges(
            "planner",
            lambda state: state["route"],
            {
                "retrieval" : "retrieval",
                "vision" : "vision",
                "report" :"report",
                "memory" : "memory"
            }
        )
        
        self.graph.add_edge("retrieval", END)
        self.graph.add_edge("vision", END)
        self.graph.add_edge("report", END)
        self.graph.add_edge("memory", END)
        self.app = self.graph.compile()

    def run(self,question):
            state = {
                "question" : question
            }
            return self.app.invoke(state)

    def planner_node(self, state:GraphState):
        print("\n ================ PLANNER NODE ===============")
        question = state["question"]
        route = self.planner_agent.route(question)
        print(f"question : {question}")
        print(f"route: {route}")
        state["route"] = route
        return state
        

    def retrieval_node(self, state:GraphState):
        print("\n =============== RETRIEVAL NODE ===============")
        result = self.retrieval_agent.run(
            state["question"],
            debug = True
        )
        state["result"] = result
        return state

    def memory_node(self, state:GraphState):
        print("\n =============== MEMORY NODE ===============")
        result = self.memory_agent.run(
            state["question"],
            debug = True
        )
        state["result"] = result
        return state
    
    def report_node(self, state:GraphState):
        print("\n =============== REPORT NODE ===============")
        result = self.report_agent.run(
            state["question"],
            debug = True
        )
        state["result"] = result
        return state
    
    def vision_node(self, state:GraphState):
        print("\n =============== VISION NODE ===============")
        result = self.vision_agent.run(
            state["question"],
            debug = True
        )
        state["result"] = result
        return state

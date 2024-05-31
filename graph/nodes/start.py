from typing import Any, Dict

from graph.state import GraphState
from langgraph.graph import StateGraph


def start(state: GraphState, workflow: StateGraph) -> Dict[str, Any]:
    print("###start###")

    return {"theGraph": workflow}

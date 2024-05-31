from typing import Any, Dict
from graph.state import GraphState
from graph.graph_utils import draw

from graph.chains.router import question_router

def process_input(state: GraphState) -> Dict[str, Any]:

    print("###ROUTE QUESTION###")
    draw("process_input", state["theGraph"])
    question = state["question"]
    source = question_router.invoke({"question": question})

    print("---ROUTE QUESTION TO "+source.datasource+"---")
    return({"thenode": source.datasource,"question": question})

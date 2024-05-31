from typing import Any, Dict
from graph.state import GraphState
from graph.graph_utils import draw

from graph.consts import START,ROUTE_QUESTION, GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH

def decide_to_generate(state: GraphState) -> Dict[str, Any]:
    print("###ASSESS GRADED DOCUMENTS###")
    draw("decide_to_generate", state["theGraph"])
    if state["web_search"]:
        print(
            "---DECISION: NOT ALL DOCUMENTS ARE NOT RELEVANT TO QUESTION, INCLUDE WEB SEARCH---"
        )
        return({"thenode": WEBSEARCH})
    else:
        print("---DECISION: GENERATE---")
        return({"thenode": GENERATE})

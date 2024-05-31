# generate.py
from typing import Any, Dict

from graph.chains.generation import generation_chain
from graph.state import GraphState

from graph.graph_utils import draw

def generate(state: GraphState) -> Dict[str, Any]:
    print("###GENERATE###")
    question = state["question"]
    documents = state["documents"]
    draw("generate", state["theGraph"])
    generation = generation_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

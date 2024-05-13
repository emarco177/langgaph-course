from typing import Any, Dict

from graph.chains.generation import augmented_chain
from graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    generation = augmented_chain.invoke({"context": documents, "question": question})
    return {"documents": documents, "question": question, "generation": generation}

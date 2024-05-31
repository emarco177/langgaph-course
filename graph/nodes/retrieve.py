from typing import Any, Dict

from graph.state import GraphState
from ingestion import retriever

from graph.graph_utils import draw

def retrieve(state: GraphState) -> Dict[str, Any]:
    print("###RETRIEVE###")
    draw("retrieve", state["theGraph"])
    question = state["question"]

    documents = retriever.invoke(question)
    return {"documents": documents, "question": question}

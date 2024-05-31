# state.py
from typing import List, TypedDict
from langgraph.graph import StateGraph

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        web_search: whether to add search
        documents: list of documents
        theGraph: StateGraph
    """

    question: str
    generation: str
    web_search: bool
    documents: List[str]
    thenode:str
    theGraph: StateGraph

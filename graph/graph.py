#graph.py
from dotenv import load_dotenv
from langgraph.graph import END, StateGraph
from graph.consts import START,ROUTE_QUESTION, GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH
from graph.nodes import start, generate, grade_documents, retrieve, web_search, process_input,decide_to_generate,check_hallucinations 
from graph.state import GraphState

from graph.graph_utils import draw

load_dotenv()

def route_node(state: GraphState):
    print("==Go To==> "+ state["thenode"] )
    return state["thenode"]

workflow = StateGraph(GraphState)
workflow.add_node(START, lambda state: start(state, workflow))
workflow.add_node("process_input",process_input)
workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node("decide_to_generate", decide_to_generate)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEBSEARCH, web_search)
workflow.add_node("check_hallucinations",check_hallucinations)

workflow.set_entry_point(START)
workflow.add_edge(START,"process_input")
workflow.add_conditional_edges("process_input",
    route_node,
    {
        WEBSEARCH: WEBSEARCH,
        "vectorstore": RETRIEVE,
    },
)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_edge(GRADE_DOCUMENTS,"decide_to_generate")
workflow.add_conditional_edges(
    "decide_to_generate",
    route_node,
    {
        WEBSEARCH: WEBSEARCH,
        GENERATE: GENERATE,
    },
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, "check_hallucinations")
workflow.add_conditional_edges(
    "check_hallucinations",
    route_node,
    {
        "not supported": GENERATE,
        "useful": END,
        "not useful": WEBSEARCH,
    },
)

app = workflow.compile()

app.get_graph().draw_mermaid_png(output_file_path="graph.png")

# graph_utils.py
import requests
from langgraph.graph import StateGraph
from collections import defaultdict

def dot_to_ascii(dot: str, fancy: bool = True) -> str:
    url = 'https://dot-to-ascii.ggerganov.com/dot-to-ascii.php'
    boxart = 1 if fancy else 0
    params = {
        'boxart': boxart,
        'src': dot,
    }
    response = requests.get(url, params=params).text
    if response == '':
        raise SyntaxError('DOT string is not formatted correctly')
    return response

def generate_dot_with_highlight(graph, current_node: str) -> str:
   # print(f"Debug: StateGraph attributes: {dir(graph)}")
   # print(f"Debug: Graph nodes: {graph.nodes}")
   # print(f"Debug: Graph edges: {graph.edges}")
   # print(f"Debug: Graph all nodes: {graph._all_edges}")
   # print(f"Debug: Graph branches: {graph.branches}")
   # print(f"Debug: Graph channels: {graph.channels}")
   # print(f"Debug: Graph waiting: {graph.waiting_edges}")
   # print(f"Debug: Graph current node: {current_node}")
    dot = 'digraph {\n    rankdir=LR;\n    node [shape=box];\n'

    for node in graph.nodes:
        peripheries = "2" if node == current_node else "1"
        dot += f'    {node} [label="{node}" peripheries={peripheries}];\n'

    for edge in graph.edges:
        dot += f'    {edge[0]} -> {edge[1]};\n'

    # Add branches to the DOT graph
    for start_node, branch_dict in graph.branches.items():
        for branch_name, branch in branch_dict.items():
            for end_label, end_node in branch.ends.items():
                dot += f'    {start_node} -> {end_node} [label="{end_label}"];\n'

    dot += '}'
   # print(dot)
    return dot

def draw(node: str, graph: StateGraph):
    # Highlight the current node
    dot = generate_dot_with_highlight(graph, node)
    graph_ascii = dot_to_ascii(dot)
    print(graph_ascii)


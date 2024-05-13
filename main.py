from pprint import pprint

from graph.graph import app

app.get_graph().draw_mermaid_png(output_file_path="./graph/graph.png")

question1 = "What are the types of agent memory?"
question2 = "How does the AlphaCodium paper work?"
inputs = {"question": question2}

for output in app.stream(inputs):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")
pprint(value["generation"])

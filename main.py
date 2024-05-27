from dotenv import load_dotenv

load_dotenv()
from pprint import pprint

from graph.graph import app

question1 = "What are the types of agent memory?"
question2 = "How can i do fine tunning image"
input1 = {"question": question1}
input2 = {"question": question2}

for output in app.stream(input2):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")

pprint(value["question"])
pprint(value["generation"])
for doc in value["documents"]:
    print(f"doc.page_content: {doc.page_content}\n")
else:
    print("No more documents")

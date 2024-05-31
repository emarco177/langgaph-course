# main.py
from dotenv import load_dotenv

load_dotenv()
from pprint import pprint

from graph.graph import app

question1 = "What are the types of agent memory?"
question2 = "What is the weather today in Paris?"
inputs = {"question": question2}

for output in app.stream(inputs):
    for key, value in output.items():
        pprint(f"Finished running: {key}:")
pprint(value["generation"])

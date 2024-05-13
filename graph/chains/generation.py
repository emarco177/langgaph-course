from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from ingestion import retriever

question = "agent memory"
docs = retriever.invoke(question)
doc_txt = docs[1].page_content


llm = ChatOpenAI(temperature=0)
prompt = hub.pull("rlm/rag-prompt")

augmented_chain = prompt | llm | StrOutputParser()

# generation = augmented_chain.invoke({"context": docs, "question": question})
# print(generation)

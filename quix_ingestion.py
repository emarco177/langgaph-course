import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from quixstreams import Application
from dotenv import load_dotenv
from quixstreams.kafka import AutoOffsetReset
import json


def main():
    urls = []
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )
    load_dotenv()

    # Create an Application
    kafka_app = Application(
        quix_sdk_token=os.getenv("QUIX_SDK_TOKEN"),
        consumer_group="csv_sample",
        # auto_offset_reset=AutoOffsetReset.latest,
        auto_create_topics=False,
    )

    # Define the topic using the "output" environment variable
    topic_name = os.environ["input-topic"]
    topic = kafka_app.topic(topic_name)

    with kafka_app.get_consumer() as consumer:
        consumer.subscribe([topic.name])
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is not None:
                value = msg.value().decode("UTF-8")
                # Analizar la cadena JSON
                # Cargar la cadena JSON en un diccionario de Python
                data = json.loads(value)

                # Recorrer las claves del diccionario y capturar la URL completa
                for key in data.keys():
                    if key.startswith("https://"):
                        url_completa = key
                        break

                print("La URL completa es:", url_completa)
                urls.append(url_completa)
                docs = WebBaseLoader(url_completa).load()
                print(f"Loaded documents {docs}")
                # docs_list = [item for sublist in docs for item in sublist]
                print(f"Loaded docs_list {docs}")
                doc_splits = text_splitter.split_documents(docs)
                # print(f" Loaded doc_splits {doc_splits}")
                vectorstore = Chroma.from_documents(
                    documents=doc_splits,
                    collection_name="rag-chroma",
                    embedding=OpenAIEmbeddings(),
                    persist_directory="./.chroma",
                )
                print(f"Loaded vectorstore {vectorstore}")
                retriever = Chroma(
                    collection_name="rag-chroma",
                    persist_directory="./.chroma",
                    embedding_function=OpenAIEmbeddings(),
                ).as_retriever()
                print(f"Loaded retriever {retriever}")
                print(f"urls {urls}\n")
                # Optionally commit the offset
                # consumer.store_offsets(msg.offset())


if __name__ == "__main__":
    main()

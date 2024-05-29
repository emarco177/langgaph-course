# Python code to demonstrate the creation of a document hierarchy in a knowledge graph for legal documents
from langchain_core.prompts import ChatPromptTemplate
from py2neo import Graph, Node, Relationship
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
import py2neo

from langchain.graphs import Neo4jGraph
import requests
import os
from langchain_community.vectorstores import Neo4jVector
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.chains import GraphCypherQAChain
from langchain.agents import initialize_agent, Tool, create_react_agent, create_openai_functions_agent
from langchain.agents import AgentType

load_dotenv()

def create_pinecone_index(index_name, pc):
    index = pc.Index(index_name)
    if index.exists:
        print("Index already exists, skipping creation")
    else:
        print("Creating index")
        pc.create_index(
            name=index_name,
            dimension=8,  # Replace with your model dimensions
            metric="euclidean",  # Replace with your model metric
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )


# Python code to demonstrate query augmentation using a knowledge graph
def augment_query(device, issue):
    # Assume a function that retrieves device-specific issues from a knowledge graph
    query_context = get_device_context(device)
    enhanced_query = f"{issue} related to {query_context}"
    return enhanced_query


def get_device_context(device):
    # Mock function to simulate retrieval from a knowledge graph
    context_mapping = {
        'Model X': 'hardware',
        'Model Y': 'software'
    }
    return context_mapping.get(device, 'general')


# Python code to demonstrate query planning with a knowledge graph
def plan_query(main_query):
    sub_topics = get_sub_topics(main_query)
    results = {}
    for topic in sub_topics:
        results[topic] = retrieve_data(topic)
    return synthesize_results(results)


def get_sub_topics(query):
    # Mock function to simulate sub-topic extraction from a knowledge graph
    return ["solar energy innovations", "key researchers in solar energy", "recent solar energy projects"]


def retrieve_data(topic):
    # Mock function to simulate data retrieval
    data = {
        'solar energy innovations': "Advancements in photovoltaic cells",
        'key researchers in solar energy': "Dr. Jane Doe, leading solar panel efficiency",
        'recent solar energy projects': "Solar Park in Sahara"
    }
    return data.get(topic, "No data found")


def synthesize_results(results):
    return " ".join([f"{key}: {value}" for key, value in results.items()])


# Python code to demonstrate dynamic learning in a knowledge graph
def update_knowledge_graph(new_data):
    # Assume a function that integrates new data into the existing knowledge graph
    integrate_data(new_data)
    print("Knowledge graph updated with new data.")


def integrate_data(data):
    # Mock function to simulate the integration of new economic data into a knowledge graph
    # This would typically involve adding new nodes or updating existing nodes/relationships
    print(f"Integrating data: {data}")

    # Sample data update
    new_financial_regulation = "2024 Financial Compliance Standards"
    update_knowledge_graph(new_financial_regulation)


def export_graph_to_csv(graph, output_dir):
    """
    Exporta el grafo de Neo4j a archivos CSV.

    Args:
        graph (py2neo.Graph): Objeto Graph de la conexión a Neo4j.
        output_dir (str): Directorio de salida para los archivos CSV.
    """
    # Exportar nodos
    nodes = graph.run("MATCH (n) RETURN n").data()
    with open(f"{output_dir}/nodes.csv", "w", encoding="utf-8") as f:
        f.write("#id,label")
        for node in nodes:
            node_data = node["n"]
            node_id = str(node_data.identity)
            node_label = node_data.labels
            f.write(f"\n{node_id},{node_label}")

    # Exportar relaciones
    rels = graph.run("MATCH ()-[r]->() RETURN r").data()
    with open(f"{output_dir}/relationships.csv", "w", encoding="utf-8") as f:
        f.write("#source,target,type")
        for rel in rels:
            rel_data = rel["r"]
            source_id = str(rel_data.start_node.identity)
            target_id = str(rel_data.end_node.identity)
            rel_type = rel_data.type
            f.write(f"\n{source_id},{target_id},{rel_type}")


def neo4j_local():
    # Connect to a Neo4j database
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
    # Create nodes
    tort_law = Node("Law", name="Tort Law")
    civil_rights = Node("Law", name="Civil Rights Law")
    case_study = Node("Document", name="Case Study on Civil Rights")
    # Create relationships
    related_to_rel = Relationship(tort_law, "RELATED_TO", civil_rights)
    has_document_rel = Relationship(civil_rights, "HAS_DOCUMENT", case_study)
    tx = graph.begin()
    # Crear una transacción y ejecutar las operaciones
    tx.create(tort_law)
    tx.create(civil_rights)
    tx.create(case_study)
    tx.create(related_to_rel)
    tx.create(has_document_rel)
    graph.commit(tx)
    print("graph created")
    # Query to retrieve related documents
    query = """
    MATCH (l:Law {name: 'Civil Rights Law'})-[:HAS_DOCUMENT]->(d)
    RETURN d.name AS Document
    """
    print(f"query: {query}")
    result = graph.run(query)
    for record in result:
        print(f"Document: {record['Document']}")

    # Sample query augmentation
    original_query = "charging issues"
    augmented_query = augment_query('Model X', original_query)
    print(f"Augmented Query: {augmented_query}")

    another_query = "recent trends in renewable energy"
    print(f"another_query: {another_query}")
    # Execute query planning
    detailed_response = plan_query(another_query)
    print(detailed_response)


def neo4j_remote():
    print("demo neo4j...")
    url = os.getenv("remote_neo4j_url")
    username = os.getenv("remote_neo4j_username")
    password = os.getenv("remote_neo4j_password")

    graph = Neo4jGraph(
        url=url,
        username=username,
        password=password
    )
    data_url = "https://gist.githubusercontent.com/tomasonjo/08dc8ba0e19d592c4c3cde40dd6abcc3/raw/da8882249af3e819a80debf3160ebbb3513ee962/microservices.json"
    import_query = requests.get(data_url).json()['query']
    graph.query(import_query)

    vector_index = Neo4jVector.from_existing_graph(
        OpenAIEmbeddings(),
        url=url,
        username=username,
        password=password,
        index_name='tasks',
        node_label="Task",
        text_node_properties=['name', 'description', 'status'],
        embedding_node_property='embedding',
    )
    query = "How will RecommendationService be updated?"
    print(f"query is {query}")
    response = vector_index.similarity_search(query)
    for result in response:
        print(result.page_content)
    #print(response[0].page_content)
    # name: BugFix
    # description: Add a new feature to RecommendationService to provide ...
    # status: In Progress
    vector_qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(),
        chain_type="stuff",
        retriever=vector_index.as_retriever()
    )
    query = "How will recommendation service be updated?"
    print(f"query is {query}")
    response = vector_qa.invoke(query)
    print(response)
    query = "How many open tickets are there?"
    print(f"query is {query}")

    response = vector_qa.invoke(query)
    print(response)
    query = "MATCH (t:Task {status:'Open'}) RETURN count(*)"
    print(f"query is {query}")
    graph.query(query)
    graph.refresh_schema()

    cypher_chain = GraphCypherQAChain.from_llm(
        cypher_llm=ChatOpenAI(temperature=0, model_name='gpt-4'),
        qa_llm=ChatOpenAI(temperature=0), graph=graph, verbose=True,
    )
    query = "How many open tickets there are?"
    print(f"query is {query}")
    response = cypher_chain.invoke(query)
    print(response)
    query = "Which team has the most open tasks?"
    print(f"query is {query}")
    response = cypher_chain.invoke(query)
    print(response)
    query = "Which services depend on Database directly?"
    print(f"query is {query}")
    response = cypher_chain.invoke(query)
    print(response)
    query = "Which services depend on Database indirectly?"
    print(f"query is {query}")
    response = cypher_chain.invoke(query)
    print(response)
    tools = [
        Tool(
            name="Tasks",
            func=vector_qa.run,
            description="""Useful when you need to answer questions about descriptions of tasks.
            Not useful for counting the number of tasks.
            Use full question as input.
            """,
        ),
        Tool(
            name="Graph",
            func=cypher_chain.run,
            description="""Useful when you need to answer questions about microservices,
            their dependencies or assigned people. Also useful for any sort of 
            aggregation like counting the number of tasks, etc.
            Use full question as input.
            """,
        ),
    ]
    # Crear un ChatPromptTemplate
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Use the provided tools to answer the user's questions."),
        ("user", "{input}"),
        ("assistant", "{agent_scratchpad}")
    ])
    # Inicializar el modelo LLM correctamente
    llm = ChatOpenAI(temperature=0, model_name='gpt-4')
    """
    # Crear el agente usando el nuevo método
    mrkl = create_openai_functions_agent(
        tools=tools,
        llm=llm,
        prompt=prompt_template
    )

    """
    mrkl = initialize_agent(
        tools,
        llm,
        agent=AgentType.OPENAI_FUNCTIONS, verbose=True
    )

    query = "Which team is assigned to maintain PaymentService?"
    print(f"query is {query}")
    response = mrkl.invoke(query)
    print(response)
    query = "Which tasks have optimization in their description?"
    print(f"query is {query}")
    response = mrkl.invoke(query)
    print(response)


if __name__ == "__main__":
    '''
    la funcion local está basada en 
    https://sunila-gollapudi.medium.com/using-knowledge-graphs-to-enhance-retrieval-augmented-generation-rag-systems-14197efc1bab
    '''
    neo4j_local()
    neo4j_remote()
    print("Done")

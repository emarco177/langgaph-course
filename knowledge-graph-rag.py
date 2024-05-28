# Python code to demonstrate the creation of a document hierarchy in a knowledge graph for legal documents
from py2neo import Graph, Node, Relationship
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()

def update_vectorDB():
    # Inicializa Pinecone
    pc = Pinecone()
    index_name = "my-index"
    try:
        index = pc.Index(index_name)
        update_pinecone_index(index)
    except Exception as e:
        print(e)
        create_pinecone_index(index_name, pc)
        index = pc.Index(index_name)
        update_pinecone_index(index)
    print("Index updated")

def update_pinecone_index(index):
    # Lee los nodos del archivo CSV
    with open('nodes.csv', 'r') as file:
        for line in file:
            node_data = line.strip().split(',')
            node_id = node_data[0]
            node_vector = [float(x) for x in node_data[1:]]
            node_metadata = {
                "type": "node",
                "label": node_data[0]  # Asume que la etiqueta del nodo está en la primera columna
            }
            index.upsert([(node_id, node_vector, node_metadata)])
    # Lee las relaciones del archivo CSV
    with open('relationships.csv', 'r') as file:
        for line in file:
            rel_data = line.strip().split(',')
            source_id = rel_data[0]
            target_id = rel_data[1]
            rel_vector = [float(x) for x in rel_data[2:]]
            rel_metadata = {
                "type": "relationship",
                "source": source_id,
                "target": target_id,
                "label": rel_data[2]  # Asume que la etiqueta de la relación está en la tercera columna
            }
            index.upsert([(source_id + "-" + target_id, rel_vector, rel_metadata)])

def create_pinecone_index(index_name, pc):

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
        f.write("id,label")
        for node in nodes:
            node_data = node["n"]
            node_id = str(node_data.identity)
            node_label = node_data.labels
            f.write(f"\n{node_id},{node_label}")

    # Exportar relaciones
    rels = graph.run("MATCH ()-[r]->() RETURN r").data()
    with open(f"{output_dir}/relationships.csv", "w", encoding="utf-8") as f:
        f.write("source,target,type")
        for rel in rels:
            rel_data = rel["r"]
            source_id = str(rel_data.start_node.identity)
            target_id = str(rel_data.end_node.identity)
            rel_type = rel_data.type
            f.write(f"\n{source_id},{target_id},{rel_type}")

def main():
    # Connect to a Neo4j database
    graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

    # Create nodes
    tort_law = Node("Law", name="Tort Law")
    civil_rights = Node("Law", name="Civil Rights Law")
    case_study = Node("Document", name="Case Study on Civil Rights")

    # Create relationships
    graph.create(Relationship(tort_law, "RELATED_TO", civil_rights))
    graph.create(Relationship(civil_rights, "HAS_DOCUMENT", case_study))

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

    # Exportar el grafo a CSV
    export_graph_to_csv(graph, "./")
    update_vectorDB()


if __name__ == "__main__":
    main()
    print("Done")

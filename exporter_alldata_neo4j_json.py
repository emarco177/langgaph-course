from neo4j import GraphDatabase
import requests
import json


class Neo4jExporter:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def export_all_data_to_json(self):
        with self.driver.session() as session:
            result = session.run(
                "CALL apoc.export.json.all(null, {useTypes: true, stream: true})"
            )
            data = [record["data"] for record in result]
            return data


if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    user = "neo4j"
    password = "password"

    exporter = Neo4jExporter(uri, user, password)
    exported_data = exporter.export_all_data_to_json()
    exporter.close()

    # Guardar los datos exportados en un archivo JSON local
    with open("all_data.json", "w") as file:
        json.dump(exported_data, file, indent=4)
    print("Exported data to all_data.json")

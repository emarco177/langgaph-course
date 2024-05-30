from neo4j import GraphDatabase


def main():
    # URI examples: "neo4j://localhost", "neo4j+s://xxx.databases.neo4j.io"
    URI = "neo4j://localhost:7687"
    AUTH = ("neo4j", "password")

    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()


if __name__ == "__main__":
    main()
    print("Done")

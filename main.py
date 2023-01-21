from neo4j import GraphDatabase
class Neo4jConnection:

    def __init__(self,
                uri="bolt://localhost:7687",
                user="neo4j",
                pwd="password"):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db="neo4j"):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = []
        query = query.strip()
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response


check_csv = '''WITH 'https://raw.githubusercontent.com/umbrae/reddit-top-2.5-million/master/data/CatGifs.csv' as url
                LOAD CSV WITH HEADERS FROM url AS row
                RETURN count(*);
            '''

load_csv = '''WITH 'https://raw.githubusercontent.com/umbrae/reddit-top-2.5-million/master/data/memes.csv' as url
                LOAD CSV WITH HEADERS FROM url AS row
                WITH row LIMIT 10000
                CREATE (m:Meme) SET m=row
            '''

get_some_memes = '''MATCH (m:Meme) return m limit 25;'''


import networkx as nx
import matplotlib.pyplot as plt

conn = Neo4jConnection("bolt://localhost:7687", user="neo4j", pwd="password")
# Connect to the Neo4j database
print("connected")

# Run Cypher query to retrieve data from Neo4j
query = "MATCH (m:Meme)-[r:HAS]->(w:Word) RETURN m,r,w LIMIT 510"
results = conn.query(query=query)

print(len(results))
# Create a NetworkX graph object
G = nx.Graph()

# Add the nodes and edges to the graph
for result in results:
    n = result["m"]
    r = result["r"]
    m = result["w"]
    G.add_node(n["id"])
    G.add_node(m["text"])
    G.add_edge(n["title"], m["text"])

nodes = G.nodes
edges = [G.edges(x) for x in nodes]
node_wts = [len(x)*50 for x in edges]
color_map = ['red', 'blue'] * (len(nodes)//2)

# Draw the graph
nx.draw(G, with_labels=True, node_size=node_wts, node_color=color_map, font_size=5)

# Show the plot
plt.show()

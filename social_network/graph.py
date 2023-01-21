import networkx as nx
import matplotlib.pyplot as plt
from py2neo import Graph

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Cypher query to retrieve all nodes and relationships
query = '''
MATCH (p:Person)-[r:FRIEND|KNOWS_INDIRECTLY]->(p2:Person)
RETURN p,r,p2
LIMIT 20
'''

query1 = '''
MATCH (p:Person)-[r:FRIEND]->(p2:Person)
RETURN p,r,p2
'''

query2 = '''
MATCH (p:Person)-[r:KNOWS_INDIRECTLY]->(p2:Person)
RETURN p,r,p2
'''

results = graph.run(query2).data()

# Create a NetworkX graph
G = nx.Graph()

# Add nodes and edges to the graph
for result in results:
    p = result["p"]
    r = result["r"]
    p2 = result["p2"]
    G.add_node(p["name"])
    G.add_node(p2["name"])
    G.add_edge(p["name"], p2["name"], relationship=r["type"])

# Draw the graph
nx.draw(G, with_labels=True)

# Show the plot
plt.show()

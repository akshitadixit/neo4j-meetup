from py2neo import Graph, Node, Relationship
import pandas as pd

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Load the data from the CSV file into a Pandas dataframe
df = pd.read_csv("social_network.csv")

# Iterate through the rows of the dataframe
for i, row in df.iterrows():
    # Create the nodes for the current row
    person_node = Node("Person", name=row["Person"])
    person_node.__primarykey__ = "name"
    person_node.__primarylabel__ = "name"
    friend_node = Node("Person", name=row["Friend"])
    friend_node.__primarykey__ = "name"
    friend_node.__primarylabel__ = "name"
    # Create the relationship between the nodes
    friendship = Relationship(person_node, "FRIEND", friend_node)
    # Merge the nodes and relationships into the Neo4j database
    graph.merge(friendship)

print("Data loaded successfully!")


# --------------------------------------


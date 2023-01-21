'''Once you have generated a "covid contact tracing" network database as a dataframe,
   you can use Python to load the data into a Neo4j graph database.
   Here is an example of how you can use the pandas library to read the dataframe
   and the py2neo library to load the data into Neo4j:
'''
from py2neo import Graph, Node, Relationship
import pandas as pd

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))
df = pd.DataFrame()

# Iterate through the rows of the dataframe
for i, row in df.iterrows():
    # Create the nodes for the current row
    Human_node = Node("Human", name=row["Human"])
    Human_node.__primarykey__ = "name"
    Human_node.__primarylabel__ = "name"
    location_node = Node("Location", name=row["Location"])
    location_node.__primarykey__ = "name"
    location_node.__primarylabel__ = "name"
    # Create the relationship between the nodes
    relation = Relationship(Human_node, "VISITED", location_node)
    relation["weight"] = row["Weight"]
    # Merge the nodes and relationships into the Neo4j database
    graph.merge(relation)

print("Data loaded successfully!")

'''This code reads the data from the dataframe and then iterates over the rows of the dataframe,
   creating nodes for each Human and location and relationships between them
   based on the edges stored in the dataframe.
   Then it uses py2neo's merge function to merge the nodes and relationships into the Neo4j database.
'''

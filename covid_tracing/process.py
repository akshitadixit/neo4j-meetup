'''You can use Cypher queries to create relationships between people
   based on common locations they have visited.
   Here is an example of how you can do this using the py2neo library in Python:
'''
from py2neo import Graph

# Connect to the Neo4j database
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Cypher query to find all pairs of people who have visited the same location
query = '''
MATCH (p1:Human)-[r:VISITED]->(l:Location)<-[r2:VISITED]-(p2:Human)
WHERE p1 <> p2
WITH p1,p2, count(l) as common_locations
MERGE (p1)-[:IN_CONTACT {weight: 1/common_locations}]->(p2)
'''

graph.run(query)

print("'IN_CONTACT' relationships established!")

'''This Cypher query matches all pairs of people p1 and p2 who have visited the same location l.
   The WHERE clause ensures that p1 and p2 are not the same Human.
   It uses the count(l) to count the number of common locations visited by p1 and p2.
   Then it uses the MERGE clause to create the "IN_CONTACT" relationship between p1 and p2
   with the weight of the relationship set to the reciprocal of the number of common locations visited.
   This way, if two people have visited more common locations,
   the edge weight between them will be smaller, representing a higher chance of them being in contact.
   It's worth noting that this Cypher query creates new relationships, it doesn't change the existing ones.
'''

'''Python code that can be used to randomly generate a "covid contact tracing" network database
   of 100 random people, where each person has a list of visited locations
   if two people visited the same location, they are connected with an edge,
   if they visited multiple same locations, the edge length between them is decreased:
'''
import random
import pandas as pd

# Set the number of people in the network
num_people = 100

# Create a list of names
names = ["Human " + str(i) for i in range(num_people)]

# Create a list of locations
locations = ["Location " + str(i) for i in range(10)]

# Create a dictionary to store the edges
edges = {}

for i in range(num_people):
    # Set the number of visited locations for the current person
    num_locations = random.randint(1, 5)
    # Choose a random set of visited locations for the current person
    person_locations = random.sample(locations, num_locations)
    for location in person_locations:
        for j in range(i+1, num_people):
            if location in person_locations:
                if (i, j) in edges:
                    edges[(i, j)] -= 1
                else:
                    edges[(i, j)] = -1

# Create a pandas dataframe from the edges
df = pd.DataFrame(list(edges.items()), columns=["Human_Location", "Weight"])

# Split the column into two columns
df[["Human", "Location"]] = df["Human_Location"].apply(pd.Series)

print("Data created successfully!!")

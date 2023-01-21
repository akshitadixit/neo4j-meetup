import random
import pandas as pd

# Set the number of people in the network
num_people = 100

# Create a list of names
names = ["Person " + str(i) for i in range(num_people)]

# Create a list of edges
edges = []
for i in range(num_people):
    # Set the number of friends for the current person
    num_friends = random.randint(1, 10)
    # Choose a random set of friends for the current person
    friends = random.sample(range(num_people), num_friends)
    # Add edges to the list of edges
    for friend in friends:
        edges.append((i, friend))

# Create a pandas dataframe from the edges
df = pd.DataFrame(edges, columns=["Person", "Friend"])

# Add the names to the dataframe
df["Person"] = df["Person"].apply(lambda x: names[x])
df["Friend"] = df["Friend"].apply(lambda x: names[x])

# Export the dataframe to a CSV file
df.to_csv("social_network.csv", index=False)

print("Social network generated successfully!")

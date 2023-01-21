# Neo4j Meetup Demo

## Pre-requisites

* Ensure you have Neo4j installed, if not follow the step in the link here to get it up and running:
[Install Neo4j](https://neo4j.com/docs/operations-manual/current/installation/windows/)
* Open up a terminal/cmdline window and shoot the following commands:
> export NEO4J_HOME="/Users/akshitadixit/neo4j"
> alias neo4j="$NEO4J_HOME/bin/neo4j"

(change the path of NEO4J_HOME to your installation folder's root)

* Now start the database server:
> neo4j console

* Visit `http://localhost:7474/` to access neo4j browser console and login to neo4j db using default auth(uname="neo4j", pwd="neo4j", it will prompt you to change password on the first login)

## Setting up

`git clone `

Move into the cloned folder. (optional: create a new conda environment to run this)

`pip install -r requirements.txt`

`python filename.py`

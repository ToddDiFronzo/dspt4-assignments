
# app/mongo_inserts.py



# client = pymongo.MongoClient("mongodb+srv://cardstud:hacine44@cluster0-uaqri.mongodb.net/test?retryWrites=true&w=majority")
# db = client.test


#app/mongo_queries.py

import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

connection_uri = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_uri)

client = pymongo.MongoClient(connection_uri)
print("----------------")
print("CLIENT:", type(client), client)

db = client.todd_database # "test_database" or whatever you want to call it
print("----------------")
print("DB:", type(db), db)

collection = db.pokemon_test # "pokemon_test" or whatever you want to call it
print("----------------")
print("COLLECTION:", type(collection), collection)

print("----------------")
print("COLLECTIONS:")
print(db.list_collection_names())  # shows a list of tables ("collections")

collection.insert_one({
    "name": "Pikachu",
    "level": 30,
    "exp": 76000000000,
    "hp": 400,
})                      # inserts a record("document") into our collection
print("DOCS:", collection.count_documents({}))   # similar to count(distinct ___ as row_count FROM my_table
print(collection.count_documents({"name": "Pikachu"}))  # similar to a where clause:  SELECT count(distinct ____ ) as row_count FROM my_table WHERE name = kk

# results = list(collection.find({"hello":"world"}))
# results1 = list(collection.find({"name":"Pikachu"}))
# print(results)
# print(results1)

# query the collection, get results, then loop through the results
# pikas = list(collection.find({"name":"Pikachu"}))
# for pika in pikas:
#     print(pika["name"])


# insert multiple documents at the same time?

tyranitar = {
    "name": "Tyranitar",
    "level": 77,
    "exp": 4814819,
    "hp": 264,
    "defense":198,
    "attack": 235
}

psyduck = {
    "name": "Psyduck",
    "level": 20,
    "exp": 23000000,
    "hp": 100,
}

pelipper = {
    "name": "Pelipper",
    "level": 100,
    "exp": 1000000,
    "atk": 122,
    "def": 328,
    "spa": 226,
    "spd": 177,
    "spe": 166,
    "nature": "Bold",
    "ability": "Drizzle",
    "held_item": "Damp Rock",
    "move1": "U-turn",
    "move2": "Scald",
    "move3": "Roost",
    "move4": "Hurricane",
    "hpev": 252,
    "defev": 252,
    "spdev": 6,
    "hpiv": 31,
    "atkiv": 31,
    "defiv": 21,
    "spaiv": 31,
    "sdpiv": 31,
    "speiv":31,
}

never = {
    "name": "NEVER played this game",
    "level": -500,
    "exp": -10000000000009,
    "hp": "a string here, not an int",
}

mewtwo = {
    "name": "Mewtwo",
    "level": 90,
    "exp": 23000000,
    "hp": 100,
}

mew = {
    "name": "Mew",
    "lvl": 22,
    "exp": 63000000,
    "hp": 600,
}

team = [tyranitar, psyduck, pelipper, never, mewtwo, mew]
collection.insert_many(team)
print("DOCS:", collection.count_documents({}))  

# query 1
high_levels = list(collection.find({"level":{"$gte":20}}))
for doc in high_levels:
    print(doc["name"])
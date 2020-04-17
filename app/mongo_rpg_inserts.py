
# app/mongo_rpg_inserts.py

import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values	# so we can insert multiple rows at once
import json					# might need to do some json conversions
import pandas as pd
import sqlite3
import pymongo
from dotenv import load_dotenv

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
curs = conn.cursor()

# How many characters are there?
query_q1 = "SELECT count(character_id) FROM charactercreator_character"; 
results1 = curs.execute(query_q1).fetchall()
print(results1)

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
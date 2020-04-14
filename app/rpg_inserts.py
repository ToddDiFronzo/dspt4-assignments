import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values	# so we can insert multiple rows at once
import json					# might need to do some json conversions
import pandas as pd
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
curs = conn.cursor()

# How many characters are there?
query_q1 = "SELECT * FROM titanic; 
results1 = curs.execute(query_q1).fetchall()
#WHERE EMPLOYEE.SSN =CAST(PROSPECT.SSN AS INTEGER) 


load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))


insertion_query = "INSERT INTO titanic(item_id, name, value, weight) VALUES %s"
execute_values(cursor, insertion_query, results1)

# make sure we are committing the data

connection.commit()

cursor.close()
connection.close()
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values	# so we can insert multiple rows at once
import json					# might need to do some json conversions
import pandas as pd

load_dotenv()

DB_HOST = os.getenv("DB_HOST", default="OOPS")
DB_NAME = os.getenv("DB_NAME", default="OOPS")
DB_USER = os.getenv("DB_USER", default="OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="OOPS")

connection = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print("CONNECTION", type(connection))

cursor = connection.cursor()
print("CURSOR", type(cursor))

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }

# insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
# execute_values(cursor, insertion_query, [
#     ('A rowwwww', 'null'),
#     ('Another row, with JSONNNNN', json.dumps(my_dict)),
#     ('Third row', "3")
# ])

insertion_query = "INSERT INTO test_table (name, data) VALUES %s"
execute_values(cursor, insertion_query, [
    ('A rowwwww', 'null'),
    ('Another row, with JSONNNNN', json.dumps(my_dict)),
    ('Third row', "3")
])

# make sure we are committing the data

connection.commit()

cursor.close()
connection.close()

import os
import pandas as pd 
import os
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import execute_values	# so we can insert multiple rows at once
import numpy as np 

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs) # so can convert the csv to list of tuples

load_dotenv()   # loads contents of the .env file into the script's environment

DB_NAME = os.getenv("DB_NAME")					
DB_USER = os.getenv("DB_USER")			
DB_PASSWORD = os.getenv("DB_PASSWORD")		
DB_HOST = os.getenv("DB_HOST")

#
# READ CSV
# 

# if your CSV file is in the 'data' directory:
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "titanic.csv")
df = pd.read_csv(CSV_FILEPATH)
df.index += 1
print(df.head())

# CONNECT TO PG db via tableplus

connection = psycopg2.connect(host=DB_HOST, dbname = DB_NAME, user=DB_USER, password=DB_PASSWORD)
print(type(connection)) #> <class 'psycopg2.extensions.connection'>

cursor = connection.cursor()
print(type(cursor))    # > <class 'psycopg2.extensions.cursor'>

# commented this part out, just used to see if we had a connection:
# query = "SELECT * from titanic_1"
# cursor.execute(query)
# results = cursor.fetchall()
# print(type(results))
# print(results) 

#
# CREATE TABLE
#

table_creation_query = """
CREATE TABLE IF NOT EXISTS passengers(
    Id SERIAL,
    Survived integer,
    Pclass int,
    Name varchar(55),
    sex varchar(10),
    age int,
    Siblings_Spouse_Aboard int,
    Parents_Children_Aboard int,
    Fare float
);
"""
cursor.execute(table_creation_query)

#
# INSERT DATA INTO THE TABLE
#
# df.to_records(index=False)
# x = list(df.to_records(index=False))
# type(x)
# type(x[0])

list_of_tuples = list(df.to_records(index=True))

insertion_query = "INSERT INTO passengers (id, survived, pclass, name, sex, age, siblings_spouse_aboard, parents_children_aboard, fare) VALUES %s"
execute_values(cursor, insertion_query,list_of_tuples)




# to commit and save our changes
connection.commit()

cursor.close()
connection.close()
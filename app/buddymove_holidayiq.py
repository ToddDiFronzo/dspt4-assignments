
import pandas as pd
import sqlite3 

# dataset_url = 'https://raw.githubusercontent.com/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module1-introduction-to-sql/buddymove_holidayiq.csv'
# df = pd.read_csv(dataset_url)
# conn = sqlite3.Connection(dataset_url)
# #print(df.head())


# df = pd.read_csv(dataset_url)
# df.to_sql('review', con=conn)

import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
#print(type(conn)) #> <class 'sqlite3.Connection'>

curs = conn.cursor()
#print(type(curs)) #> <class 'sqlite3.Cursor'>

dataset = os.path.join(os.path.dirname(__file__), "..", "data", "buddymove_holidayiq.csv")
df = pd.read_csv(dataset)
print(df.head())

#df.to_sql('review', con=conn)
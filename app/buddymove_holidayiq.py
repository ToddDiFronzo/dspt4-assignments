
import pandas as pd
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

'''
P2_Q1: Count how many rows you have - it should be 249
'''
query_1 = "SELECT count(User_Id) as total_rows FROM review"  
		
results_1 = curs.execute(query_1).fetchone()[0]
print("==========")
print("Q1. RESULTS\n The total number of rows is: ", results_1)		



'''P2_Q2: How many users who reviewed at least 100 'Nature' in the category also reviewed
	at least 100 in the 'Shopping' category?
'''
query_2 = "SELECT  count(Shopping) as total_users FROM review WHERE Nature > 99 AND Shopping > 99"

results_2 = curs.execute(query_2).fetchone()[0]
print()
print("==========")
print("Q2. RESULTS\n The total number of users who reviewed at least 100 'Nature' and at least 100 'Shopping' categories is: ", results_2)	
print()	

'''Stretch: What are the average number of reviews for each category?'''

query_stretch = '''SELECT avg(total_nature_reviews) as avg_reviews
                    FROM (
                        SELECT  count(Nature) as total_nature_reviews
		                FROM review 
	                )'''

results_3 = curs.execute(query_stretch).fetchone()[0]
print() 
print("==========")
print("Stretch RESULTS\n The average number of reviews for each category: ", results_3)	
print()	
  
	
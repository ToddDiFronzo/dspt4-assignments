# ap_queries.py

import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "data", "rpg_db.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row
print(type(conn)) #> <class 'sqlite3.Connection'>

curs = conn.cursor()
print(type(curs)) #> <class 'sqlite3.Cursor'>

# How many characters are there?
query_q1 = "SELECT count(character_id) FROM charactercreator_character"

#for row in curs.execute(query):
    #print('There are a total of', row[1], 'Characters')
results1 = curs.execute(query_q1).fetchone()[0]
print() 
print("===============")
print("Q1. RESULTS\n--> The total number of characters are: ", results1)
print() 

# How many of each specific subclass
query_q2 = '''
SELECT ccc.character_id as character 
		 ,count(distinct c.character_ptr_id) as total_clerics
		,count(distinct f.character_ptr_id) as total_fighters
		,count(distinct m.character_ptr_id) as total_mages
		,count(distinct n.mage_ptr_id) as total_necromancers
		,count(distinct t.character_ptr_id) as total_thieves
FROM charactercreator_character ccc 
LEFT JOIN charactercreator_fighter f  
	ON character = f.character_ptr_id
LEFT JOIN charactercreator_cleric c 
	ON character = c.character_ptr_id
LEFT JOIN charactercreator_mage m 
	ON character =  m.character_ptr_id
LEFT JOIN charactercreator_necromancer n 
	ON character = n.mage_ptr_id
LEFT JOIN charactercreator_thief t 
	ON character = t.character_ptr_id
'''
results2 = list(curs.execute(query_q2).fetchall())
print("==========")
print("Q2. RESULTS")
for i in results2:
    print()
    print(f' Total clerics: ({i[0]})\n Total fighters: ({i[1]})\n Total mages:({i[2]})\n Total necromancers: ({i[3]})\n Total thieves: ({i[4]})')
    print()

# How many total items
query_q3 = '''SELECT item_id
	,count(distinct item_id) as total_items
FROM charactercreator_character_inventory
'''
results3 = curs.execute(query_q3).fetchone()[1]
print("==========")
print("Q3. RESULTS\n-->The total number of items is: ", results3)
print()

# How many of the total items are weapons
query_q4a = '''SELECT item_id ,count(distinct item_id) as total_items ,count(distinct w.item_ptr_id) as total_weapons
FROM armory_item i 
LEFT JOIN armory_weapon w 
ON w.item_ptr_id = i.item_id'''

results4a = curs.execute(query_q4a).fetchone()[2]
print("==========")
print("Q4a. RESULTS\n-->The total number of items that are weapons is: ", results4a)
print()

# How many of the total items are not weapons
query_q4b = ''' 
SELECT item_id
	,count(distinct item_id) as total_items
	,count(distinct w.item_ptr_id) as total_weapons
	,count(distinct item_id) - count(distinct w.item_ptr_id) as not_weapons
FROM armory_item i 
LEFT JOIN armory_weapon w 
	ON w.item_ptr_id = i.item_id'''

results4b = curs.execute(query_q4b).fetchone()[3]
print("==========")
print("Q4b. RESULTS\n-->The total number of items that are not weapons is: ", results4b)
print()

# How many items does each character have? Return first 20 rows
query_q5 = ''' SELECT 
	ccc.character_id
	,ccc.name  
	, count(distinct ci.item_id) as total_items
FROM charactercreator_character_inventory ci 
LEFT JOIN charactercreator_character ccc 
	ON ccc.character_id = ci.character_id
GROUP BY ccc.character_id
LIMIT 20 '''

results5 = list(curs.execute(query_q5).fetchall())
print("Q5. RESULTS")
print("==========")
for i in results5:
    print()
    print(f' Character_id: ({i[0]}), named ({i[1]}), has ({i[2]} items).')
print()

#How many Weapons does each character have? (Return first 20 rows)
query_q6 = ''' SELECT 
	ccc.character_id
	,ccc.name  
	,count(distinct ci.item_id) as total_items
	,count(distinct aw.item_ptr_id) as total_weapons
FROM charactercreator_character_inventory ci 
LEFT JOIN charactercreator_character ccc 
	ON ccc.character_id = ci.character_id
LEFT JOIN armory_item ai 
	ON ai.item_id = ci.item_id
LEFT JOIN armory_weapon aw 
	ON aw.item_ptr_id = ai.item_id
GROUP BY ccc.character_id
LIMIT 20 '''

results6 = list(curs.execute(query_q6).fetchall())
print("Q6. RESULTS")
print("==========")
for i in results6:
    print()
    print(f' Character_id ({i[0]}), named ({i[1]}), has ({i[3]}) weapons out of his/her ({i[2]}) items).')
print()
# On average, how many Weapons does each character have
query_q7 = '''SELECT avg(total_items) as avg_items
FROM (

	SELECT 
		ccc.character_id
		,ccc.name  
		, count(distinct ci.item_id) as total_items
		,count(distinct aw.item_ptr_id) as total_weapons
	FROM charactercreator_character_inventory ci 
	LEFT JOIN charactercreator_character ccc 
		ON ccc.character_id = ci.character_id
	LEFT JOIN armory_item ai 
		ON ai.item_id = ci.item_id
	LEFT JOIN armory_weapon aw 
		ON aw.item_ptr_id = ai.item_id
	GROUP BY ccc.character_id
) subz'''
results7 = curs.execute(query_q7).fetchone()[::]
print("==========")
print("Q7. RESULTS\n-->The average number of items each character has is: ", results7)

# On average, how many Weapons does each character have
query_q8 = '''
SELECT avg(total_weapons) as avg_weapons
FROM (

	SELECT 
		ccc.character_id
		,ccc.name  
		, count(distinct ci.item_id) as total_items
		,count(distinct aw.item_ptr_id) as total_weapons
	FROM charactercreator_character_inventory ci 
	LEFT JOIN charactercreator_character ccc 
		ON ccc.character_id = ci.character_id
	LEFT JOIN armory_item ai 
		ON ai.item_id = ci.item_id
	LEFT JOIN armory_weapon aw 
		ON aw.item_ptr_id = ai.item_id
	GROUP BY ccc.character_id
) subz'''
results8 = curs.execute(query_q8).fetchone()[::]
print("==========")
print("Q8. RESULTS\n--> The average number of weapons each character has is: ", results8)
print() 
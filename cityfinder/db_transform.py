# Database Transformations
# 2-10-2016
# This file contains corrections for the sql database.

import sqlite3

def walk_relation_clean(cursor):
	'''
	Creates a new uid for each unique city in the walk csv.
	'''
	cursor.execute('DELETE FROM walk WHERE CITY IS NULL OR trim(CITY) = ""')
	cursor.execute('SELECT CITY FROM walk')

	cities = {}
	uid = 0
	for row in cursor:
		cities[row[0]] = uid
		uid += 1

	for city in cities: 
		uid = cities[city]
		cursor.execute('UPDATE walk SET uid = ? WHERE CITY = ?', [uid, city])

	cursor.execute('')

	return cities

def add_uid_to_relation(cursor, cities, relation):
	'''
	Cleans up weather file and adds uid for city based on cities dictionary.
	'''
	cursor.execute('DELETE FROM ? WHERE CITY = "city"', [relation])
	cursor.execute('ALTER TABLE ? ADD COLUMN uid int', [relation])

	for city in cities:
		uid = cities[city]
		name = city.split()
		if '-' in city: 
			name = city.split('-')
		if len(name) > 2:
			if 'St.' not in name[1]:
				query = '%' + name[1] + '%'
			else: 
				query = '%' + name[2] + '%'
		else: 
			query = '%' + name[0] + '%'
		cursor.execute('UPDATE ? SET uid = ? WHERE CITY LIKE ?', [relation, uid, query])

	connection.commit()
	cursor.close()

def go(dbfilename):
	'''
	Runs full file
	'''
	connection = sqlite3.connect(dbfilename)
	cursor = connection.cursor()

	cities = walk_file_clean(cursor)
	add_uid_to_relation(cursor, cities)

	connection.commit()
	cursor.close()
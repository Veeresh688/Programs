# Python program to get data from mysql database.

import mysql.connector

connection = mysql.connector.connect(host = '138.68.140.83', user = 'veeresh', password = 'Veeresh@123', database = 'dbVeeresh')
cursor = connection.cursor()

dataTableFields = None

def getFieldValues():
	global dataTableFields
	cursor.execute("SHOW COLUMNS FROM item")
	headers = cursor.fetchall()
	dataTableFields = [header[0] for header in headers]

def readItems():
	query = "select * from item"
	cursor.execute(query)
	rows = cursor.fetchall()
	for row in rows:
		print()
		for indexCounter in range(len(dataTableFields)):
			print(dataTableFields[indexCounter] + ":",row[indexCounter])		

getFieldValues()
readItems()
cursor.close()
connection.close()
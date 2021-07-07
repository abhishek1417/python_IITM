#Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL Table after which you Fetch and Display data #from Table

import mysql.connector

mydb=mysql.connector.connect(
	host="localhost",
    user="root",
    password="Abhi@1234",
    database="sakila"
)
mycursor= mydb.cursor()

mycursor.execute(INSERT INTO actor(id,name) VALUES(01, 'John'))
mycursor.commit()
myresult=mycursor.fatchall()
for i in myresult:
	print(x)
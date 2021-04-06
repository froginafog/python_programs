import mysql.connector

#this is the connection to mysql database (db)
mydb = mysql.connector.connect(host="localhost",
                               user="myusername", #mysql username
                               password="mypassword" #mysql password
                              )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase;")

print("Query Success");

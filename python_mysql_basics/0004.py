import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

sql = "SHOW TABLES;"

mycursor.execute(sql)

for x in mycursor:
  print(x) 

print("Query Success");

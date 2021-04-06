import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword"
                              )

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for row in mycursor:  
    print(row) 

print("Query Success");

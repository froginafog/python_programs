import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )
mycursor = mydb.cursor()

sql = "SELECT * FROM students"

mycursor.execute(sql)

result = mycursor.fetchall()

for row in result:
    print(row)


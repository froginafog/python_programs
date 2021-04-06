import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

#sql = "UPDATE table_name SET column_name = 'new_value' WHERE last_name = 'old_value'"
sql = "UPDATE students SET last_name = 'The Tiny' WHERE last_name = 'The Mighty'"

print("sql:", sql)

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "rows(s) were updated")

print("sql:", sql)

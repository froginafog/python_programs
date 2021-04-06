import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

#sql = "DELETE FROM table_name WHERE column_name = 'value'"
sql = "DELETE FROM students WHERE last_name = 'The Timely'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "rows(s) were deleted")

print("sql:", sql)

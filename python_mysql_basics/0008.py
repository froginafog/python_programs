import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

sql = "SELECT * FROM " + "students" \
      + " WHERE " + "last_name = 'The Timely'" \
      + " OR " + "last_name = 'The Hood'" 
      
mycursor.execute(sql)

result = mycursor.fetchall()

num_rows = len(result)

for i in range(0, num_rows):
    num_columns = len(result[i])
    print('|', end = '')
    for j in range(0, num_columns):
        if(j == 0):
            print("|%-5s|" %result[i][j], end = '');
        else:
            print("|%-30s|" %result[i][j], end = '');
    print("|\n");

print("sql:", sql)
print("Query Success")

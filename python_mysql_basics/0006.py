import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

sql = "INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)"

values = [['Andy', 'The Candy', 'AndyTheCandy@coolmail.com'],
          ['Tom', 'The Timely', 'TomTheTimely@coolmail.com'],
          ['Eve', 'The Sleepy', 'EveTheSleepy@coolmail.com']
         ]

num_values = len(values);
for i in range(0, num_values):
    mycursor.execute(sql, values[i])

mydb.commit()
#this is required otherwise no change will be applied to the table
#this means that if we don't include this line, the data will be not inserted into the table

print("Query Success");

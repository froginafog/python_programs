import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

sql = ["""INSERT INTO students (first_name, last_name, email)
          VALUES ('Bob', 'The Great', 'BobTheGreat@coolmail.com'); """,
       """INSERT INTO students (first_name, last_name, email)
               VALUES ('Robin', 'The Hood', 'RobinTheHood@coolmail.com'); """,
       """INSERT INTO students (first_name, last_name, email)
               VALUES ('Mimi', 'The Mighty', 'MimiTheMighty@coolmail.com'); """
      ]

num_queries = len(sql);
for i in range(0, num_queries):
    mycursor.execute(sql[i])

mydb.commit()
#this is required otherwise no change will be applied to the table
#this means that if we don't include this line, the data will be not inserted into the table

print("Query Success");

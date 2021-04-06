import mysql.connector

mydb = mysql.connector.connect(host="localhost",
                               user="myusername",
                               password="mypassword",
                               database="mydatabase"
                              )

mycursor = mydb.cursor()

sql = """CREATE TABLE students (id INT(10) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                                first_name VARCHAR(50) NOT NULL,
                                last_name VARCHAR(50) NOT NULL,
                                email VARCHAR(50),
                                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)"""

mycursor.execute(sql)

print("Query Success");

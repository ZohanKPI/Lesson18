import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="zahar4022"
# )
#
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE my_first_db")
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="zahar4022",
    database="my_first_db"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE student")

mycursor.execute("DROP TABLE employee")

mycursor.execute("CREATE TABLE student (id INT PRIMARY KEY, name VARCHAR(255))")

mycursor.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT(6))")

#mycursor.execute("ALTER TABLE student CHANGE id id2 INT PRIMARY KEY")

mycursor.execute("INSERT INTO student (id2, name) VALUES (%s, %s)", (1, "John"))

mycursor.execute("INSERT INTO employee (name, salary) VALUES (%s, %s)", ("John", 10000))

mycursor.execute("SELECT * FROM student")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
    
mycursor.close()
mydb.close()
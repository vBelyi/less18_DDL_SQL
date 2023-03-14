import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv('MY_FIRST_DB_PASSWORD')

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password=password,
    auth_plugin='caching_sha2_password'
)

mycursor = mydb.cursor()
mycursor.execute('CREATE DATABASE my_first_db')
mycursor.execute('CREATE TABLE my_first_db.student (id INT, name VARCHAR(255))')
mycursor.execute('CREATE TABLE my_first_db.employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), salary INT (6))')
mycursor.execute('ALTER TABLE my_first_db.student MODIFY id INT PRIMARY KEY')
mycursor.execute('INSERT INTO my_first_db.student (id, name) VALUES (01, "john")')
mycursor.execute('INSERT INTO my_first_db.employee (id, name, salary) VALUES (01, "john", 10000)')
mydb.commit()

mycursor.execute('SHOW DATABASES LIKE "my_first_db"')
myresult = mycursor.fetchall()
print(myresult)

mycursor.execute('SHOW TABLES FROM my_first_db')
myresult2 = mycursor.fetchall()
print(myresult2)

mycursor.execute('SELECT * FROM my_first_db.student')
myresult3 = mycursor.fetchall()
print(myresult3)

mycursor.execute('SELECT * FROM my_first_db.employee')
myresult4 = mycursor.fetchall()
print(myresult4)


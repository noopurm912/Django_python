import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",           #will hold the url of database in case of other database
    user = "root",
    password = "Indy@46227",
    database = "testdb"

)
my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE testdb")

#my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     #print(db)    #return the databases in tuple
#     print(db[0])

# my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(10))")
# my_cursor.execute("SHOW TABLES")
#
# for table in my_cursor:
#     print(table[0])
# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("john" , "john@gmail.com", 30)
# my_cursor.execute(sqlStuff, record1)
# mydb.commit()

# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record = [
#     ("john" , "john@gmail.com", 30),
#     ("Noopur" , "noop@gmail.com", 30),
#     ("Nitin" , "nit@gmail.com", 30),
# ]
# my_cursor.executemany(sqlStuff, record)
# mydb.commit()
# my_cursor.execute("ALTER TABLE users ADD user_id INTEGER AUTO_INCREMENT PRIMARY KEY")
# mydb.commit()


# #pull data from table

# my_cursor.execute("SELECT * FROM users")
# result = my_cursor.fetchall()
# for item in result:
#     print(item[0])

#where clause
# my_cursor.execute("SELECT * FROM users WHERE age > 20")
# result = my_cursor.fetchall()
# for item in result:
#     print(item)

#wildcard and like can work with the condition as and or
# my_cursor.execute("SELECT * FROM users WHERE name LIKE 'N%'")
# result = my_cursor.fetchall()
# for item in result:
#     print(item)

#updating records
# my_sql = "UPDATE users SET age = 41 WHERE name = 'Noopur'"
# my_cursor.execute(my_sql)
# mydb.commit()

#limiting the results and ordering results using OFFSET for ignore the first result, ORDER BY name ASC
#deleting record DELETE FROM users WHERE name = ''
#commit

# import sqlite3

# path = r"C:\Users\User\Desktop\Python Crash Course A Hands-On, Project-Based Introduction to Programming, 2nd Edition\python_sqlite3"

# try:
#     conn = sqlite3.connect(path)
#     conn.execute(
#         """
#             Create table student (
#                 st_id INT AUTO_INCREMENT PRIMARY KEY,
#                 st_name VARCHAR(50),
#                 st_class VARCHAR(10),
#                 st_email VARCHAR(30)
#             )

#     """
#     )

#     conn.close()
# except sqlite3.OperationalError:
#     print("The table is already exists.")


# 🧇🧇🧇🧇🧇 Below the is the example of raw string which do nothing when we put a small r with a string.
# print("print\t\b\n this which is not raw yet.")
# print(r"print\t\b\n this which is not raw yet.")

# Another example of raw string
# If we print the following as it is without r then it will give us the unicode error
# s = "Hello\xfrom AskPython"
# s = r"Hello\xfrom AskPython"
# print(s)

# 🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤🍤
# Creating an SQLite database from a Python program: shows you how to create a new
# SQLite database from a Python program using the sqlite3 module
# storeDB = r"C:\Users\User\Desktop\Python Crash Course A Hands-On, Project-Based Introduction to Programming, 2nd Edition\python_sqlite3\database.db"

import sqlite3


# def create_connection(db_file):
#     """create a database connection to a SQLite database"""
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#         print(sqlite3.version)
#     except Error as e:
#         print(e)
#     finally:
#         if conn:
#             conn.close()


# if __name__ == "__main__":

#     create_connection(storeDB)


# 🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖🍖
# Insert into a table
# try:
# create_db = """Create table student (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(40),
#     fname VARCHAR(40)

#     )"""

#     ins = f"""insert into student (name,fname) values('asad','sami')"""
#     connection = sqlite3.connect("sqlite.db")
#     if connection is None:
#         connection.execute(create_db)
#     connection.execute(ins)
#     connection.commit()
#     connection.close()

# except sqlite3.OperationalError as e:
#     print(e)

# 🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄🍄
# Now we will implement select query in sqlite3.
from prettytable import PrettyTable

tab = PrettyTable()

conn = sqlite3.connect("sqlite.db")

create_db = """Create table student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    fname VARCHAR(40)

    )"""

if conn is None:
    conn.execute(create_db)
    # Below in limit we have insert 1,3 (this means we leave the one entry and display the remaining upto 3 rows.)
data = conn.execute(
    """
    select * from student limit 1,3 
"""
)
print(data)  # If we print data which is a cursor object will not print the data

# Above data which is a cursor object will pointer the the single row it a time. but if you do data.fetchall that will fetch all the data inside of that table
# Now to print the data we need to loop because it contain tuple.
tab.field_names = ["ID", "NAME", "FATHER_NAME"]
for item in enumerate(data, 1):
    print(item[0], item[1][1], " : ", item[1][2])
    tab.add_row(row=[item[0], item[1][1], item[1][2]])


print(tab)

# print(data.rowcount)

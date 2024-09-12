import sqlite3

# Connect to a database
connection = sqlite3.connect('StudentsInfo.db')

# Create a cursor object to interact with the database 
cursor = connection.cursor()

# Creating a Table
cursor.execute('''CREATE TABLE Students (id INTEGER PRIMARY KEY, name TEXT, grade REAL)''')

# Inserting data
cursor.execute("INSERT INTO Students (name, grade) VALUES ('Alice', 85.5)")

# Retrieve data and fetch the data using fetchall()
cursor.execute("SELECT * FROM Students")
rows = cursor.fetchall()
for row in rows: 
    print(row)

# Commit the changes 
connection.commit()

# Closing connection from database
connection.close()

# try except for error handling
# Let the non-existing table be the "Teachersinfo"
try:
    cursor.execute("SELECT * FROM Teachersinfo") 

except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")

# Parameterized query

cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ('Bob', 92.3))
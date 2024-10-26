import time
import requests
import json
import sqlite3

connection = sqlite3.connect("db_t1.db")
cursor = connection.cursor()
# Example: Creating a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
# Insert some sample data
cursor.execute('''
    INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 24)
''')
# Commit the changes to the database
connection.commit()

# Query the data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
connection.close()
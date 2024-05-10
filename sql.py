import sqlite3

# Connect to the database

conn = sqlite3.connect('db.sqlite')

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS posts ( id INTEGER PRIMARY KEY, name TEXT, price NUMBER, description, TEXT)

''')

conn.commit()

# Insert data into the table

data_to_insert = [('This is the first post.',),
                  ('Another post for the database.',)
                  ,('One more post for the example.',)]

cursor.executemany("INSERT INTO posts (content) VALUES (?)", data_to_insert)

# Commit the changes and close the connection

conn.commit()

conn.close()
# import the sqlite3 library
import sqlite3

# create a database connection
conn = sqlite3.connect("new.db")
# create a cursor object to execute sql commands
cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO population VALUES('New York', \
	'NY', 8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco', \
	'CA', 800000)")

# commit the changes
conn.commit()

# close the database connection
conn.close()
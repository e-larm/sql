# import the sqlite3 library
import sqlite3

# create a database connection
conn = sqlite3.connect("new.db")
c= conn.cursor()

# insert multiple records using a tuple
cities = [
         ('Boston', 'MA', 600000),
         ('Chicago', 'IL', 2700000),
         ('Houston', 'TX', 2100000),
         ('Phoenix', 'AZ', 1500000)   
        ]

# insert data into table
c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)

# commit the changes
conn.commit()

# close the database connection
conn.close()
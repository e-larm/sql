# import from CSV

# import the csv library
import csv

import sqlite3

conn = sqlite3.connect("new.db")
c = conn.cursor()

# open the csv file and assign it to a variable
employees = csv.reader(open("employees.csv", "rU"))

# create a new table called employees
#c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

# Insert data into table
c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)

# commit
conn.commit()

# close the database connection
conn.close()

#!/usr/bin/python3
""" Module for slecting rows in db
"""
import MySQLdb
import sys
username = sys.argv[1]
password = sys.argv[2]
dbname = sys.argv[3]
db = MySQLdb.connect(user=username,
                     passwd=password,
                     db=dbname,
                     host="localhost",
                     port=3306)
cursor = db.cursor()
cursor.execute("""SELECT *
FROM states
ORDER BY states.id ASC""")

if __name__ == "__main__":
    for i in cursor._rows:
        print(i)

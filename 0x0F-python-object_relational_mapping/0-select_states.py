#!/usr/bin/python3
""" Module for slecting rows in db
"""
import MySQLdb
db = MySQLdb.connect(user="root",
                     passwd="Khalif01@2023",
                     db="hbtn_0e_0_usa")
cursor = db.cursor()
cursor.execute("""SELECT *
FROM states
ORDER BY states.id ASC""")

if __name__ == "__main__":
    for i in cursor._rows:
        print(i)

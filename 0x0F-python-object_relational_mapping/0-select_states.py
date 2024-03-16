#!/usr/bin/python3
""" Module for slecting rows in db """
import MySQLdb
import sys
def connector():
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
    for i in cursor._rows:
        print(i)
    cursor.close()
    db.close()
if __name__ == "__main__":
    connector()
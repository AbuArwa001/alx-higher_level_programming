#!/usr/bin/python3
""" Module for slecting rows in db That starts with CAPS N"""
import MySQLdb
import sys


def connector():
    """
    Establishes a connection to a MySQL database and retrieves
        all rows from the 'states' table,
        where States start with capital N
    ordered by the 'id' column in ascending order.

    This function expects three command line arguments:
    - sys.argv[1]: Username for the MySQL database
    - sys.argv[2]: Password for the MySQL database
    - sys.argv[3]: Name of the MySQL database

    The function connects to the MySQL database using the provided credentials
        and retrieves
    all rows from the 'states' table, printing each row to the console.

    Note: This function requires the MySQLdb library to be installed.

    """
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
    WHERE name LIKE 'N%'
    """)
    for i in cursor._rows:
        print(i)
    cursor.close()
    db.close()


if __name__ == "__main__":
    connector()

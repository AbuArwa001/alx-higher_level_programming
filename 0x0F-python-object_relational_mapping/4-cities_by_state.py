#!/usr/bin/python3
""" Module that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def connector():
    """
    Establishes a connection to a MySQL database and retrieves
        all rows from the 'states' table,
        where IT FILTERS SEARCH
    ordered by the 'id' column in ascending order.

    This function expects three command line arguments:
    - sys.argv[1]: Username for the MySQL database
    - sys.argv[2]: Password for the MySQL database
    - sys.argv[3]: Name of the MySQL database

    The function connects to the MySQL database using the provided credentials
        and retrieves
    all rows from the 'cities' table, printing each row to the console.

    Note: This function requires the MySQLdb library to be installed.

    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    string = """SELECT cities.id,
                cities.name AS CityName ,
                states.name AS StateName
                FROM cities
                JOIN states ON states.id = cities.state_id
                ORDER BY cities.id ASC;"""
    db = MySQLdb.connect(user=username,
                         passwd=password,
                         db=dbname,
                         host="localhost",
                         port=3306)
    cursor = db.cursor()
    cursor.execute(string)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    connector()

#!/usr/bin/python3
""" Module that lists all States from the
database hbtn_0e_4_usa Using SqlAlchemy"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def connector():
    """
    Retrieves and prints all rows from the 'states'
    table in a MySQL database, ordered by 'id'.

    Requires three command line arguments:
    - MySQL database username
    - MySQL database password
    - MySQL database name

    Dependencies:
    - Requires MySQLdb and SQLAlchemy libraries.

    Example usage:
    python script_name.py username password database_name

    Assumes 'State' model mapping to 'states'
    table is defined elsewhere with attributes 'id' and 'name'.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    con_str = 'mysql+mysqldb://{}:{}@localhost/{}'.format(username,
                                                          password,
                                                          dbname)
    engine = create_engine(con_str, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.id, State.name).order_by(State.id).all()

    for state in query:
        print(f"{state.id}:", state.name)


if __name__ == "__main__":
    connector()

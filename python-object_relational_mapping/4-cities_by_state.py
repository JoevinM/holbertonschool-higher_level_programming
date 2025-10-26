#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv


def list_all_cities(user, password, db_name):
    """Return all cities as a list of tuples (id, city_name, state_name)."""
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cursor.fetchall()
    cursor.close()
    db.close()
    return rows


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./4-cities_by_state.py <user> <password> <db_name>")
    else:
        user = argv[1]
        password = argv[2]
        db_name = argv[3]
        for row in list_all_cities(user, password, db_name):
            print(row)

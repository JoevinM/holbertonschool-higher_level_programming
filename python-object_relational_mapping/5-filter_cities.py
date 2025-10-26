#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv


def list_cities_by_state(user, password, db_name, state_name):
    """Returns a comma-separated string of city names for a given state."""
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        db=db_name,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )
    rows = cursor.fetchall()
    result = ", ".join([row[0] for row in rows])
    cursor.close()
    db.close()
    return result


if __name__ == "__main__":
    if len(argv) == 5:
        print(list_cities_by_state(argv[1], argv[2], argv[3], argv[4]))
    else:
        # Optionnel mais propre : message d'usage si mauvais arguments
        print("More than 4 arguments")

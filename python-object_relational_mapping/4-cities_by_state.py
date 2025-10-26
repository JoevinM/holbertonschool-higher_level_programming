#!/usr/bin/python3
"""
lists all states with a name starting with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        port=3306,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

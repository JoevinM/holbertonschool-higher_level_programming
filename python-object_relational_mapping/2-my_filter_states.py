#!/usr/bin/python3
"""
lists all states where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=password,
        port=3306,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".
        format(state_name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

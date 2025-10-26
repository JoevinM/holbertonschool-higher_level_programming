#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
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
        "SELECT id, name FROM states \
        WHERE BINARY name = %s ORDER BY id ASC", (state_name,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

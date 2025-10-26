#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
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
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
    )

    rows = cursor.fetchall()

    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()

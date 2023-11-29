#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
import MySQLdb
import sys


def list_states(username, password, hbtn):
    """aqui se conceta con la base de datos"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=hbtn)
    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = states.id\
    ORDER BY cities.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password, hbtn = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, hbtn)

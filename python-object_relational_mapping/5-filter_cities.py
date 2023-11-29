#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
import MySQLdb
import sys


def list_states(username, password, hbtn, state):
    """aqui se conceta con la base de datos"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=hbtn)
    cur = db.cursor()

    cur.execute("SELECT cities.name \
    FROM cities JOIN states ON cities.state_id = states.id\
    WHERE states.name = 'Texas'\
    ORDER BY cities.id ASC")

    rows = cur.fetchall()

    for count, row in enumerate(rows):
        if count < len(rows) - 1:
            print('{},'.format(row[0]), end=" ")
        else:
            print('{}'.format(row[0]), end="")

    print("")

    cur.close()
    db.close()


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    hbtn, state = sys.argv[3], sys.argv[4]
    list_states(username, password, hbtn, state)

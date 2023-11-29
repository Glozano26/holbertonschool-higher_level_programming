#!/usr/bin/python3
"""A script to list states from database hbtn_0e_0_usa."""
import MySQLdb
import sys


def list_states(username, password, hbtn, state_name_searched=None):
    """aqui se conceta con la base de datos"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=hbtn)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        if row[1] == state_name_searched:
            print('({}, \'{}\')'.format(row[0], row[1]))

    cur.close()
    db.close()


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    hbtn, state_name_searched = sys.argv[3], sys.argv[4]
    list_states(username, password, hbtn, state_name_searched)

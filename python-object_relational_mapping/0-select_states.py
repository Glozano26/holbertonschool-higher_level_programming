#!/usr/bin/python3
import MySQLdb

def list_states(username, password, hbtn):
    #aqui se conceta con la base de datos
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=hbtn)
    cur = db.cursor()
    
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
        
    cur.close()
    db.close()
    
if __name__ == '__main__':
    list_states()

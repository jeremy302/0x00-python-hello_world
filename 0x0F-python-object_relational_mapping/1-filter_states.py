#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
from MySQLdb import connect
import sys

if __name__ == '__main__':
    host = 'localhost'
    user, passwd, dbname = sys.argv[1:4]

    db = connect(host=host, user=user, passwd=passwd, db=dbname)
    cur = db.cursor()

    cur.execute('select * from states where name like "N%" order by id;')
    for row in cur.fetchall():
        if row[1][0] == 'N':
            print(row)
    cur.close()
    db.close()

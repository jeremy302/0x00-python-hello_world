#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
from MySQLdb import connect
import sys

if __name__ == '__main__':
    host = 'localhost'
    user, passwd, dbname = sys.argv[1:4]

    db = connect(host=host, user=user, passwd=passwd, db=dbname)
    cur = db.cursor()

    cur.execute('select cities.id,cities.name, states.name from cities ' +
                'inner join states where cities.state_id = states.id ' +
                'order by cities.id')
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

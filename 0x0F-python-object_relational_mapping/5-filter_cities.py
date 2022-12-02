#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
from MySQLdb import connect
import sys

if __name__ == '__main__':
    host = 'localhost'
    user, passwd, dbname, state = sys.argv[1:5]

    try:
        db = connect(host=host, user=user, passwd=passwd, db=dbname)
        cur = db.cursor()
        cur.execute(
            '''select cities.name from cities where cities.state_id = ''' +
            '''(select id from states where states.name='{0}') '''
            .format(state) +
            'order by cities.id')
        rows = list(cur.fetchall())
        if rows:
            print(', '.join(row[0] for row in rows), end='')
        cur.close()
        db.close()
    except Exception:
        pass
    print()

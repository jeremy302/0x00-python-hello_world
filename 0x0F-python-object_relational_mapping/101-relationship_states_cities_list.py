#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, dbname))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as sess:
        states = sess.query(State).order_by(State.id)
        for state in states:
            print('{}: {}'.format(state.id, state.name))
            for city in sorted(state.cities, key=lambda c: c.id):
                print('    {}: {}'.format(city.id, city.name))

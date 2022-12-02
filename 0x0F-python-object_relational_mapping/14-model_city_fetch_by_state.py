#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, dbname))
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as sess:
        for city in sess.query(City).order_by(City.id):
            state = sess.query(State).filter_by(id=city.state_id).first()
            print('{}: ({}) {}'.format(state.name, city.id, city.name))

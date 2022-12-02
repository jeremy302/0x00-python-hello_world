#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    user, passwd, dbname = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, dbname))
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as sess:
        result = sess.query(State).filter(
            State.name.like('%a%')).order_by(State.id)
        for row in result:
            print('{}: {}'.format(row.id, row.name))

#!/usr/bin/python3
''' <TODO> docstring of the module for the relevant question '''
import sys

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    user, passwd, dbname, state = sys.argv[1:5]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, dbname))
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    with Session() as sess:
        result = sess.query(State).filter(State.name == state)
        row = result.first()
        if row:
            print(row.id)
        else:
            print("Not found")

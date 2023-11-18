#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    if len(sys.argv) == 5:
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(sys.argv[1],
                                       sys.argv[2],
                                       sys.argv[3]))
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(State).filter(State.name == sys.argv[4]).first()
        if state:
            print("{}".format(state.id))
        else:
            print("Not found")
        session.close()
    else:
        print("Usage: ./10-model_state_my_get.py <username> <password> \
            <database name> <state name>")

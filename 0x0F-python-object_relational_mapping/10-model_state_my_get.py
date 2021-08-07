#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    states = session.query(State).all()
    desired_state = ''
    for state in states:
        if state.name == sys.argv[4]:
            desired_state = state
        else:
            continue
    if desired_state != '':
        print(desired_state.id)
    else:
        print('Not found')

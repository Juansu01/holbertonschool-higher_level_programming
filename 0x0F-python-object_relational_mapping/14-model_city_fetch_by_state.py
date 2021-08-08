#!/usr/bin/python3
"""
Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    cities_and_states = session.query(City, State).filter(
        State.id == City.state_id).all()
    for city, state in cities_and_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

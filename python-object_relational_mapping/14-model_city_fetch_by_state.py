#!/usr/bin/python3
"""Lists first states object from the database"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import Base, City


if __name__ == "__main__":
    """Lists first state object from the database"""

    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{database}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    states = (session.query(State, City).filter(City.state_id == State.id)
              .order_by(State.id))
    for state, city in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

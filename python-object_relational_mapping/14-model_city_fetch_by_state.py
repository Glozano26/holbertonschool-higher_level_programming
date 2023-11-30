#!/usr/bin/python3
""" All states via SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def list_states(username, password, hbtn):
    """funcion para listar los estados"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, hbtn))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    citys_and_states = session.query(City, State).join(State).all()

    for city, state in citys_and_states:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password, hbtn = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, hbtn)

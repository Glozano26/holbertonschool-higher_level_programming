#!/usr/bin/python3
""" All states via SQLAlchemy"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_states(username, password, hbtn, state_name):
    """funcion para listar los estados"""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{hbtn}')

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name == state_name).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    hbtn, state_name = sys.argv[3], sys.argv[4]
    list_states(username, password, hbtn, state_name)

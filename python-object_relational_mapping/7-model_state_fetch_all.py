#!/usr/bin/python3
""" All states via SQLAlchemy"""
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


def list_states(username, password, hbtn):
    """funcion para listar los estados"""
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{hbtn}')


    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password, hbtn = sys.argv[1], sys.argv[2], sys.argv[3]
    list_states(username, password, hbtn)

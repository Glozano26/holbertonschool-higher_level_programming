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

    states = session.query(State).first()

    if states is not None:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")


if __name__ == '__main__':
    """Get arguments  from command-line"""
    username, password = sys.argv[1], sys.argv[2]
    hbtn = sys.argv[3]
    list_states(username, password, hbtn)

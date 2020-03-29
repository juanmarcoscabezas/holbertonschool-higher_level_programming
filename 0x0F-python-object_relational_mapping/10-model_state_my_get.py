#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) == 5:
        USER = sys.argv[1]
        PASSWD = sys.argv[2]
        DATABASE = sys.argv[3]
        STATE = sys.argv[4]

        DB_CON = 'mysql+mysqldb://{}:{}@localhost/{}'
        engine = create_engine(DB_CON.format(USER, PASSWD, DATABASE),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        instance = session.query(State).\
            filter_by(name=STATE).first()

        if instance is not None:
            print('{}'.format(instance.id))
        else:
            print('Not found')

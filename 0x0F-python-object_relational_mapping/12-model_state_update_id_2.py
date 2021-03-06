#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    if len(sys.argv) == 4:
        USER = sys.argv[1]
        PASSWD = sys.argv[2]
        DATABASE = sys.argv[3]

        DB_CON = 'mysql+mysqldb://{}:{}@localhost/{}'
        engine = create_engine(DB_CON.format(USER, PASSWD, DATABASE),
                               pool_pre_ping=True)
        Base.metadata.create_all(engine)

        session = Session(engine)

        session.query(State).\
            filter(State.id == 2).\
            update({State.name: "New Mexico"}, synchronize_session=False)
        session.commit()

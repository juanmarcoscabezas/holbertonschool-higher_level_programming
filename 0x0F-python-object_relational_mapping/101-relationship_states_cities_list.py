#!/usr/bin/python3

import sys
from relationship_state import State
from relationship_city import City, Base
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

        for instance in session.query(State).order_by(State.id):
            print('{}: {}'.format(instance.id, instance.name))
            for city in instance.cities:
                print('    {}: {}'.format(city.id, city.name))

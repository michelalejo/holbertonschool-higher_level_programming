#!/usr/bin/python3
"""script that lists all states from a database"""


from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        data = Session()

        results = data.query(State).filter_by(name=argv[4]).all()
        if not results:
                print("Not found")
        else:
                for dates in results:
                        print("{}".format(dates.id))

        data.close()

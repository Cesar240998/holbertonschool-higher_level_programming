#!/usr/bin/python3
"""Lists all states with a name starting with N from a database"""

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine, delete
    from model_state import Base, State
    from sys import argv
    import re

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).all()

    for i in rows:
        if 'a' in i.__dict__['name']:
            session.delete(i)

    session.commit()
    session.close()

#!/usr/bin/python3
"""Lists all states with a name starting with N from a database"""

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv
    import re

    if (len(argv) != 5):
        print('Use: username, password, database name and state')
        exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    state = argv[4]

    if (re.search('^[a-zA-Z ]+$', state) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(
            State.name.like(state))

    if (states.count() == 0):
        print("Not found")
    else:
        for state in states:
            print(f'{state.id}')

    session.close()

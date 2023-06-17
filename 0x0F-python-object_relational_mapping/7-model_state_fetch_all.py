#!/usr/bin/python3
"""list all State objects from the database passed
as argument
"""
if __name__ == '__main__':
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        database))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    rows = session.query(State).order_by(State.id)
    for row in rows:
        print('{}: {}'.format(row.id, row.name))

#!/usr/bin/python3
"""adds a state object 'louisiana' to the database passed
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

    state = State(name="Louisiana")

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(state)
    session.commit()

    state = session.query(State).filter(State.name == state.name).first()
    print(state.id)

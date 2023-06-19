#!/usr/bin/python3
"""lists all State objects, and corresponding City objects,
"""
if __name__ == '__main__':
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username,
        password,
        db_name))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc(), City.id.asc()).\
        join(State.cities)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

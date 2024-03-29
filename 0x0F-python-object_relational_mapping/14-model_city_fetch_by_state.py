#!/usr/bin/python3
"""prints all City objects from the database
"""
if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
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

    for state, city in session.query(State, City).\
            filter(State.id == City.state_id).order_by(City.id).all():
        print('{}: ({}) {}'.format(state.name, city.id, city.name))

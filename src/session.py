from sqlalchemy.orm import sessionmaker

from .orm.query import Query


def make_session(engine):
    Session = sessionmaker(bind=engine)

    return Session(query_cls=Query)

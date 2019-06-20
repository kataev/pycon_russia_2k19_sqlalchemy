import os
import typing
from contextlib import contextmanager

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker, scoped_session, Query, Mapper


def _get_query_cls(mapper, session):
    if mapper:
        m = mapper
        if isinstance(m, tuple):
            m = mapper[0]
        if isinstance(m, Mapper):
            m = m.entity

        try:
            return m.__query_cls__(mapper, session)
        except AttributeError:
            pass

    return Query(mapper, session)


Session = sessionmaker(query_cls=_get_query_cls)
engine = create_engine(os.environ["DB_URL"])
metadata = MetaData(bind=engine)
current_session = scoped_session(Session)


@as_declarative(metadata=metadata)
class Base:
    pass


@contextmanager
def session(**kwargs) -> typing.ContextManager[Session]:
    """Provide a transactional scope around a series of operations."""
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()

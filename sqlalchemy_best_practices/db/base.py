import os
import typing
from contextlib import contextmanager

from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import sessionmaker

engine = create_engine(os.environ["DB_URL"])
metadata = MetaData(bind=engine)
Session = sessionmaker()


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

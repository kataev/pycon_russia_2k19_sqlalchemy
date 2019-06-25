import asyncio
import contextvars
import functools

from contextvars_executor import ContextVarExecutor
from sqlalchemy.orm import scoped_session

from .db import Dialog, Message
from .db.base import Session

_scope = contextvars.ContextVar('session_scope')


def scopefunc():
    try:
        return _scope.get()
    except LookupError:
        raise RuntimeError('Use current_session only on request context')


def run_in_threadpool(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        def inner():
            return func(*args, **kwargs)

        return asyncio.get_running_loop().run_in_executor(None, inner)

    return wrap


current_session = scoped_session(Session, scopefunc=scopefunc)

context_executor = ContextVarExecutor()


async def example():
    loop = asyncio.get_event_loop()
    loop.set_default_executor(context_executor)
    _scope.set(1)

    d = Dialog('some_user_id')
    data = d, Message(d, 'hello'), Message(d, 'again')

    @run_in_threadpool
    def query():
        current_session.add_all(data)
        current_session.flush()

    await query()

    assert d.created_at


if __name__ == '__main__':
    asyncio.run(example())

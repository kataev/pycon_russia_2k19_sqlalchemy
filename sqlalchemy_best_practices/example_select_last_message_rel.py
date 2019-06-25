from .db import Dialog, Message, session


def query_example():
    d = Dialog('some_user_id')
    data = d, Message(d, 'hello'), Message(d, 'again')

    with session() as s:
        s.add_all(data)
        s.flush()
        assert d.last_message == data[-1]


if __name__ == '__main__':
    query_example()

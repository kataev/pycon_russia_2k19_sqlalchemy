from .db import Dialog, Message, session


def query_example():
    d = Dialog('some_user_id')
    c_m = Message(d, 'hello')
    b_m = Message(d, 'again')

    with session() as s:
        s.add_all([d, c_m, b_m])

        assert s.query(Message).last_message(d) == data[-1]


if __name__ == '__main__':
    query_example()

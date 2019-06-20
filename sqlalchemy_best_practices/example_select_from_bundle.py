from .db import Dialog, Message, MessagePerDialog, session


def query_example():
    d = Dialog('some_user_id')
    c_m = Message(d, 'hello')
    b_m = Message(d, 'again')

    with session() as s:
        s.add_all([d, c_m, b_m])

        bundle = MessagePerDialog('mean')
        for row in s.query(bundle).all():
            breakpoint()
            assert isinstance(row, MessagePerDialog)
            assert row.mean.dialog_id
            assert row.mean.count


if __name__ == '__main__':
    query_example()

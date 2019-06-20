from .db import session, Dialog, Message


def some_handler():
    dialog = Dialog('some_user_id')
    message = Message(dialog, 'Привет Олег')

    with session() as s:
        s.add(dialog)
        s.add(message)

    print(message.text)


if __name__ == '__main__':
    some_handler()

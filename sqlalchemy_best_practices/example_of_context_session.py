from .db import session, Dialog, ClientMessage


def some_handler():
    dialog = Dialog('some_user_id')
    message = ClientMessage(dialog, 'Привет Олег')

    with session() as s:
        s.add(dialog)
        s.add(message)


from .db import session, current_session, Dialog



def query_from_session():
    with session() as s:
        dialogs = s.query(Dialog).all()


def query_from_contextual_session():
    dialogs = current_session.query(Dialog).all()

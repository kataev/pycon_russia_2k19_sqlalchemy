from .db import session, Dialog


def without_explicit_flush():
    # Transient
    dialog = Dialog('some_user_id')

    with session() as s:
        s.add(dialog)  # Pending
        # Persistent
    # Detached


def with_explicit_flush():
    dialog = Dialog('some_user_id')  # Transient

    with session() as s:
        s.add(dialog)  # Pending
        s.flush()  # Persistent
    # Detached


if __name__ == '__main__':
    with_explicit_flush()

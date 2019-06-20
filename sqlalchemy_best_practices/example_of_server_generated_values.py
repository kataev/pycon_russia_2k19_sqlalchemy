from .db import Dialog, session


def fetch_created_at():
    dialog = Dialog('some_user_id')
    with session() as s:
        s.add(dialog)
        s.flush()
        assert dialog.created_at


if __name__ == '__main__':
    fetch_created_at()

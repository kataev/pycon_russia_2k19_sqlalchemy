from .db import current_session, Dialog


def some_handler(request):
    dialog = Dialog('some_user_id')
    current_session.add(dialog)

    first = current_session.query(Dialog).first()
    print(first.text)


if __name__ == '__main__':
    some_handler()

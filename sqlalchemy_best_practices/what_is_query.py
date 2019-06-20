from .db import session, Dialog


def example():
    with session() as s:
        query = s.query(Dialog)
        print(type(query))
        "<class 'sqlalchemy.orm.query.Query'>"


def filtering():
    with session() as s:
        s.query(Dialog).filter_by(user_id='some_value')

        s.query(Dialog).filter(Dialog.user_id == 'some_value')
        condition = Dialog.user_id == 'some_value'
        print(condition)
        print(type(condition))
        "<class 'sqlalchemy.sql.elements.BinaryExpression'>"

if __name__ == '__main__':
    filtering()

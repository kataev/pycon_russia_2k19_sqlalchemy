import sqlalchemy as sa
from sqlalchemy import orm as so
from sqlalchemy.ext.declarative import declared_attr

from .base import Base


class Dialog(Base):
    __tablename__ = "dialog"

    id = sa.Column('dialog_id', sa.Integer, primary_key=True)

    created_at = sa.Column(
        sa.DateTime(), nullable=False, server_default=sa.func.now()
    )
    user_id = sa.Column(sa.String, nullable=False, index=True)

    def __init__(self, user_id):
        self.user_id = user_id

    @declared_attr
    def last_message(cls):
        def condition():
            from sqlalchemy.orm import foreign, remote
            from .message import Message

            message = sa.alias(Message, 'msg')

            subquery = sa.select(
                [sa.func.max(remote(message.c.message_id))],
                whereclause=remote(message.c.dialog_id) == foreign(Dialog.id)
            )

            dialog_condition = remote(Message.dialog_id) == foreign(Dialog.id)
            message_condition = remote(Message.id) == subquery
            return dialog_condition & message_condition

        return so.relationship('Message', primaryjoin=condition, uselist=False, viewonly=True)


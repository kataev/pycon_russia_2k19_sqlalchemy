import sqlalchemy as sa
from sqlalchemy import orm as so

from .base import Base
from .dialog import Dialog


class MessageQuery(so.Query):
    def last_message(self, dialog):
        max_id = self.session.query(
            sa.func.max(Message.id)
        ).filter(Message.dialog == dialog).as_scalar()

        return self.filter(Message.id == max_id).one()


class Message(Base):
    __tablename__ = "message"
    __query_cls__ = MessageQuery

    id = sa.Column('message_id', sa.Integer, primary_key=True)
    dialog_id = sa.Column(
        Dialog.id.type, sa.ForeignKey(Dialog.id), nullable=False
    )
    client_message_id = sa.Column(
        sa.Integer, sa.ForeignKey(id), nullable=True,
    )
    text = sa.Column(sa.Text, nullable=False)
    meta = sa.Column(sa.JSON, nullable=False, default={})

    client_message = so.relationship(
        lambda: Message, backref=so.backref("bot_messages"),
        remote_side=[id],

    )
    dialog = so.relationship(
        Dialog, lazy="joined",
        backref=so.backref("messages", query_class=MessageQuery)
    )

    def __init__(self, dialog, text):
        self.dialog = dialog
        self.text = text

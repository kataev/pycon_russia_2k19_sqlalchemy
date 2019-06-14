import sqlalchemy as sa
from sqlalchemy import orm as so

from .base import Base
from .dialog import Dialog


class ClientMessage(Base):
    __tablename__ = "client_message"

    id = sa.Column(sa.Integer, primary_key=True)
    dialog_id = sa.Column(
        Dialog.id.type, sa.ForeignKey(Dialog.id), nullable=False
    )
    text = sa.Column(sa.Text, nullable=False)
    meta = sa.Column(sa.JSON, nullable=False, default={})

    dialog = so.relationship(
        Dialog, lazy="joined", backref=so.backref("client_messages")
    )

    def __init__(self, dialog, text):
        self.dialog = dialog
        self.text = text


class BotMessage(Base):
    __tablename__ = "bot_message"

    id = sa.Column(sa.Integer, primary_key=True)
    dialog_id = sa.Column(
        Dialog.id.type, sa.ForeignKey(Dialog.id), nullable=False
    )
    client_message_id = sa.Column(
        ClientMessage.id.type,
        sa.ForeignKey(ClientMessage.id),
        nullable=False,
    )
    text = sa.Column(sa.Text, nullable=False)
    meta = sa.Column(sa.JSON, nullable=False, default={})

    client_message = so.relationship(
        lambda: ClientMessage, backref=so.backref("bot_messages")
    )
    dialog = so.relationship(
        Dialog, lazy="joined", backref=so.backref("bot_messages")
    )

    def __init__(self, dialog, text):
        self.dialog = dialog
        self.text = text

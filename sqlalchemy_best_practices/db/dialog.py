import sqlalchemy as sa

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

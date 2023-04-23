import sqlalchemy as sq
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class users(Base):
    __tablename__ = "users"

    id_users_chat = sq.Column(sq.Integer)
    id_users_select = sq.Column(sq.Integer)
    UniqueConstraint('id_users_chat', 'id_users_select', name='user_unique')

    def __str__(self):
        return f'Publisher {self.id_users_chat}: {self.id_users_select}'

from sqlalchemy import Column, Integer#, String, Boolean
from sqlalchemy.orm import relationship
from model.base import db

class UserRoleLink(db.Model):
    __tablename__ = 'user_role_link'

    user_id = Column(Integer, primary_key=True)
    role_id = Column(Integer, primary_key=True)

    users = relationship('User', back_populates='users')
    roles = relationship('Role', back_populates='roles')

    def json(self):
        return {'user_id': self.user_id,
                'role_id': self.role_id}

    def __repr__(self):
        attrs = ", ".join(f"{key}={value!r}" for key, value in vars(self).items())
        return f"{self.__class__.__name__}({attrs})"
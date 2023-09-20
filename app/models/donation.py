from sqlalchemy import Column, ForeignKey, Integer, Text

from .parent_base import ParentBase


class Donation(ParentBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

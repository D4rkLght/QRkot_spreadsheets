from sqlalchemy import Column, String, Text

from .parent_base import ParentBase


class CharityProject(ParentBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

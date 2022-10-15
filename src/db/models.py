from datetime import datetime

from sqlalchemy import Column, Integer, Text, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    target_url = Column(Text())
    key = Column(String(length=10))
    secret_key = Column(String(length=15))
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())

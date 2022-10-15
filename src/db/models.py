from datetime import datetime

from sqlalchemy import Column, Integer, Text, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    target_url = Column(Text(), nullable=False)
    key = Column(String(length=10), unique=True, nullable=False)
    secret_key = Column(String(length=15), unique=True, nullable=False)
    visits = relationship('Visit')
    created_at = Column(DateTime(), nullable=False, default=datetime.now())
    updated_at = Column(DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())


class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    url_id = Column(Integer(), ForeignKey('urls.id'))
    url = relationship('Url')
    ip = Column(String(length=15), nullable=False)
    user_agent = Column(Text())
    visit_time = Column(DateTime(), nullable=False, default=datetime.now())

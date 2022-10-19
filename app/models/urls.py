from datetime import datetime

from sqlalchemy import Column, Integer, Text, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship

from app.config import config
from app.db import Base


class Url(Base):
    __tablename__ = 'urls'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    target_url = Column(Text(), nullable=False)
    key = Column(String(length=10), unique=True, nullable=False)
    secret_key = Column(String(length=15), unique=True, nullable=False)
    visits = relationship('Visit', back_populates='url')
    created_at = Column(DateTime(), nullable=False, default=datetime.now())
    updated_at = Column(DateTime(), nullable=False, default=datetime.now(), onupdate=datetime.now())

    @property
    def shorted_url(self) -> str:
        return f"{config.server.domain}/{self.key}"

    @property
    def statistics_url(self) -> str:
        return f"{config.server.domain}/{self.secret_key}"


class Visit(Base):
    __tablename__ = 'visits'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    url_id = Column(Integer(), ForeignKey('urls.id'))
    url = relationship('Url', back_populates='visits')
    ip = Column(String(length=15), nullable=False)
    user_agent = Column(Text())
    visit_time = Column(DateTime(), nullable=False, default=datetime.now())

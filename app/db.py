from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.config import config

_engine = create_engine(config.database.url)
_DBSession = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
Base = declarative_base()


def get_session() -> Session:
    return _DBSession()  # type: ignore

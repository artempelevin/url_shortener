from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.config import SQLALCHEMY_DATABASE_URL

_engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
_DBSession = sessionmaker(autocommit=False, autoflush=False, bind=_engine)
Base = declarative_base()


def get_session() -> Session:
    return _DBSession()  # type: ignore

import secrets
from random import randint
from typing import Callable

from sqlalchemy.orm import Session

from app.models import Url
from app.schemas.urls import UrlRequestScheme


def shorted_url_create(db: Session, url_info: UrlRequestScheme) -> Url:
    url = Url(
        target_url=url_info.url,
        key=_generate_uniq_key(db=db, min_size=4, max_size=10, key_is_uniq=_is_uniq_key),
        secret_key=_generate_uniq_key(db=db, min_size=5, max_size=15, key_is_uniq=_is_uniq_secret_key)
    )
    db.add(url)
    db.commit()
    return url


def _generate_uniq_key(db: Session, min_size: int, max_size: int, key_is_uniq: Callable[[Session, str], bool]) -> str:
    key_ = _generate_key(min_size=min_size, max_size=max_size)
    while not key_is_uniq(db, key_):
        key_ = _generate_key(min_size=min_size, max_size=max_size)
    return key_


def _generate_key(min_size: int, max_size: int) -> str:
    alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
    return ''.join(secrets.choice(alphabet) for _ in range(randint(min_size, max_size)))


def _is_uniq_key(db: Session, key: str) -> bool:
    return db.query(Url).filter(Url.key == key).one_or_none() is None


def _is_uniq_secret_key(db: Session, secret_key: str) -> bool:
    return db.query(Url).filter(Url.secret_key == secret_key).one_or_none() is None

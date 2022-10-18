from fastapi import Request
from sqlalchemy.orm import Session

from app.models import Url, Visit


def get_url_by_key(db: Session, key: str) -> Url | None:
    return db.query(Url).filter(Url.key == key).one_or_none()


def get_url_by_secret_key(db: Session, secret_key: str) -> Url | None:
    return db.query(Url).filter(Url.secret_key == secret_key).one_or_none()


def add_visit(db: Session, request: Request, url_info: Url) -> None:
    visit = Visit(
        url_id=url_info.id,
        ip=request.client.host,     # TODO Consider this situation
        user_agent=request.headers.get('User-Agent', '')
    )
    db.add(visit)
    db.commit()

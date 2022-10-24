from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_session
from app.schemas.urls import UrlRequestScheme, ShortedUrlResponseScheme
from app.utils.urls_crud import shorted_url_create

router = APIRouter()


@router.post(
    path='/',
    response_model=ShortedUrlResponseScheme
)
async def create_new_shorted_url(url_info: UrlRequestScheme,
                                 db: Session = Depends(get_session)) -> ShortedUrlResponseScheme:
    shorted_url = shorted_url_create(db=db, url_info=url_info)
    return ShortedUrlResponseScheme(
        original_url=shorted_url.target_url,
        shorted_url=shorted_url.shorted_url,
        statistic_url=shorted_url.statistics_url,
        created_at=shorted_url.created_at
    )

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db import get_session
from app.schemas.statistics import VisitStatisticsResponseScheme, Visit
from app.schemas.urls import ShortedUrlResponseScheme
from app.utils.urls import get_url_by_secret_key

router = APIRouter()


@router.get(
    path='/{secret_key}',
    response_model=VisitStatisticsResponseScheme
)
async def provide_url_statistics(secret_key: str, db: Session = Depends(get_session)) -> VisitStatisticsResponseScheme:
    url_info = get_url_by_secret_key(db=db, secret_key=secret_key)
    if not url_info:
        raise HTTPException(status_code=404, detail="URL not found")
    return VisitStatisticsResponseScheme(
        url_info=ShortedUrlResponseScheme(
            original_url=url_info.target_url,
            shorted_url=url_info.shorted_url,
            statistic_url=url_info.statistics_url,
            created_at=url_info.created_at
        ),
        total_visits=len(url_info.visits),
        visits=[
            Visit(ip=visit_info.ip,
                  user_agent=visit_info.user_agent,
                  time=visit_info.visit_time) for visit_info in url_info.visits
        ]
    )

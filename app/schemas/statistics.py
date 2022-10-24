from datetime import datetime

from pydantic import BaseModel

from app.schemas.urls import ShortedUrlResponseScheme


class VisitStatisticsResponseScheme(BaseModel):
    url_info: ShortedUrlResponseScheme
    total_visits: int
    visits: list["Visit"]


class Visit(BaseModel):
    ip: str
    user_agent: str
    time: datetime


VisitStatisticsResponseScheme.update_forward_refs()

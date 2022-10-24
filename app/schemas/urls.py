from datetime import datetime

from pydantic import BaseModel, HttpUrl


class UrlRequestScheme(BaseModel):
    url: HttpUrl


class ShortedUrlResponseScheme(BaseModel):
    original_url: str
    shorted_url: str
    statistic_url: str
    created_at: datetime

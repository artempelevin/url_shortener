from fastapi import APIRouter, HTTPException, Request
from fastapi import Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.config import config
from app.db import get_session
from app.utils.urls import get_url_by_key, get_url_by_secret_key, add_visit

router = APIRouter()


@router.get(
    path='/{key}',
    response_class=RedirectResponse
)
async def redirect(key: str, request: Request, db: Session = Depends(get_session)) -> RedirectResponse:
    url_by_key = get_url_by_key(db=db, key=key)
    if url_by_key:
        add_visit(db=db, request=request, url_info=url_by_key)
        return RedirectResponse(url=url_by_key.target_url)

    url_by_secret_key = get_url_by_secret_key(db=db, secret_key=key)
    if url_by_secret_key:
        return RedirectResponse(url=f"{config.api_paths.statistics}/{key}")

    raise HTTPException(status_code=404, detail="URL not found")

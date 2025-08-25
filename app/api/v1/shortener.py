from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ShortenRequest, ShortenResponse, StatsResponse
from app.crud.links import get_by_code
from app.services.shortener import shorten

router = APIRouter(prefix="/api/v1", tags=["shortener"])


@router.post("/shorten", response_model=ShortenResponse, status_code=status.HTTP_200_OK)
def create_short_url(
    payload: ShortenRequest, request: Request, db: Session = Depends(get_db)
) -> ShortenResponse:
    url = str(payload.url)
    # get short code (or create new one if it doesn't exist)
    code = shorten(db, url)
    # get full short url
    short_url = str(request.url_for("redirect_by_code", code=code))
    return ShortenResponse(short_url=short_url)


@router.get("/stats/{code}", response_model=StatsResponse)
def stats(code: str, db: Session = Depends(get_db)) -> StatsResponse:
    # get link stats by code
    link = get_by_code(db, code)
    if not link:
        raise HTTPException(status_code=404, detail="Code not found")
    return StatsResponse(
        original_url=link.original_url,
        clicks=link.clicks,
        created_at=link.created_at,
    )

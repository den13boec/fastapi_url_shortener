from contextlib import contextmanager
from typing import Any, Generator

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.api.v1.shortener import router as shortener_router
from app.crud.links import get_by_code, increment_clicks


@contextmanager
def lifespan(app: FastAPI) -> Generator[None, Any, None]:
    # create tables if not exist
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="URL Shortener", version="1.0.0", lifespan=lifespan)

# include routers
app.include_router(shortener_router)


@app.get("/s/{code}", name="redirect_by_code")
def redirect_by_code(code: str, db: Session = Depends(get_db)) -> RedirectResponse:
    # get link by code
    link = get_by_code(db, code)
    # check if link exists
    if not link:
        raise HTTPException(status_code=404, detail="Code not found")
    # increment clicks for this link
    increment_clicks(db, link)
    return RedirectResponse(url=link.original_url, status_code=307)

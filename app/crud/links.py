from typing import Optional
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from app.models import Link

def get_by_code(db: Session, code: str) -> Optional[Link]:
    # get link by its unique code
    return db.scalar(select(Link).where(Link.code == code))

def get_by_url(db: Session, url: str) -> Optional[Link]:
    # get link by its original url
    return db.scalar(select(Link).where(Link.original_url == url))

def create(db: Session, code: str, url: str) -> Link:
    # create new link
    obj = Link(code=code, original_url=url)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def increment_clicks(db: Session, link: Link) -> None:
    # increment click for the link
    db.execute(update(Link).where(Link.id == link.id).values(clicks=Link.clicks + 1))
    db.commit()

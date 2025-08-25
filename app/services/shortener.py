import secrets
from sqlalchemy.orm import Session
from app.crud.links import get_by_code, get_by_url, create
from string import ascii_letters, digits


def generate_code(db: Session, length: int = 6, max_attempts: int = 1000) -> str:
    # 52+10=62 characters
    ALPHABET = ascii_letters + digits

    # generate unique short code
    for _ in range(max_attempts):
        code = "".join(secrets.choice(ALPHABET) for _ in range(length))
        if not get_by_code(db, code):
            return code
    raise RuntimeError("Failed to generate unique short code")


def shorten(db: Session, url: str) -> str:
    # check if the URL already exists in the database
    existing = get_by_url(db, url)
    if existing:
        return existing.code
    # otherwise generate new code
    code = generate_code(db)
    create(db, code, url)
    return code

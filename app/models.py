from datetime import datetime, timezone
from sqlalchemy import Integer, String, Text, DateTime, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Link(Base):
    __tablename__ = "links"
    # ensure code field is unique across all links
    __table_args__ = (
        UniqueConstraint("code", name="uq_links_code"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    code: Mapped[str] = mapped_column(String(6), nullable=False, index=True, unique=True)
    original_url: Mapped[str] = mapped_column(Text, nullable=False)
    clicks: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))

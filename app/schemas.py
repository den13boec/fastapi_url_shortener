from datetime import datetime
from pydantic import BaseModel, Field


class ShortenRequest(BaseModel):
    url: str = Field(
        ...,
        description="Original URL to be shortened",
        examples=["https://example.com/your/very/long/url"],
    )


class ShortenResponse(BaseModel):
    short_url: str


class StatsResponse(BaseModel):
    original_url: str
    clicks: int
    created_at: datetime

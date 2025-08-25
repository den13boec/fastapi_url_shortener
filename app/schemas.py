from datetime import datetime
from pydantic import BaseModel, Field, HttpUrl, field_serializer


class ShortenRequest(BaseModel):
    url: HttpUrl = Field(
        ...,
        description="Original URL to be shortened",
        examples=["https://example.com/your/very/long/url"],
        max_length=2000,
    )


class ShortenResponse(BaseModel):
    short_url: str


class StatsResponse(BaseModel):
    original_url: str
    clicks: int
    created_at: datetime

    # searialize created_at to ISO date format
    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> str:
        return value.date().isoformat()

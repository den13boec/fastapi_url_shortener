from datetime import datetime
from pydantic import BaseModel, Field

class ShortenRequest(BaseModel):
    url: str = Field(..., description="Original URL")

class ShortenResponse(BaseModel):
    code: str
    short_url: str
    original_url: str

class StatsResponse(BaseModel):
    code: str
    original_url: str
    clicks: int
    created_at: datetime

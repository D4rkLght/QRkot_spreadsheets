from datetime import timedelta
from typing import Optional

from pydantic import BaseModel, Field

from app.core.config import MAX_SYMBOLS_NAME


class GoogleApi(BaseModel):
    name: str = Field(..., max_length=MAX_SYMBOLS_NAME)
    collection_time: timedelta
    description: Optional[str]

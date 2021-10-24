from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InboxSchema(BaseModel):
    id: Optional[int]
    code: Optional[str]
    filename: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

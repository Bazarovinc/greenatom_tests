from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InboxSchema(BaseModel):
    id: Optional[int]
    code: Optional[str]
    filename: Optional[str]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True

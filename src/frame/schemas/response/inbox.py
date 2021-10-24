from datetime import datetime

from pydantic import BaseModel


class InboxResponseSchema(BaseModel):
    id: int
    code: str
    filename: str
    created_at: datetime

    class Config:
        orm_mode = True


class FrameResponseSchema(BaseModel):
    id: int
    code: str
    filename: str
    created_at: datetime
    file: str

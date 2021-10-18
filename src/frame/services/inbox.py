from src.core.database import Base, get_db
from fastapi import Depends
from src.frame.models import Inbox
from sqlalchemy.orm import Session
from src.frame.schemas.base.inbox import InboxSchema
from typing import List


class InboxService:

    model: Base = Inbox
    schema = InboxSchema

    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def create(self, data: schema):
        data_model = self.model(**data.dict(exclude_none=True))
        self.session.add(data_model)
        self.session.commit()
        return data_model

    def get_all(self, code: str):
        return self.session.query(self.model).filter(self.model.code == code).all()

    def delete(self, id: int):
        self.session.delete(self.session.query(self.model).filter(self.model.id == id).one())
        self.session.commit()

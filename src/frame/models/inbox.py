from datetime import datetime

from sqlalchemy import VARCHAR, Column, DateTime, Integer

from src.core.database import Base


class Inbox(Base):
    __tablename__ = 'inbox'

    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(300), nullable=False)
    filename = Column(VARCHAR(300), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

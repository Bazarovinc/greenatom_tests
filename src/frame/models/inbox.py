from src.core.database import Base
from sqlalchemy import VARCHAR, Column, Integer, BigInteger, Sequence, DateTime
from datetime import datetime


class Inbox(Base):
    __tablename__ = 'inbox'

    id = Column(Integer, primary_key=True)
    code = Column(VARCHAR(300), nullable=False)
    filename = Column(VARCHAR(300), nullable=False)
    created_at = Column(DateTime, default=datetime.now)

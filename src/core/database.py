import sqlalchemy.orm

from src.core import config
from sqlalchemy.ext.declarative import declarative_base

DSN = f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}:" \
      f"{config.POSTGRES_PORT}"

engine = sqlalchemy.create_engine(DSN, pool_pre_ping=True)


SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

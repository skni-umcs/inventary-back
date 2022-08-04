from core.models import *
import core.models
from core.db import engine, SessionLocal
from sqlalchemy.orm import Session

core.models.Base.metadata.create_all(bind=engine)


def get_db_session():
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

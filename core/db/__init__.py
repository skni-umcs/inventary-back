import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from datetime import datetime

engine = db.create_engine('mysql+pymysql://inventary:inventary@db:3306/inventary', echo=True)

SessionLocal = sessionmaker(bind=engine)

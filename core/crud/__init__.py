import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from core.models import Base

engine = db.create_engine('mysql+pymysql://inventary:inventary@db:3306/inventary', echo=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


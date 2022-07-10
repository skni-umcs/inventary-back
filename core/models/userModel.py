from . import Column, Integer, String, Base, ForeignKey
from core.models.privilegesModel import PrivilegesModel


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    username = Column(String(250), unique=True)
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True)
    hashed_password = Column(String(255))
    privileges_id = Column(Integer, ForeignKey(PrivilegesModel.id))

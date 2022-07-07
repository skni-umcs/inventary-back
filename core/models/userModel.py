from . import Column, Integer, String, Base, ForeignKey
from core.models.privilgesModel import PrivilgesModel


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250))
    hashed_password = Column(String(255))
    privilges_id = Column(Integer, ForeignKey(PrivilgesModel.id))

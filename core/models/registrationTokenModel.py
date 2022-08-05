from . import Column, Integer, String, Base, ForeignKey
from core.models.userModel import UserModel


class RegistrationTokenModel(Base):
    __tablename__ = "regTokens"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(250), unique=True)
    token = Column(String(30), unique=True)
    users_limit = Column(Integer)
    user_id = Column(Integer, ForeignKey(UserModel.id))

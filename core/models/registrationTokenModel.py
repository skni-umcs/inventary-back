from . import Column, Integer, String, Base, ForeignKey
from core.models.userModel import UserModel


class registrationTokenModel(Base):
    __tablename__ = "regTokens"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    token = Column(String(30), unique=True)
    users_limit = Column(Integer)
    user_id = Column(Integer, ForeignKey(UserModel.id))

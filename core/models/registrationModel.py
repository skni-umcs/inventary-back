from . import Column, Integer, Base, ForeignKey
from core.models.userModel import UserModel
from core.models.registrationTokenModel import RegistrationTokenModel


class RegistrationModel(Base):
    __tablename__ = "registrations"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    user_id = Column(Integer, ForeignKey(UserModel.id), nullable=False)
    token_id = Column(Integer, ForeignKey(RegistrationTokenModel.id), nullable=False)

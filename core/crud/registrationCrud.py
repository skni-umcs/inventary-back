from . import Session
from core.models.registrationModel import RegistrationModel


def get_by_id(session: Session, registrationId: int):
    tokenModel: RegistrationModel = session.query(RegistrationModel).filter(RegistrationModel.id == registrationId).first()
    return tokenModel


def get_by_user_id(session: Session, userId: int):
    registrationModel: RegistrationModel = session.query(RegistrationModel).filter(RegistrationModel.user_id == userId).first()
    return registrationModel


def get_by_token_id(session: Session, tokenId: int):
    registrationModels: list[RegistrationModel] = session.query(RegistrationModel).filter(RegistrationModel.user_id == tokenId)
    return registrationModels


def add(session: Session, model: RegistrationModel):
    session.add(model)
    session.commit()


def remove(session: Session, model: RegistrationModel):
    session.delete(model)
    session.commit()


# def edit(session: Session, editModel: RegistrationModel):
#     oldModel: RegistrationModel = session.query(RegistrationModel).filter(RegistrationModel.id == editModel.id).first()
#
#     assert oldModel.user_id == editModel.user_id

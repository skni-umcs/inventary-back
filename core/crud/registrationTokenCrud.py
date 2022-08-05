from . import Session
from core.models.registrationTokenModel import RegistrationTokenModel


def get_by_id(session: Session, tokenId: int):
    tokenModel: RegistrationTokenModel = session.query(RegistrationTokenModel).filter(RegistrationTokenModel.id == tokenId).first()
    return tokenModel


def get_by_token(session: Session, token: str):
    tokenModel: RegistrationTokenModel = session.query(RegistrationTokenModel).filter(RegistrationTokenModel.token == token).first()
    return tokenModel


def add(session: Session, model: RegistrationTokenModel):
    session.add(model)
    session.commit()


def remove(session: Session, model: RegistrationTokenModel):
    session.delete(model)
    session.commit()


def edit(session: Session, editModel: RegistrationTokenModel):
    oldModel: RegistrationTokenModel = session.query(RegistrationTokenModel).filter(RegistrationTokenModel.id == editModel.id).first()

    assert oldModel.user_id == editModel.user_id
    assert oldModel.token == editModel.token

    oldModel.users_limit = editModel.users_limit

    session.commit()

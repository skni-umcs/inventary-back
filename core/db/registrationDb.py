import core.crud.registrationCrud as RC
import core.db.userDb as UD
from core.models.registrationModel import RegistrationModel
from core.schemas.registrationSchema import RegistrationSchema
from . import Session


def get_by_user_id(session: Session, userId: int) -> RegistrationSchema:
    registrationModel: RegistrationModel = RC.get_by_user_id(session, userId)

    registrationSchema = RegistrationSchema(
        id=registrationModel.id,
        token_id=registrationModel.token_id,
        user_id=registrationModel.user_id
    )

    return registrationSchema


def get_by_token_id(session: Session, tokenId: int) -> list[RegistrationSchema]:
    registrationModels: list[RegistrationModel] = RC.get_by_token_id(session, tokenId)

    registrationSchemas: list[RegistrationSchema] = []

    for registrationModel in registrationModels:
        registrationSchema = RegistrationSchema(
            id=registrationModel.id,
            token_id=registrationModel.token_id,
            user_id=registrationModel.user_id
        )
        registrationSchemas.append(registrationSchema)

    return registrationSchemas


def get_usernames_by_token_id(session: Session, tokenId: int) -> list[str]:
    registrationModels: list[RegistrationModel] = RC.get_by_token_id(session, tokenId)

    usernames: list[str] = []

    for registrationModel in registrationModels:
        userId = registrationModel.user_id
        username = UD.get_username_by_id(session, userId)
        usernames.append(username)

    return usernames

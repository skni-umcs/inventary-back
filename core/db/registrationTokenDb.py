from . import Session
import core.crud.registrationTokenCrud as RTC
import core.db.registrationDb as RD
import core.db.userDb as UD
from core.models.registrationTokenModel import RegistrationTokenModel
from core.models.userModel import UserModel
from core.schemas.registrationTokenSchema import RegistrationTokenSchema


def get_by_id(session: Session, tokenId: int) -> RegistrationTokenSchema:
    tokenModel: RegistrationTokenModel = RTC.get_by_id(session, tokenId)

    usersRegistered = RD.get_usernames_by_token_id(session, tokenModel.id)
    creatorUsername = UD.get_username_by_id(session, tokenModel.user_id)

    tokenSchema = RegistrationTokenSchema(
        id=tokenModel.id,
        token=tokenModel.token,
        users_limit=tokenModel.users_limit,
        users_registered=usersRegistered,
        creator_username=creatorUsername
    )

    return tokenSchema


def get_by_creator_id(session: Session, creatorId: int) -> list[RegistrationTokenSchema]:
    tokenModels: list[RegistrationTokenModel] = RTC.get_by_creator_id(session, creatorId)

    tokenSchemas: list[RegistrationTokenSchema] = []

    for tokenModel in tokenModels:
        usersRegistered = RD.get_usernames_by_token_id(session, tokenModel.id)
        creatorUsername = UD.get_username_by_id(session, tokenModel.user_id)

        tokenSchema: RegistrationTokenSchema = RegistrationTokenSchema(
            id=tokenModel.id,
            name=tokenModel.name,
            token=tokenModel.token,
            users_limit=tokenModel.users_limit,
            users_registered=usersRegistered,
            creator_username=creatorUsername
        )

        tokenSchemas.append(tokenSchema)

    return tokenSchemas


def get_by_token(session: Session, token: str) -> RegistrationTokenSchema:
    tokenModel: RegistrationTokenModel = RTC.get_by_token(session, token)

    assert tokenModel

    usersRegistered = RD.get_usernames_by_token_id(session, tokenModel.id)
    creatorUsername = UD.get_username_by_id(session, tokenModel.user_id)

    tokenSchema = RegistrationTokenSchema(
        id=tokenModel.id,
        name=tokenModel.name,
        token=tokenModel.token,
        users_limit=tokenModel.users_limit,
        users_registered=usersRegistered,
        creator_username=creatorUsername
    )

    return tokenSchema


def add(session: Session, tokenSchema: RegistrationTokenSchema) -> None:
    userSchema: UserModel = UD.get_by_username(session, tokenSchema.creator_username)

    tokenModel = RegistrationTokenModel(
        name=tokenSchema.name,
        token=tokenSchema.token,
        users_limit=tokenSchema.users_limit,
        user_id=userSchema.id
    )

    RTC.add(session, tokenModel)

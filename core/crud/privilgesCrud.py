from . import session
from core.models.privilegesModel import PrivilegesModel


def add(item: PrivilegesModel):
    session.add(item)
    session.commit()


def get_by_id(privligeId: int):
    item = session.query(PrivilegesModel).filter(PrivilegesModel.id == privligeId).first()

    return item


def get_by_description(description: str):
    item = session.query(PrivilegesModel).filter(PrivilegesModel.description == description).first()

    return item

from . import Session
from core.models.privilegesModel import PrivilegesModel


def add(session: Session, item: PrivilegesModel):
    session.add(item)
    session.commit()


def get_by_id(session: Session, privligeId: int):
    item = session.query(PrivilegesModel).filter(PrivilegesModel.id == privligeId).first()

    return item


def get_by_description(session: Session, description: str):
    item = session.query(PrivilegesModel).filter(PrivilegesModel.description == description).first()

    return item

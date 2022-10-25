from . import Session
from core.models import RentalRecordModel


def add(session: Session, rentalRecordModel: RentalRecordModel) -> None:
    session.add(rentalRecordModel)
    session.commit()


def get_by_id(session: Session, recordId: int) -> RentalRecordModel:
    rentalRecordModel = session.query(RentalRecordModel).filter(RentalRecordModel.id == recordId).first()

    return rentalRecordModel


def get_by_user_id(session: Session, userId: int, limit: int, offset: int) -> [RentalRecordModel]:
    rentalRecordModel = session.query(RentalRecordModel).filter(RentalRecordModel.user_id == userId)\
                            .sort_by(RentalRecordModel.date).limit(limit).offset(offset).all()

    return rentalRecordModel


def get_by_item_id_and_user_id(session: Session, itemId: int, userId: int, limit: int, offset: int) -> [RentalRecordModel]:
    rentalRecordModel = session.query(RentalRecordModel).filter(RentalRecordModel.item_id == itemId)\
                            .filter(RentalRecordModel.user_id == userId).sort_by(RentalRecordModel.date).limit(limit).offset(offset).all()

    return rentalRecordModel


def get_by_item_id(session: Session, itemId: int, limit: int, offset: int) -> [RentalRecordModel]:
    rentalRecordModel = session.query(RentalRecordModel).filter(RentalRecordModel.item_id == itemId)\
                            .sort_by(RentalRecordModel.date).limit(limit).offset(offset).all()

    return rentalRecordModel


def delete(session: Session, rentalRecordModel: RentalRecordModel) -> None:
    session.delete(rentalRecordModel)
    session.commit()


def delete_by_id(session: Session, recordId: int) -> None:
    session.query(RentalRecordModel).filter(RentalRecordModel.id == recordId).delete()
    session.commit()


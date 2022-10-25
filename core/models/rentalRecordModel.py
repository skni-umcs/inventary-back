from . import Column, Integer, String, Base, ItemModel, UserModel, DateTime, ForeignKey, WarehouseModel


class RentalRecordModel(Base):
    __tablename__ = "rental_records"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    item_id = Column(Integer, ForeignKey(ItemModel.id))
    user_id = Column(Integer, ForeignKey(UserModel.id))
    quantity = Column(Integer)
    date = Column(DateTime)
    comment = Column(String(250))
    warehouse = ForeignKey(WarehouseModel.id)

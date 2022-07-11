from . import Column, Integer, String, Base, ForeignKey
from core.models.userModel import UserModel
from core.models.categoryModel import CategoryModel
from core.models.warehouseModel import WarehouseModel


class ItemModel(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(250))
    category_id = Column(Integer, ForeignKey(CategoryModel.id))
    value = Column(Integer)
    warehouse_id = Column(Integer, ForeignKey(WarehouseModel.id))
    description = Column(String(250))
    keywords = Column(String(1000))
    user_id = Column(Integer, ForeignKey(UserModel.id))

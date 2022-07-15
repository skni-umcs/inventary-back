from . import Column, Integer, String, Base


class WarehouseModel(Base):
    __tablename__ = "warehouse"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(250), unique=True)

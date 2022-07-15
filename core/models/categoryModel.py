from . import Column, Integer, String, Base, ForeignKey


class CategoryModel(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String(250), unique=True)

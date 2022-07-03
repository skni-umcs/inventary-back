from . import Column, Integer, String, Base, ForeignKey


class ItemModel(Base):
    __tablename__ = "item"
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    category_id = Column(Integer, ForeignKey("Category.id"))
    value = Column(Integer)
    warehouse_id = Column(Integer, ForeignKey("Warehouse.id"))  # TODO foreign_key (tabela warehouse)
    description = Column(String(250))
    keywords = Column(String(1000))
    user_id = Column(Integer, ForeignKey("User.id"))

    def __init__(self, name, category_id, value, warehouse_id, description, keywords, user_id):
        self.name = name
        self.category_id = category_id
        self.value = value
        self.warehouse_id = warehouse_id
        self.description = description
        self.keywords = keywords
        self.user_id = user_id


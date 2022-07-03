from . import Column, Integer, String, Base, ForeignKey


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)


from . import Column, Integer, String, Base


class PrivilegesModel(Base):
    __tablename__ = "privileges"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    description = Column(String(255), unique=True)

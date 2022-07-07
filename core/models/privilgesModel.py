from . import Column, Integer, String, Base


class PrivilgesModel(Base):
    __tablename__ = "privilges"
    id = Column(Integer, primary_key=True, autoincrement=True)
    desc = Column(String(255))

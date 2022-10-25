from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# TODO - change table names to plural
from .categoryModel import CategoryModel
from .warehouseModel import WarehouseModel
from .userModel import UserModel
from .itemModel import ItemModel
from .privilegesModel import PrivilegesModel
from .registrationModel import RegistrationModel
from .registrationTokenModel import RegistrationTokenModel


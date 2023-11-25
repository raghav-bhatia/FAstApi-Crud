from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Employee(Base):
    __tablename__ = "Employee"

    id = Column(Integer, primary_key=True, index=True)
    fname = Column(String)
    lname = Column(String)
    age = Column(Integer)

class Employee_Login(Base):
    __tablename__ = "Employee_Login"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)
    
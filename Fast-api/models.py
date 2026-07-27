from sqlalchemy import Column, Integer, String, Float
from database import Base

class Electronics(Base):
    __tablename__ = "electronics"

    id = Column(Integer, primary_key=True, index = True)
    name = Column(String(100), nullable = False)
    category = Column(String(100), nullable= False)
    brand = Column(String(100), nullable = False)
    price = Column(Float, nullable = False)
    stock = Column(Integer, nullable = False)
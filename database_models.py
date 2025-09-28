from sqlalchemy import Integer,Float,String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    
    __tablename__ = "product"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)

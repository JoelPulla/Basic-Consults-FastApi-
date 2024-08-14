from config.database import Base
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    
    __tablename__ = 'User',
    
    id = Column(Integer, primary_key =True)
    name = Column(String)
    laste_name = Column(String)
    mail = Column(String)
    direcction = Column(String)
    number = Column(String)
    is_actie = Column(Boolean)
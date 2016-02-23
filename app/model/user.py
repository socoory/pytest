from sqlalchemy import Column, String, Integer, DateTime

from ..database import Base

class User(Base):
    __tablename__ = 'user'

    user_sql = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(64), unique=True, index=True)
    password = Column(String(64))
    name = Column(String(32))
    regdate = Column(DateTime)

    def __init__(self):
        pass
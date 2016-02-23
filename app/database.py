from sqlalchemy import create_engine , MetaData
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://python_id:wjddudry@localhost/test')
Base = declarative_base(bind=engine)
Base.metadata = MetaData(bind=engine)

def init():
    from model import user
    Base.metadata.create_all(engine)
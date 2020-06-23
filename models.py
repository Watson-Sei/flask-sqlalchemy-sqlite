from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__='users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

if __name__=='__main__':
    engine = create_engine('sqlite:///db.sqlite3', echo=True)
    Base.metadata.create_all(engine)    # テーブルを作成
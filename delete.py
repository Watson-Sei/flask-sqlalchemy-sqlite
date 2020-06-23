from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('sqlite:///db.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


# 削除処理
row = session.query(User).filter_by(id=1).one()
session.delete(row)
session.commit()
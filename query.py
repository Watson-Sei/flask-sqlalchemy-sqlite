from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User

engine = create_engine('sqlite:///db.sqlite3', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

for row in session.query(User).all():
    print(row.id, row.name, row.fullname, row.password)
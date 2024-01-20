#!/usr/bin/python3
from sqlalchemy import create_engine, MetaData, select, Table, Column, Integer, String, insert, text
from sqlalchemy.orm import declarative_base, sessionmaker

password = 'Kerra-m1'

engine = create_engine('mysql://root:root@localhost/mydata')

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(50), nullable=False)

Base.metadata.create_all(bind=engine)

new_user = User(name='Leeroy')
nyanchwa = User(name='Nyanchwa')
Session = sessionmaker()
session = Session(bind=engine)
session.add(new_user)
session.add(nyanchwa)
session.query(User)
session.commit()
rows = session.query(User).all()
print(rows)
session.close()


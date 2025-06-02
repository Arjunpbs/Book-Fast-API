from sqlalchemy import Column,Integer,String,ForeignKey
from app.utils.db import Base



class User(Base):
  __tablename__="tbl_users"
  id=Column(Integer,primary_key=True,index=True)
  username=Column(String(50),nullable=False,unique=True)
  email=Column(String(100),nullable=False,unique=True)
  password=Column(String(100),nullable=False)
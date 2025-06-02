from sqlalchemy import Column,Integer,String,ForeignKey
from app.utils.db import Base


class Book(Base):
    __tablename__="tbl_books"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100),nullable=False)
    author=Column(String(100),nullable=False)
    description=Column(String(500),nullable=True)
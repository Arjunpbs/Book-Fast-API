from fastapi import APIRouter,Depends
from app.crud import bookServices
from typing import List
from app.utils.db import get_db 
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas import BookCreate
from typing import Dict
from app.utils.general_methods import verify_token
router=APIRouter(prefix="/book",tags=["book"])

bookObject = bookServices()
@router.get("/get_all_books")
async def getAllBook(user:str=Depends(verify_token),db:AsyncSession=Depends(get_db))->Dict:
    return await bookObject.getAllBook(db)

@router.post("/add_book")
async def addBook(payload:BookCreate,db: AsyncSession = Depends(get_db),user:str=Depends(verify_token))-> dict:
    return await bookObject.addBook(db,payload)

@router.post("/update_book/{book_id:int}")
async def updateBook(book_id:int,payload:BookCreate,db:AsyncSession=Depends(get_db),user:str=Depends(verify_token))-> dict:
    
    return await bookObject.updateBook(db,book_id,payload)

@router.delete("/delete_book/{book_id:int}")
async def deleteBook(book_id:int,db: AsyncSession = Depends(get_db),user:str=Depends(verify_token))-> dict:
    return await bookObject.deleteBook(db,book_id)
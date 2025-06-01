from fastapi import APIRouter
from app.crud import bookServices


router=APIRouter(prefix="/book",tags=["book"])


@router.get("/get_all_books")
async def getAllBook():
    return await bookServices.getAllBook()

@router.post("/add_book")
async def addBook():
    return await bookServices.addBook()

@router.put("/update_book")
async def updateBook():
    return await bookServices.updateBook()

@router.delete("/delete_book")
async def deleteBook():
    return await bookServices.deleteBook()
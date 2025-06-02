from app.models.bookModel import Book
from sqlalchemy.future import select
from fastapi import HTTPException

class bookServices:
    async def getAllBook(self,db):
        try:
            result = await db.execute(select(Book))
            
            books = result.scalars().all()
           
            books_list = []
            for book in books:
                books_list.append({
                    "id": book.id,
                    "title": book.title,
                    "author": book.author,
                    "description": book.description
                })
            return {"books": books_list}

        
        except Exception as e:
            return {"error": str(e)}
        

        
    async def addBook(self,db, payload):
        try:
            new_book = Book(**payload.dict())
            print
            db.add(new_book)
            await db.commit()
            await db.refresh(new_book)
            return {"message": "Book added successfully", "book_id": new_book.id}
        except Exception as e:
            await db.rollback()
            return {"error": str(e)}
    

    async def updateBook(self,db,book_id: int, payload): 
        try:
           result = await db.execute(select(Book).where(Book.id == book_id))
           book = result.scalar_one_or_none()
           if not book:
               return HTTPException(status_code=404, detail="Book not found")
           else:
               book.title = payload.title
               book.author = payload.author    
               book.description = payload.description
               await db.commit()
               await db.refresh(book)
               return {"message": "Book updated successfully", "book_id": book_id}
        except Exception as e:
            return {"error": str(e)}
        
    
    async def deleteBook(self,db,book_id: int):
        try:
           result= await db.execute(select(Book).where(Book.id == book_id))
           book = result.scalar_one_or_none()
           if not book:
               return HTTPException(status_code=404, detail="Book not found")
           else:
               await db.delete(book)
               await db.commit()
               return {"message": "Book deleted successfully", "book_id": book_id}
        except Exception as e:
            return {"error": str(e)}
          
    
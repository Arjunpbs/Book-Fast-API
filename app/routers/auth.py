from fastapi import  APIRouter
from app.crud import authServices
from app.schemas import UserCreate,Login
from app.utils.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
router=APIRouter(prefix="/user", tags=["auth"])




userObj= authServices()
@router.post("/signup")
async def signup(payload:UserCreate,db:AsyncSession=Depends(get_db)):
    return await userObj.signIn(db, payload)

@router.post("/login")  
async def login(payload:Login, db:AsyncSession=Depends(get_db)):
    return  await userObj.logIn(db, payload)

@router.post("/logout")
async def logout():
    return await authServices.logOut()
from fastapi import  APIRouter
from app.crud import authServices


router=APIRouter(prefix="/user", tags=["auth"])

@router.post("/signup")
async def signup():
    return await authServices.signIn()

@router.post("/login")  
async def login():
    return  await authServices.logIn()

@router.post("/logout")
async def logout():
    return await authServices.logOut()
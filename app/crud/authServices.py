from app.models.userModel import User
from app.utils.general_methods import hashpassword,verify_password,create_access_token
from fastapi.responses import JSONResponse
from sqlalchemy.future import select
class authServices:
   async def signIn(self, db, payload):
       try:
           hashedpw = hashpassword(payload.password)
           user= User(
               username=payload.username,
               email=payload.email,
                password=hashedpw,
           )
           db.add(user)
           await db.commit()
           await db.refresh(user)
           return {"message": "User signed up successfully"}  
       except Exception as e:
            await db.rollback()
            return {"error": f"User creation failed {str(e)}"}
      
   
   async def logIn(self,db,payload):
       
        try:
                
                result = await db.execute(select(User).where(User.username == payload.username))
                user = result.scalars().first()
                if not user:
                    return JSONResponse({"error": "User not found"})
                if not verify_password(payload.password, user.password):
                     return JSONResponse(content={"error": "Invalid password"}, status_code=401)
                else:
                    access_token = create_access_token(
                                data={"sub": user.username}
                            )
                    return JSONResponse(
                        content={
                            "message": "Login successful",
                            "access_token": access_token,
                            "token_type": "bearer"
                        },
                        status_code=200
                    )

        except Exception as e:
                return JSONResponse({"error": f"Login failed: {str(e)}"}, status_code=500)


   async def logOut(self):  
        return {"message": "User logged out successfully"}
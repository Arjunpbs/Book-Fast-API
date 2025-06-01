class authServices:
   async def signIn(self):
       return {"message": "User signed up successfully"}  
   
   async def logIn(self):
       return {"message": "User logged in successfully"}
   

   async def logOut(self):  
        return {"message": "User logged out successfully"}
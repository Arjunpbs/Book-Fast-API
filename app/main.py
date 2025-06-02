
import os



from fastapi import FastAPI,Depends
import uvicorn
from app.utils.db import engine, Base

from app.routers import allRouters

from app.utils.db import engine

app=FastAPI()

for router in allRouters:
    app.include_router(router)



@app.on_event("startup")
async def on_startup():
    # Example: Automatically create all tables (if needed)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("Database tables created or already exist.")



@app.on_event("shutdown")
async def shutdown_event():
   
    await engine.dispose() 
    print("Shutdown event: Cleaning up resources...")


# if __name__=="__main__":
#      uvicorn.run(app, host="0.0.0.0",port=8000)

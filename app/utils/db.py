from app.config import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine=create_async_engine(
   url=DATABASE_URL,
    echo=True,
    future=True 
)
AsyncSessionLocal=sessionmaker(
  bind=engine,
    class_=AsyncSession,    
    expire_on_commit=False,
    autoflush=False,
)


# Base class for models

Base=declarative_base()

async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
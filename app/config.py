from dotenv import load_dotenv
import os


load_dotenv()

# Get the absolute path to the directory where the current script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("Base directory:", BASE_DIR)




DB_USER = os.getenv("DB_USER")
print(DB_USER)
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
print(DB_PORT)
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("JWT_SECRET")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


DATABASE_URL=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
import bcrypt
def hashpassword(password: str) -> str:
  salt=bcrypt.gensalt()
  hashed=bcrypt.hashpw(password.encode('utf-8'), salt)
  hashedpw= hashed.decode('utf-8')
  return hashedpw


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import  HTTPException,status
def create_access_token(data: dict)->str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    encoded_jwt=f"Bearer {encoded_jwt}"
    return encoded_jwt


def verify_token(bearer_token: str):
    try:
        if not bearer_token.startswith("Bearer "):
            raise ValueError("Invalid token format. Token must start with 'Bearer '")
        
        token = bearer_token.removeprefix("Bearer ").strip()
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    
    except JWTError:
         raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
       

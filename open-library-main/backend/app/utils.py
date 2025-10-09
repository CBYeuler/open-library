from passilb.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from config import settings

pwd-context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    # hash a plain password
    return pwd_context.hash(password)

def verify_password(plain:str, hashed:str) -> bool:
    # verify a plain password against hashed
    return pwd_context.verify(plain,hashed)

def create_access_token(subject:str | int, expires_minutes:int | None=None) -> str:
    # set expiry time
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {"sub":str(subject), "exp":expire}
    
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token:str) -> dict:
    # decode and verify token
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])

# add more utility functions here as needed
from jose import JWTError, jwt
from datetime import datetime, timedelta

# openssl rand -hex 32
SECRET_KEY = "72cb597c794195196863d8fd6d8746aaf6fe073b245f17be2e7b28626a168314"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

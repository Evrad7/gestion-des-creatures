import os
from datetime import timedelta, datetime
from jose import jwt, JWTError
from passlib.context import CryptContext
from errors import Missing, Duplicate
from fastapi import HTTPException, status
from model.user import User, CreateUser, InnerUser

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake.data import user as data
else:
    from data import  user as data

SECRET_KEY="secure_generated_secret_code"
ALGORITH="HS256"
pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto" )


def verified_password(plain:str, hash:str):
    """Hash <plain> and compare with <hash> from the database"""
    return pwd_context.verify(plain, hash)

def get_hash(plain:str):
    """Return the hash of a <plain> string"""
    return pwd_context.hash(plain)

def lookup_user(username:str) -> User | None:
    try:
        return data.get_one(name=username)
    except Missing:
        return None

def get_jwt_username(token:str):
    """Return username from JWT access <token>"""
    try:
        playout=jwt.decode(access_token=token, key=SECRET_KEY, algorithms=[ALGORITH])
        if not (username:=playout.get("sub")):
            return None
    except JWTError:
        return None
    return username


def get_current_user(token:str):
    if not (username:=get_jwt_username(token)):
        return None
    if not (user:=lookup_user(username)):
        return None
    return user
    
def create_access_token(data:dict, expires:timedelta):
    src=data.copy()
    now=datetime.now()
    if not expires:
        expires=timedelta(minutes=15)
    src.update({"exp":now+expires})
    return jwt.encode(claims=src, key=SECRET_KEY, algorithm=ALGORITH)

def auth_user(name:str, plain:str):
    """Authenticate user <name> and <plain> password"""
    if not (user:=lookup_user(username=name)):
        return None
    if not verified_password(plain, user.hash):
        return None
    return user

def get_all():
    return data.get_all()

def get_one(name:str):
    try:
        return data.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)

def create(create_user:CreateUser):
    inner_user=InnerUser(
        name=create_user.name,
        hash=get_hash(create_user.password))
    try:
        return data.create(inner_user)
    except Duplicate as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.msg)


def modify(create_user:CreateUser):
    inner_user=InnerUser(
        name=create_user.name,
        hash=get_hash(create_user.password))
    try:
        return data.modify(inner_user)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)


def delete(user:User):
    try:
        return data.delete(user)
    except Missing as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.msg)
    except Duplicate as exc:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=exc.msg)
    




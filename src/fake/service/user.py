from model.user import User
from fastapi import HTTPException
from fastapi import status

import fake.data.user as data


def get_all()->list[User]:
    return data._users

def get_one(name:str)->User:
    user=data.find(name)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing user {name}")
    return user


def create(user:User)->User:
    if  data.find(user.name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Duplicate user {user.name}")
    return user


def modify(user:User)->User:
    if not data.find(user.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing user {user.name}")
    return user


def replace(user:User)->User:
    return data.replace(user)

def delete(user:User)->None:
    if not data.find(user.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing user {user.name}")
    return user

    

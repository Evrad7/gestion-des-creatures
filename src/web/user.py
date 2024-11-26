import os
from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from service import user as service
from model.user import User, CreateUser

if os.getenv("CRYPTID_UNIT_TEST"):
    import fake.service.user as service
else:
    import service.user as service

ACCESS_TOKEN_EXPIRES_MINUTE=15
router=APIRouter(prefix="/user")

oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/user/token")

unauth_exception=HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="username or password incorrect",
    headers={"WWW-Authenticate": "Bearer"},
)

@router.post("/token")
def create_access_token(form_data:Annotated[OAuth2PasswordRequestForm, Depends()]):

    """Get username and password from OAuth form,
        return access token"""
    
    user=service.auth_user(form_data.username, form_data.password)
    if not user:
        raise unauth_exception
    token=service.create_access_token(data={"sub":user.name}, expires=timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTE))
    return {"access_token":token, "token_type":"bearer"}


@router.get("/token")
def get_access_token(token:Annotated[str, Depends(oauth2_scheme)]):
    """Return the current access token"""
    return {"token":token}



@router.get("/")
@router.get("")
def get_all() -> list[User]:
    return service.get_all()


@router.get("/{name}")
@router.get("/{name}/")
def get_one(name:str) -> service.User | None:
    return service.get_one(name)

@router.post("",status_code=201, response_model=User)
@router.post("/", status_code=201, response_model=User)
def create(create_user:CreateUser):
    return service.create(create_user)

@router.put("")
@router.put("/")
def modify(create_user:CreateUser) -> User:
    return service.modify(create_user)


# @router.patch("/")
# def replace(user:User) -> User:
#     return service.replace(user)

@router.delete("",status_code=204)
@router.delete("/", status_code=204)
def delete(user:User) -> None:
    return service.delete(user)

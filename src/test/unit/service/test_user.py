import os
from model.user import User, CreateUser, InnerUser
from fastapi import HTTPException
import pytest

os.environ["CRYPTID_UNIT_TEST"]="true"

import service.user as service


def test_create(create_user:CreateUser) -> None:
    user:InnerUser=service.create(create_user)
    assert user.name==create_user.name

def test_create_duplicate(users:list[User]):
    create_user:CreateUser=CreateUser(name=users[0].name, password="password")
    with pytest.raises(HTTPException):
        service.create(create_user)

def test_get_one(users:list[User]):
    assert users[0]==service.get_one(users[0].name)

def test_get_one_missing(user:User):
    with pytest.raises(HTTPException):
        service.get_one(user.name)


def test_modify(users:list[User]):
    user:CreateUser=CreateUser(name=users[0].name, password="password")
    assert user.name==service.modify(user).name

def test_modify_missing(create_user:CreateUser):
    with pytest.raises(HTTPException):
        service.modify(create_user)

def test_delete(users:list[User]):
    assert service.delete(users[0])

def test_delete_missing(user:User):
    with pytest.raises(HTTPException):
        service.delete(user)


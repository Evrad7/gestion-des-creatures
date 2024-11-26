import os
from fastapi import HTTPException, status
from model.user import User
import pytest

os.environ["CRYPTID_UNIT_TEST"]="true"
import web.user as web




def assert_duplicate(exc:HTTPException):
    assert exc.status_code==status.HTTP_409_CONFLICT
    assert "Duplicate" in exc.msg


def assert_missing(exc:HTTPException):
    assert exc.status_code==status.HTTP_404_NOT_FOUND
    assert "Missing" in exc.msg

def test_create(user:User):
    assert web.create(user)==user

def test_create_duplicate(users:list[User]):
    with pytest.raises(HTTPException) as exc:
        web.create(users[0])
        assert_duplicate(exc)

def test_get_one(users:list[User]):
    assert web.get_one(users[0].name)==users[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        web.get_one("MISSING")
        assert_missing()


def test_modify(users:list[User]):
    assert web.modify(users[0])==users[0]

def test_modify_missing(user:User):
    with pytest.raises(HTTPException) as exc:
        web.modify(user)
        assert_missing(exc)



def test_delete(users:list[User]):
    assert web.delete(users[0])

def test_delete_missing(user:User):
    with pytest.raises(HTTPException) as exc:
        web.delete(user)
        assert_missing(exc)


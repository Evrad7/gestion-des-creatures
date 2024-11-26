
import os
import pytest
from errors import Duplicate, Missing
from model.user import InnerUser

os.environ["CRYPTID_SQLITE_DB"]=":memory:"
import data.user


def test_create(user:InnerUser):
    resp=data.user.create(user, "user")
    assert resp==user

def test_create_one_duplicate(user:InnerUser):
    with pytest.raises(Duplicate):
        data.user.create(user, "user")

def test_get_one(user:InnerUser):
    resp=data.user.get_one(user.name)
    assert user==resp

def test_get_one_missing(user:InnerUser):
    with pytest.raises(Missing):
        data.user.get_one("MISSING")

def test_modify(user:InnerUser):
    user.hash="modified hash"
    resp=data.user.modify(user)
    assert resp==user

def test_modify_missing(user:InnerUser):
    test_user=InnerUser(name="MISSING", hash=user.hash)
    with pytest.raises(Missing):
        data.user.modify(test_user)

def test_delete(user:InnerUser):
    print(data.user.get_one(user.name), "++++++++++++++++++++++++++++++")
    assert data.user.delete(user)

def test_delete_missing(user:InnerUser):
    with pytest.raises(Missing):
        data.user.delete(user)
    
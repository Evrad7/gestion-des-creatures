import os
from fastapi import HTTPException, status
from model.creature import Creature
import pytest

os.environ["CRYPTID_UNIT_TEST"]="true"
import web.creature as web




def assert_duplicate(exc:HTTPException):
    assert exc.status_code==status.HTTP_409_CONFLICT
    assert "Duplicate" in exc.msg


def assert_missing(exc:HTTPException):
    assert exc.status_code==status.HTTP_404_NOT_FOUND
    assert "Missing" in exc.msg

def test_create(creature:Creature):
    assert web.create(creature)==creature

def test_create_duplicate(creatures:list[Creature]):
    with pytest.raises(HTTPException) as exc:
        web.create(creatures[0])
        assert_duplicate(exc)

def test_get_one(creatures:list[Creature]):
    assert web.get_one(creatures[0].name)==creatures[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        web.get_one("MISSING")
        assert_missing()


def test_modify(creatures:list[Creature]):
    assert web.modify(creatures[0])==creatures[0]

def test_modify_missing(creature:Creature):
    with pytest.raises(HTTPException) as exc:
        web.modify(creature)
        assert_missing(exc)



def test_delete(creatures:list[Creature]):
    assert web.delete(creatures[0])

def test_delete_missing(creature:Creature):
    with pytest.raises(HTTPException) as exc:
        web.delete(creature)
        assert_missing(exc)


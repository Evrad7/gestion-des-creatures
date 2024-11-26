import os
from fastapi import HTTPException, status
from model.explorer import Explorer
import pytest

os.environ["CRYPTID_UNIT_TEST"]="true"
import web.explorer as web




def assert_duplicate(exc:HTTPException):
    assert exc.status_code==status.HTTP_409_CONFLICT
    assert "Duplicate" in exc.msg


def assert_missing(exc:HTTPException):
    assert exc.status_code==status.HTTP_404_NOT_FOUND
    assert "Missing" in exc.msg

def test_create(explorer:Explorer):
    assert web.create(explorer)==explorer

def test_create_duplicate(explorers:list[Explorer]):
    with pytest.raises(HTTPException) as exc:
        web.create(explorers[0])
        assert_duplicate(exc)

def test_get_one(explorers:list[Explorer]):
    assert web.get_one(explorers[0].name)==explorers[0]

def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        web.get_one("MISSING")
        assert_missing()


def test_modify(explorers:list[Explorer]):
    assert web.modify(explorers[0])==explorers[0]

def test_modify_missing(explorer:Explorer):
    with pytest.raises(HTTPException) as exc:
        web.modify(explorer)
        assert_missing(exc)



def test_delete(explorers:list[Explorer]):
    assert web.delete(explorers[0])

def test_delete_missing(explorer:Explorer):
    with pytest.raises(HTTPException) as exc:
        web.delete(explorer)
        assert_missing(exc)


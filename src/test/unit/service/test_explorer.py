
import os
from model.explorer import Explorer
from fastapi import HTTPException
import pytest

os.environ["CRYPTID_UNIT_TEST"]="true"

import service.explorer as service


def test_create(explorer:Explorer) -> None:
    assert explorer==service.create(explorer)

def test_create_duplicate(explorers:list[Explorer]):
    with pytest.raises(HTTPException):
        service.create(explorers[0])

def test_get_one(explorers:list[Explorer]):
    assert explorers[0]==service.get_one(explorers[0].name)

def test_get_one_missing(explorer:Explorer):
    with pytest.raises(HTTPException):
        service.get_one(explorer.name)


def test_modify(explorers:list[Explorer]):
    assert explorers[0]==service.modify(explorers[0])

def test_modify_missing(explorer:Explorer):
    with pytest.raises(HTTPException):
        service.modify(explorer)

def test_delete(explorers:list[Explorer]):
    assert service.delete(explorers[0])

def test_delete_missing(explorer:Explorer):
    with pytest.raises(HTTPException):
        service.delete(explorer)


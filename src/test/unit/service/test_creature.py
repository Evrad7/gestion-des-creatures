import os
from model.creature import Creature
from errors import Duplicate, Missing
from fastapi import HTTPException
import pytest

os.environ["CRYPTID_UNIT_TEST"]="true"

import service.creature as service


def test_create(creature:Creature) -> None:
    assert creature==service.create(creature)

def test_create_duplicate(creatures:list[Creature]):
    with pytest.raises(HTTPException):
        service.create(creatures[0])

def test_get_one(creatures:list[Creature]):
    assert creatures[0]==service.get_one(creatures[0].name)

def test_get_one_missing(creature:Creature):
    with pytest.raises(HTTPException):
        service.get_one(creature.name)


def test_modify(creatures:list[Creature]):
    assert creatures[0]==service.modify(creatures[0])

def test_modify_missing(creature:Creature):
    with pytest.raises(HTTPException):
        service.modify(creature)

def test_delete(creatures:list[Creature]):
    assert service.delete(creatures[0])

def test_delete_missing(creature:Creature):
    with pytest.raises(HTTPException):
        service.delete(creature)


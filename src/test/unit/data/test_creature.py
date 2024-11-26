
import os
import pytest
from errors import Duplicate, Missing
from model.creature import Creature

os.environ["CRYPTID_SQLITE_DB"]=":memory:"
import data.creature


def test_create(creature:Creature):
    resp=data.creature.create(creature)
    assert resp==creature

def test_create_one_duplicate(creature:Creature):
    with pytest.raises(Duplicate):
        data.creature.create(creature)

def test_get_one(creature:Creature):
    resp=data.creature.get_one(creature.name)
    assert creature==resp

def test_get_one_missing(creature:Creature):
    with pytest.raises(Missing):
        data.creature.get_one("MISSING")

def test_modify(creature:Creature):
    creature.description="modified description"
    resp=data.creature.modify(creature)
    assert resp==creature

def test_modify_missing(creature:Creature):
    creature.name="MISSING"
    with pytest.raises(Missing):
        data.creature.modify(creature)

def test_delete(creature:Creature):
    assert data.creature.delete(creature)

def test_delete_missing(creature:Creature):
    with pytest.raises(Missing):
        data.creature.delete(creature)
    
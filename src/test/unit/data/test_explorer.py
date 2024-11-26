
import os
import pytest
from errors import Duplicate, Missing
from model.explorer import Explorer

os.environ["CRYPTID_SQLITE_DB"]=":memory:"
import data.explorer


def test_create(explorer:Explorer):
    resp=data.explorer.create(explorer)
    assert resp==explorer

def test_create_one_duplicate(explorer:Explorer):
    with pytest.raises(Duplicate):
        data.explorer.create(explorer)

def test_get_one(explorer:Explorer):
    resp=data.explorer.get_one(explorer.name)
    assert explorer==resp

def test_get_one_missing(explorer:Explorer):
    with pytest.raises(Missing):
        data.explorer.get_one("MISSING")

def test_modify(explorer:Explorer):
    explorer.description="modified description"
    resp=data.explorer.modify(explorer)
    assert resp==explorer

def test_modify_missing(explorer:Explorer):
    explorer.name="MISSING"
    with pytest.raises(Missing):
        data.explorer.modify(explorer)

def test_delete(explorer:Explorer):
    assert data.explorer.delete(explorer)

def test_delete_missing(explorer:Explorer):
    with pytest.raises(Missing):
        data.explorer.delete(explorer)
    
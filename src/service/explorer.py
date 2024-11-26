import os
from fastapi import HTTPException
from model.explorer import Explorer
from errors import Missing, Duplicate

if os.getenv("CRYPTID_UNIT_TEST"):
    import fake.data.explorer as data
else:
    import data.explorer as data

def get_all()->list[Explorer]:
    return data.get_all()

def get_one(name:str)->Explorer:
    try:
        explorer=data.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    return explorer

def create(explorer:Explorer)->Explorer:
    try:
        return data.create(explorer)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)


def modify(explorer:Explorer)->Explorer:
    try:
        return data.modify(explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


def replace(explorer:Explorer)->Explorer:
    return data.replace(explorer)

def delete(explorer:Explorer)->None:
    try:
        return data.delete(explorer)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

    


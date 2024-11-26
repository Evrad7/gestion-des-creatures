import os
from fastapi import HTTPException
from model.creature import Creature
from errors import Missing, Duplicate

if os.getenv("CRYPTID_UNIT_TEST"):
    import fake.data.creature as data
else:
    import data.creature as data

def get_all()->list[Creature]:
    return data.get_all()

def get_one(name:str)->Creature:
    try:
        creature=data.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    return creature

def create(creature:Creature)->Creature:
    try:
        return data.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=409, detail=exc.msg)


def modify(creature:Creature)->Creature:
    try:
        return data.modify(creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)


def replace(creature:Creature)->Creature:
    return data.replace(creature)

def delete(creature:Creature)->None:
    try:
        return data.delete(creature)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

    


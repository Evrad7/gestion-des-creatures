from model.creature import Creature
from fastapi import HTTPException
from fastapi import status

import fake.data.creature as data


def get_all()->list[Creature]:
    return data._creatures

def get_one(name:str)->Creature:
    creature=data.find(name)
    if not creature:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing creature {name}")
    return creature


def create(creature:Creature)->Creature:
    if  data.find(creature.name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Duplicate creature {creature.name}")
    return creature


def modify(creature:Creature)->Creature:
    if not data.find(creature.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing creature {creature.name}")
    return creature


def replace(creature:Creature)->Creature:
    return data.replace(creature)

def delete(creature:Creature)->None:
    if not data.find(creature.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing creature {creature.name}")
    return creature

    

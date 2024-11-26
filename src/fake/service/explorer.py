from model.explorer import Explorer
from fastapi import HTTPException
from fastapi import status

import fake.data.explorer as data


def get_all()->list[Explorer]:
    return data._explorers

def get_one(name:str)->Explorer:
    explorer=data.find(name)
    if not explorer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing explorer {name}")
    return explorer


def create(explorer:Explorer)->Explorer:
    if  data.find(explorer.name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Duplicate explorer {explorer.name}")
    return explorer


def modify(explorer:Explorer)->Explorer:
    if not data.find(explorer.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing explorer {explorer.name}")
    return explorer


def replace(explorer:Explorer)->Explorer:
    return data.replace(explorer)

def delete(explorer:Explorer)->None:
    if not data.find(explorer.name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Missing explorer {explorer.name}")
    return explorer

    

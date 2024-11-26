import os
from fastapi import APIRouter
from model.creature import Creature

if os.getenv("CRYPTID_UNIT_TEST"):
    import fake.service.creature as service
else:
    import service.creature as service


router=APIRouter(prefix="/creature")

@router.get("/")
@router.get("")
def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/{name}")
@router.get("/{name}/")
def get_one(name:str) -> service.Creature | None:
    return service.get_one(name)

@router.post("",status_code=201)
@router.post("/", status_code=201)
def create(creature:Creature) -> Creature:
    return service.create(creature)

@router.put("")
@router.put("/")
def modify(creature:Creature) -> Creature:
    return service.modify(creature)


# @router.patch("/")
# def replace(creature:Creature) -> Creature:
#     return service.replace(creature)

@router.delete("",status_code=204)
@router.delete("/", status_code=204)
def delete(creature:Creature) -> None:
    return service.delete(creature)

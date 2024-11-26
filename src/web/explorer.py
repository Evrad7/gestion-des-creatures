import os
from fastapi import APIRouter
import service.explorer as service
from model.explorer import Explorer

if os.getenv("CRYPTID_UNIT_TEST"):
    import fake.service.explorer as service
else:
    import service.explorer as service

router=APIRouter(prefix="/explorer")

@router.get("")
@router.get("/")
def get_all() ->list[Explorer]:
    return service.get_all()

@router.get("/{name}")
@router.get("/{name}/")
def get_one(name:str) -> service.Explorer | None:
    return service.get_one(name)


@router.post("",status_code=201)
@router.post("/", status_code=201)
def create(explorer:Explorer) -> Explorer:
    return service.create(explorer)


@router.put("")
@router.put("/")
def modify(explorer:Explorer) -> Explorer:
    return service.modify(explorer)

# @router.patch("/")
# def replace(explorer:Explorer) -> Explorer:
#     return service.replace(explorer)


@router.delete("", status_code=204)
@router.delete("/", status_code=204)
def delete(explorer:Explorer) -> None:
    return service.delete(explorer)

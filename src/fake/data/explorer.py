from model.explorer import Explorer
from errors import Missing, Duplicate

_explorers:list[Explorer]=[
    Explorer(name="Claude Hande",
        country="FR",
        description="Scarce during full moons"),

    Explorer(name="Noah Weiser",
    country="DE",
    description="Myopic machete man"),
]

def find(name:str) -> Explorer | None:
    for _ in _explorers:
        if _.name == name:
            return _
        
def check_missing(name:str):
    if not find(name):
        raise Missing(f"Missing explorer {name}")

def check_duplicate(name:str):
    if find(name):
        raise Duplicate(f"Duplicate explorer  {name}")

def get_all() -> list[Explorer]:
    return _explorers

def get_one(name:str) -> Explorer | None:
    check_missing(name)
    return find(name)
        
def create(explorer: Explorer) -> Explorer:
    check_duplicate(explorer.name)
    return explorer

def modify(explorer: Explorer) -> Explorer:
    check_missing(explorer.name)
    return explorer

def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer

def delete(explorer: Explorer) -> bool:
    check_missing(explorer.name)
    return True
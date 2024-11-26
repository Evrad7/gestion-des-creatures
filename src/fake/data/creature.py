from model.creature import Creature
from errors import Missing, Duplicate

_creatures:list[Creature]=[
    
    Creature(name="Yeti",
    aka="Abominable Snowman",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan"),

    Creature(name="Bigfoot",
    description="Yeti's Cousin Eddie",
    country="US",
    area="*",
    aka="Sasquatch")

]

def find(name:str) -> Creature | None:
    for _ in _creatures:
        if _.name == name:
            return _
        
def check_missing(name:str):
    if not find(name):
        raise Missing(f"Missing creature {name}")

def check_duplicate(name:str):
    if find(name):
        raise Duplicate(f"Duplicate creature  {name}")

def get_all() -> list[Creature]:
    return _creatures

def get_one(name:str) -> Creature | None:
    check_missing(name)
    return find(name)
        
def create(creature: Creature) -> Creature:
    check_duplicate(creature.name)
    return creature

def modify(creature: Creature) -> Creature:
    check_missing(creature.name)
    return creature

def replace(creature: Creature) -> Creature:
    """Completely replace an creature"""
    return creature

def delete(creature: Creature) -> bool:
    check_missing(creature.name)
    return True
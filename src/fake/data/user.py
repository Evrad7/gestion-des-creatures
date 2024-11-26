from model.user import User
from errors import Missing, Duplicate

_users:list[User]=[
    
    User(name="Jean",
        hash="xyz",
    ),

    User(name="Paul",
         hash="abc"
    )

]
def find(name:str) -> User | None:
    for _ in _users:
        if _.name == name:
            return _
        
def check_missing(name:str):
    if not find(name):
        raise Missing(f"Missing user {name}")

def check_duplicate(name:str):
    if find(name):
        raise Duplicate(f"Duplicate user  {name}")

def get_all() -> list[User]:
    return _users

def get_one(name:str) -> User | None:
    check_missing(name)
    return find(name)
        
def create(user: User) -> User:
    check_duplicate(user.name)
    return user

def modify(user: User) -> User:
    check_missing(user.name)
    return user

def replace(user: User) -> User:
    return user

def delete(user:User) -> bool:
    check_missing(user.name)
    return True
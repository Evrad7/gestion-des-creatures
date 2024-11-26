from sqlite3 import IntegrityError
from typing import Any
from model.user import User, InnerUser
from . import curs, conn
from errors  import Missing, Duplicate


def init() -> None:
    curs.execute(
        """CREATE TABLE IF NOT EXISTS user
        (name text primary key,
         hash text
        )
        """
        )
    
    curs.execute(
        """CREATE TABLE IF NOT EXISTS xuser
        (name text primary key,
         hash text
        )
        """
        )

init()

def row_to_model(row:tuple) -> InnerUser:
    name, hash=row
    return InnerUser(name=name, hash=hash)

def model_to_dict(inner_user:InnerUser) -> dict[str, Any]:
    return inner_user.model_dump()

def get_all() -> list[InnerUser]:
    stmt:str="SELECT * FROM user"
    curs.execute(stmt)
    rows=list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def get_one(name, table:str="user") -> InnerUser:
    stmt:str=f"SELECT * FROM {table} WHERE name=:name"
    curs.execute(stmt, {"name":name})
    row=curs.fetchone()
    if not row:
        raise Missing(msg=f"User {name} not found")
    return row_to_model(row)

def create(inner_user:InnerUser, table:str="user") -> InnerUser:
    stmt:str=f"INSERT INTO {table} VALUES (:name, :hash)"
    try:
        curs.execute(stmt, model_to_dict(inner_user))
    except IntegrityError:
        raise Duplicate(f"User {inner_user.name} already exists")
    conn.commit()
    return get_one(inner_user.name, table=table)

def modify(inner_user:InnerUser) -> InnerUser:
    stmt:str="""
    UPDATE user
    SET name=:name,
        hash=:hash
        WHERE name=:name_orig
    """
    params=model_to_dict(inner_user)
    params["name_orig"]=inner_user.name
    curs.execute(stmt,params)
    if curs.rowcount!=1:
        raise Missing(msg=f"User {inner_user.name} not found")
    conn.commit()
    return get_one(inner_user.name)

def replace(inner_user:InnerUser) -> InnerUser:
    return inner_user

def delete(user:User):
    inner_user=get_one(user.name)
    stmt="DELETE FROM user WHERE name=:name"
    res=curs.execute(stmt, {"name":user.name})
    if curs.rowcount!=1:
        raise Missing(msg=f"User {user.name} not found")
    create(inner_user, "xuser")
    conn.commit()
    return bool(res)


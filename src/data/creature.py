from sqlite3 import IntegrityError
from typing import Any
from model.creature import Creature
from . import curs, conn
from errors  import Missing, Duplicate


def init() -> None:
    curs.execute(
        """CREATE TABLE IF NOT EXISTS creature
        (name text primary key,
         country text,
         description text,
         area text,
         aka text)
        """
        )

init()

def row_to_model(row:tuple) -> Creature:
    name, country, description, area, aka=row
    return Creature(name=name, country=country, description=description, area=area, aka=aka)

def model_to_dict(creature:Creature) -> dict[str, Any]:
    return creature.model_dump()

def get_all() -> list[Creature]:
    stmt:str="SELECT * FROM creature"
    curs.execute(stmt)
    rows=list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def get_one(name) -> Creature:
    stmt:str="SELECT * FROM creature WHERE name=:name"
    curs.execute(stmt, {"name":name})
    row=curs.fetchone()
    if not row:
        raise Missing(msg=f"Creature {name} not found")
    return row_to_model(row)

def create(creature:Creature) -> Creature:
    stmt:str="INSERT INTO creature VALUES (:name, :country, :description, :area, :aka)"
    try:
        curs.execute(stmt, model_to_dict(creature))
    except IntegrityError:
        raise Duplicate(f"Creature {creature.name} already exists")
    conn.commit()
    return get_one(creature.name)

def modify(creature:Creature) -> Creature:
    stmt:str="""
    UPDATE creature
    SET name=:name,
      country=:country,
      description=:description,
      area=:area,
      aka=:aka WHERE name=:name_orig
    """
    params=model_to_dict(creature)
    params["name_orig"]=creature.name
    curs.execute(stmt,params)
    if curs.rowcount!=1:
        raise Missing(msg=f"Creature {creature.name} not found")
    conn.commit()
    return get_one(creature.name)

def replace(creature:Creature) -> Creature:
    return creature

def delete(creature:Creature):
    stmt="DELETE FROM creature WHERE name=:name"
    res=curs.execute(stmt, {"name":creature.name})
    if curs.rowcount!=1:
        raise Missing(msg=f"Creature {creature.name} not found")

    conn.commit()
    return bool(res)


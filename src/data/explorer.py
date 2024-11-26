from sqlite3 import IntegrityError
from typing import Any
from model.explorer import Explorer
from . import curs, conn
from errors import Missing, Duplicate

def init() -> None:
    curs.execute(
        """CREATE TABLE  IF NOT EXISTS explorer
        (name text primary key,
         country text,
         description text
         )
        """
        )
init()

def row_to_model(row:tuple) -> Explorer:
    name, country, description=row
    return Explorer(name=name, country=country, description=description)

def model_to_dict(explorer:Explorer) -> dict[str, Any]:
    return explorer.model_dump()

def get_all() -> list[Explorer]:
    stmt:str="SELECT * FROM explorer"
    curs.execute(stmt)
    rows=list(curs.fetchall())
    return [row_to_model(row) for row in rows]

def get_one(name) -> Explorer:
    stmt:str="SELECT * FROM explorer WHERE name=:name"
    curs.execute(stmt, {"name":name})
    row=curs.fetchone()
    if not row:
        raise Missing(msg=f"Explorer {name} not found")
    return row_to_model(row)

def create(explorer:Explorer) -> Explorer:
    stmt:str="INSERT INTO explorer VALUES (:name, :country, :description)"
    try:
        curs.execute(stmt, model_to_dict(explorer))
    except IntegrityError:
        raise Duplicate(msg=f"Explorer {explorer.name} already exists")
    conn.commit()
    return get_one(explorer.name)

def modify(explorer:Explorer) -> Explorer:
    stmt:str="""
    UPDATE explorer
    SET name=:name,
      country=:country,
      description=:description
      WHERE name=:name_orig
    """
    params=model_to_dict(explorer)
    params["name_orig"]=explorer.name
    curs.execute(stmt,params)
    if curs.rowcount!=1:
        raise Missing(msg=f"Explorer {explorer.name} not found")
    conn.commit()
    return get_one(explorer.name)

def replace(explorer:Explorer) -> Explorer:
    return explorer

def delete(explorer:Explorer):
    stmt="DELETE FROM explorer WHERE name=:name"
    res=curs.execute(stmt, {"name":explorer.name})
    if curs.rowcount!=1:
        raise Missing(msg=f"Explorer {explorer.name} not found")
    conn.commit()
    return bool(res)

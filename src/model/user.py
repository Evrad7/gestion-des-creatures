from pydantic import BaseModel, Field

class User(BaseModel):
    name:str

class InnerUser(User):
    hash:str

class CreateUser(User):
    password:str=Field(min_length=1)

    class Config:
        schema_extra={
            "examples":[
                {
                    "user":"user",
                    "password":"password",
                }
            ]
        }




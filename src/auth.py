import uvicorn
from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


app=FastAPI()
basic=HTTPBasic()

secret_user="evrad7"
secret_password="password"

@app.get("/who")
def get_user(cred:Annotated[HTTPBasicCredentials, Depends(basic)]):
    if(cred.username==secret_user and cred.password==secret_password):
        return {"username":cred.username, "password":cred.password}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
if __name__=="__main__":
    uvicorn.run("auth:app", reload=True)
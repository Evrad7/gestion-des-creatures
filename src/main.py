import uvicorn
from typing import Literal, Annotated
from fastapi import FastAPI, File, UploadFile
from web import explorer, creature, user
from fastapi.staticfiles import StaticFiles




app=FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)
app.include_router(user.router)

@app.get("/")
def top() -> Literal['top here']:
    return "top here"

@app.post("/small")
async  def upload_small_file(small_file:Annotated[bytes, File()]):
    return f"file_size: {len(small_file)}"

app.mount("/static", StaticFiles(directory="static", html=True))


if __name__=="__main__":
    uvicorn.run("main:app", reload=True)
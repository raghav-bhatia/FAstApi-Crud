from fastapi import FastAPI
from pydantic import BaseModel

class EDeatails(BaseModel):
    name:str
    eid:str
    address:str

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/data/{eid}")
def empDetail(eid:int):
    return {'eid':eid}



@app.post("/ED")
def empDetail(Detaiis:EDeatails):
    return Detaiis
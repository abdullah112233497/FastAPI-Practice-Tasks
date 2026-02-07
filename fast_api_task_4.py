from fastapi import FastAPI
from pydantic import BaseModel
class Data(BaseModel):
    name : str
    gpa : float
    grade: str

best=FastAPI()
@best.post("/dataPosted")
def data(dAtA: Data):
    return {f"Posted Data is: {dAtA}"}
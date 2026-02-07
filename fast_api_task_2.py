# Task no.2: Return Sq
from fastapi import FastAPI
app = FastAPI()
@app.get("/{number}")
def task1(number:int):
    return {f"the square of the {number} is {number*number} "}

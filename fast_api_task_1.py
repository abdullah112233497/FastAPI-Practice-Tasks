# Task no.1: Return Data
from fastapi import FastAPI
app = FastAPI()
@app.get("/{name}/{skill}")
def task1(name:str,skill:str):
    return {f"Name: {name},skill: {skill}"}

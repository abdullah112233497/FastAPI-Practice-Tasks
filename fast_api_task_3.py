# Task no.3: Return Sum of the Query param given numbers:
from fastapi import FastAPI
app = FastAPI()
@app.get("/home")
def task1(num1:int,num2:int):
    return {f"Number1 : {num1} + Number2: {num2}= {num1+num2}"}

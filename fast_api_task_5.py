from fastapi import FastAPI
app=FastAPI()
databaseFake=[
    {"id":1, "name":"Abdullah", "grade":"B"},
    {"id":2, "name":"Rehan", "grade":"A-"},
    {"id":2, "name":"Sami", "grade":"F"}
]
@app.put("/putapi/{id}/{g}")
def updating(id: int, g:str):
    for i in databaseFake:
        if i["id"]==id:
            i["grade"]=g
            return {"Status: Update the Record successfully."}
        else:
            return{"Status: Request Failed."}
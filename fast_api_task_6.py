from fastapi import FastAPI
app=FastAPI()
databaseFake=[
    {"id":1, "name":"Abdullah", "grade":"B"},
    {"id":2, "name":"Rehan", "grade":"A-"},
    {"id":2, "name":"Sami", "grade":"F"}
]
@app.delete("/delapi/{id}")
def updating(id: int):
    for i in databaseFake:
        if i["id"]==id:
            databaseFake.remove(i)
            return {"Status: Delete the Record successfully."}
        else:
            return {"Status: Request Failed."}
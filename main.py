from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


TODOOS=[
    {"id":1,"task":"do laundry","is_complete":False},
    {"id":2,"task":"buy groceries","is_complete":True},
    {"id":3,"task":"clean room","is_complete":False}
]
    

@app.get("/")
def root():
    return{"message":"hello world"}


@app.get('/products/{id}')
def get_product(id:int):
    products=["toothbrush","laptop","mouse","keyboard"]
    return products[id]

@app.get("/todos/all")
def get_all_todos():
    return TODOOS


@app.get("/todos/{id}")
def get_todo_id(id:int):
    return TODOOS[id]




@app.post("/todos/create")
def append_todo(new_todo):
    TODOOS.append(new_todo)
    return "success"

@app.put("/todos/update")
def update_todo(existing_todo=Body()):
    TODOOS[0] = existing_todo
    return "success"

@app.delete("/todos/delete/{id}")
def delete_todo(id:int):
    TODOOS.pop(id)
    return "success"
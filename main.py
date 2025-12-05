from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float

# "Base de datos" temporal en memoria
items_db = {}

@app.get("/")
def root():
    return {"status": "Backend funcionando correctamente"}

@app.post("/items")
def create_item(item: Item):
    items_db[item.id] = item
    return item

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item no encontrado"}
    return items_db[item_id]

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items_db:
        return {"error": "Item no encontrado"}
    del items_db[item_id]
    return {"status": "Item eliminado"}

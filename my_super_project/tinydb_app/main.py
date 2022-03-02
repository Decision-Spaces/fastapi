from typing import List
from tinydb import TinyDB, Query
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

db = TinyDB('db.json')

# Add user
@app.post("/users/{user_id}")
def read_item(user_id: int):
    db.insert({"user_id": user_id})
    return {"user_id": user_id}

# Fetch user
@app.get("/users/{user_id}")
def read_item(user_id: int):
    User = Query()
    db.search(User['user_id'] == user_id)
    return {"user_id": user_id}

# Add item (for user)
@app.post("/users/{user_id}/items/")
def read_item(user_id: int):
    table = db.table('items')
    table.insert({"user_id": user_id,'value': True})
    return {"user_id": user_id,'value': True}

# Get items (for user)
@app.get("/users/{user_id}/items/")
def read_item(user_id: int):
    Item = Query()
    table = db.table('items')
    table.search(Item['user_id'] == user_id)
    return {"user_id": user_id}
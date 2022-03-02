from typing import List
from tinydb import TinyDB, Query
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

db = TinyDB('db.json')


@app.post("/users/{user_id}")
def read_item(user_id: int):
    db.insert({"user_id": user_id})
    return {"user_id": user_id}

@app.get("/users/{user_id}")
def read_item(user_id: int):
    User = Query()
    db.search(User['user_id'] == user_id)
    return {"user_id": user_id}


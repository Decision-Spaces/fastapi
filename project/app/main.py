from typing import List
from tinydb import TinyDB, Query
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

db = TinyDB('db.json')

templates = Jinja2Templates(directory="templates")

# Add space
@app.post("/spaces/{user_id}")
def read_item(space_id: int):
    db.insert({"space_id": space_id})
    return {"space_id": space_id}

# Fetch space
@app.get("/spaces/{space_id}")
def read_item(space_id: int):
    Space = Query()
    return db.search(Space['space_id'] == space_id)

# Add decision (for space)
@app.post("/spaces/{space_id}/decisions/")
def read_item(space_id: int):
    table = db.table('decisions')
    table.insert({"space_id": space_id,'value': True})
    return {"space_id": space_id,'value': True}

# Get decisions (for space)
@app.get("/decisions/{space_id}")
def read_item(space_id: int):
    Decision = Query()
    table = db.table('decisions')
    return table.search(Decision['space_id'] == space_id)

# Form for New Decision
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/addDecision", response_class=HTMLResponse)
async def home(request: Request):
    data = openfile("home.md")
    return templates.TemplateResponse("addDecision.html", {"request": request, "data": data})

from fastapi import FastAPI 
from datetime import datetime
from pydantic import BaseModel



class TodoBase(BaseModel):
    date: datetime
    title: str
    context: str

class TodoCreate(TodoBase):
    todo_id: int
    user_id: int

class TodoDelete(TodoCreate):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoGet(TodoCreate):
    pass


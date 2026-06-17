from pydantic import BaseModel
from typing import List, Optional

class TodoCreate(BaseModel):
    title : str


class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
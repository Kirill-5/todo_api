from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str
    id: int
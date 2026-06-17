from pydantic import BaseModel
from typing import List, Optional

class TokenAccess(BaseModel):
    access_token: str
    token_type: str
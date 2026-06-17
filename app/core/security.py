from authx import AuthX, AuthXConfig
from fastapi import Depends, HTTPException

from app.models.user import User

config = AuthXConfig()
config.JWT_SECRET_KEY = "your-secret-key"
config.JWT_TOKEN_LOCATION = ["headers"]
config.JWT_HEADER_NAME = "Authorization"
config.JWT_ACCESS_TOKEN_EXPIRES = None

security = AuthX(config=config)


def get_current_user(payload = Depends(security.access_token_required)):
    username = payload.sub
    if not username:
        raise HTTPException(status_code=404, detail="Invalid token")
    return username
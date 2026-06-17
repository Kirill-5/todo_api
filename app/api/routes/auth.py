from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.schemas.token import TokenAccess
from app.core.security import security, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User is already registered")

    new_user = User(username=user.username, password=user.password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return UserResponse(
        username=new_user.username,
        id=new_user.id,
    )



@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    if db_user.password != user.password:
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = security.create_access_token(
        uid=user.username
        )
    return {"access_token": token , "token_type": "bearer"}
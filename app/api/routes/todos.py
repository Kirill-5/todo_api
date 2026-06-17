from fastapi import APIRouter, Depends, HTTPException
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoResponse, TodoUpdate
from app.schemas.token import TokenAccess
from app.core.security import security, get_current_user


router = APIRouter(prefix="/todos", tags=["todos"])


@router.get("/", response_model=list[TodoResponse])
def get_todos(user = Depends(get_current_user), db: Session = Depends(get_db)):
    username = user
    current_user = db.query(User).filter(User.username == user).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    user_todos = db.query(Todo).filter(Todo.user_id == current_user.id).all()
    return user_todos



@router.post("/", response_model=TodoResponse)
def create_todo(
    payload: TodoCreate,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    username = user
    current_user = db.query(User).filter(User.username == username).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_todo = Todo(
        user_id = current_user.id,
        title=payload.title,
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return TodoResponse(
        id = new_todo.id,
        title = new_todo.title,
        completed = new_todo.completed,
    )


@router.delete("/{id}")
def delete_todo(id : int, user = Depends(get_current_user), db: Session = Depends(get_db)):
    username = user
    current_user = db.query(User).filter(User.username == username).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    todo= db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404 , detail="Not found")

    if todo.user_id != current_user.id:
        raise HTTPException(status_code=403 , detail="Not yours")

    db.delete(todo)
    db.commit()

    return {"message" : "deleted"}


@router.patch("/{id}", response_model=TodoResponse)
def update_todo(
    payload: TodoUpdate,
    id: int,
    user = Depends(get_current_user),
    db: Session = Depends(get_db)
    ):

    username = user
    current_user = db.query(User).filter(User.username == username).first()
    if not current_user:
        raise HTTPException(status_code=404, detail="User not found")

    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Not found")

    if todo.user_id != current_user.id:
        raise HTTPException(status_code=403 , detail="Not yours")

    if payload.title is not None:
        todo.title = payload.title

    if payload.completed is not None:
        todo.completed = payload.completed

    db.commit()
    db.refresh(todo)

    return TodoResponse(
        id=todo.id,
        title=todo.title,
        completed=todo.completed,
    )
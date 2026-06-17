from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean


# Таблица пользователя
class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    completed =  Column(Boolean, default=False)
    user_id = Column(ForeignKey("users.id"))
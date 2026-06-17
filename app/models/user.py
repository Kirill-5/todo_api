from app.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

# Таблица пользователя
class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

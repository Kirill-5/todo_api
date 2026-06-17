from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.api.routes import auth, todos
from app.db.database import engine, Base
from app.models import user, todo


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Todo list",
    swagger_ui_parameters={"persistAuthorization": True}
)

security_scheme = HTTPBearer()


app.include_router(auth.router)
app.include_router(todos.router)
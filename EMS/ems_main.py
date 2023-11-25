from fastapi import FastAPI
from .database import engine
from .import models
from .routers import employee,employee_login,authentication

app=FastAPI()


models.Base.metadata.create_all(bind=engine)

app.include_router(authentication.router)
app.include_router(employee.router)
app.include_router(employee_login.router)




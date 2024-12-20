"""run fastAPI"""
from fastAPI.routes import routes
from fastapi import FastAPI

app = FastAPI()

app.include_router(routes.endPoints)

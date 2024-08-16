from fastapi import FastAPI
from routes.routes import endPoint

app = FastAPI()

app.include_router(endPoint)
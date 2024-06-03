import uvicorn
from fastapi import FastAPI

from app.core import models
from app.api_v1 import router as api_v1_router
from app.core.database import engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(router=api_v1_router, prefix="/api_v1")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)

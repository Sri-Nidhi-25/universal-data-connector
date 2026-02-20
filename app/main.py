
from fastapi import FastAPI
from app.routers import health, data
from app.utils.logging import configure_logging
from app.routers import chat
configure_logging()

app = FastAPI(title="Universal Data Connector")

@app.get("/")
def root():
    return {"message": "Universal Data Connector API is running"}

app.include_router(health.router)
app.include_router(data.router)
app.include_router(chat.router)

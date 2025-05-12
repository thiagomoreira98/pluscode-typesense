from fastapi import FastAPI
from app.core.routes import router
from app.config import init

app = FastAPI(
    title="Pluscode API",
    description="Pluscode API",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    init()

app.include_router(router)


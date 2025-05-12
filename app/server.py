from fastapi import FastAPI
from app.routes import router
from app.seed import generate_products

app = FastAPI(
    title="Pluscode API",
    description="Pluscode API",
    version="1.0.0",
)

@app.on_event("startup")
def on_startup():
    generate_products(100000)

app.include_router(router)


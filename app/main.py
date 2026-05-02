from fastapi import FastAPI
from app.routes import health, events

app = FastAPI(title="DynamicOS API")

app.include_router(health.router, prefix="/api/v1")
app.include_router(events.router, prefix="/api/v1")

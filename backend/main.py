from fastapi import FastAPI
from backend.health import router as health_router


app = FastAPI()

app.include_router(health_router)













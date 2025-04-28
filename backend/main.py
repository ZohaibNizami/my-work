from fastapi import FastAPI
from backend.health import router as health_router



app = FastAPI()

# Include the health check router
app.include_router(health_router)


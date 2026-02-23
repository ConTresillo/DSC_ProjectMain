from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI()

# 1️⃣ Register API first
app.include_router(router, prefix="/api/v1")

# 2️⃣ THEN mount static
app.mount("/", StaticFiles(directory="static", html=True), name="static")
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import init_db
from app.api.routes import router


# Create FastAPI application
app = FastAPI(
    title="Astra Document Intelligence",
    version="1.0.0",
)


# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize database
@app.on_event("startup")
def startup():
    init_db()


# API routes
app.include_router(router)


# Basic root endpoint
@app.get("/")
def root():
    return {
        "message": "Astra Document Intelligence API is running"
    }

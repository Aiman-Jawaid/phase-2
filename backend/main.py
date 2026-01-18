from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Validate required environment variables
def validate_environment():
    required_vars = ["BETTER_AUTH_SECRET", "DATABASE_URL"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

validate_environment()

# Import models and create database tables
from models import Task
from db import engine
from sqlmodel import SQLModel

# Import exception handlers
from utils.exception_handlers import (
    http_exception_handler,
    validation_exception_handler,
    general_exception_handler
)
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

# Create database tables on startup
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create FastAPI app instance
app = FastAPI(
    title="Todo API",
    description="Secure Todo Management Backend with JWT Authentication",
    version="1.0.0"
)

# Add CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", "Authorization", "Content-Type"],  # Allow all headers plus auth and content-type
)

# Register custom exception handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Todo API - Secure Todo Management Backend"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-backend"}

# Include routes after app is initialized
from routes import tasks, auth
app.include_router(tasks.router, prefix="/api", tags=["tasks"])
app.include_router(auth.router, prefix="/api", tags=["auth"])
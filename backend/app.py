import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from main import app

# The main FastAPI app is already defined in main.py
# We're just ensuring it's properly configured for Hugging Face Spaces

# Add CORS middleware to handle requests from different origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Optionally add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "todo-backend"}

# The app is now ready to be served by Hugging Face Spaces
# Hugging Face will automatically detect and serve the FastAPI app
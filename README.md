# Todo Application

This is a full-stack Todo application with a React/Next.js frontend and a FastAPI backend.

## Deployment Instructions

### Frontend (Deployed on Vercel)
The frontend is deployed on Vercel at: https://frontend-ert2jakw6-aimans-projects-3ae3674b.vercel.app

### Backend (To be deployed on Hugging Face)
The backend can be deployed on Hugging Face Spaces using the following steps:

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a new Space on Hugging Face at https://huggingface.co/new-space

3. Select the "Docker" SDK and "CPU" hardware

4. Add the following files to your repository:
   - main.py (contains the FastAPI application)
   - requirements.txt (dependencies)
   - Dockerfile (deployment configuration)
   - app.py (entry point)
   - run_app.py (startup script)
   - README.md (with Hugging Face metadata)

5. In the Space settings, add the following secrets:
   - BETTER_AUTH_SECRET: Your JWT secret
   - DATABASE_URL: Your PostgreSQL connection string

6. The API will be available at your Space URL.

## Architecture

- **Frontend**: Next.js 14.x application with TypeScript
- **Backend**: FastAPI application with SQLModel and PostgreSQL
- **Authentication**: JWT-based authentication
- **Deployment**: Frontend on Vercel, Backend on Hugging Face Spaces

## Features

- User authentication and authorization
- Task management (CRUD operations)
- Responsive UI
- Secure API endpoints
# Todo Application

This is a full-stack Todo application with a React/Next.js frontend and a FastAPI backend.

## Deployment Instructions

### Frontend (Deployed on Vercel)
The frontend is deployed on Vercel at: https://frontend-ert2jakw6-aimans-projects-3ae3674b.vercel.app

### Backend (To be deployed on Hugging Face)
The backend can be deployed on Hugging Face Spaces using either of the following methods:

#### Method 1: Dedicated Repository (Recommended)
1. Create a new GitHub repository containing only the backend code
2. Copy the contents of the `backend/` directory to the root of the new repository
3. Create the Space on Hugging Face and link the new repository

#### Method 2: Subdirectory
1. Create a new Space on Hugging Face at https://huggingface.co/new-space
2. Select the "Docker" SDK and "CPU" hardware
3. When prompted for the repository, link your GitHub repository: `https://github.com/Aiman-Jawaid/phase-2.git`
4. In the Space settings, specify the working directory as `backend`
5. The Space will use the Dockerfile in the backend directory

#### Required Environment Variables
In the Space settings, add the following secrets:
- `BETTER_AUTH_SECRET`: Your JWT secret
- `DATABASE_URL`: Your PostgreSQL connection string

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
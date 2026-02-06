---
title: Todo API Backend
emoji: 🚀
colorFrom: blue
colorTo: yellow
sdk: docker
app_file: run_app.py
---

# Todo API Backend

Secure Todo Management Backend with JWT Authentication built using FastAPI and SQLModel.

## Features

- JWT-based authentication and authorization
- User-isolated task management
- Full CRUD operations for tasks
- Filtering by task status (pending, completed)
- Data validation and error handling
- Secure API endpoints

## Tech Stack

- **Framework**: FastAPI
- **Database**: PostgreSQL (via SQLModel)
- **Authentication**: JWT tokens with python-jose
- **ORM**: SQLModel (combines Pydantic and SQLAlchemy)

## Running the Application

The API is deployed on Hugging Face Spaces and will be available at the space URL.

API documentation is available at `/docs`.

## API Endpoints

### Authentication

All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <JWT_TOKEN>
```

### Tasks

- `GET /api/tasks` - Get all tasks for the authenticated user
  - Query parameters: `status` (all, pending, completed)
- `POST /api/tasks` - Create a new task
- `GET /api/tasks/{id}` - Get a specific task
- `PUT /api/tasks/{id}` - Update a task
- `PATCH /api/tasks/{id}/complete` - Toggle task completion status
- `DELETE /api/tasks/{id}` - Delete a task

## Security

- All API endpoints require JWT authentication
- Users can only access their own tasks
- Input validation is performed on all endpoints
- Proper error handling without sensitive information disclosure
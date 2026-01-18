# Todo Full-Stack Web Application Constitution

## Core Principles

### Full-Stack Specification Adherence
All implementations must strictly follow the specifications defined in the /specs/ directory. Frontend components must align with UI specs, backend APIs must conform to REST endpoint specs, and database models must match schema definitions. No implementation should deviate from the documented specs without explicit updates to the corresponding spec files.

### Authentication-First Security
Security is paramount - every API endpoint must validate JWT tokens before processing requests. User data isolation is non-negotiable: users can only access and modify their own tasks. All authentication flows must utilize Better Auth with proper JWT handling. No endpoint should be accessible without proper authentication unless explicitly defined as public.

### Test-First Implementation (NON-NEGOTIABLE)
TDD is mandatory: Tests must be written before implementation code. Unit tests for individual functions, integration tests for API endpoints, and end-to-end tests for critical user flows must be implemented. All tests must pass before merging. The Red-Green-Refactor cycle is strictly enforced for all feature development.

### Type-Safe Development
All code must be strongly typed using TypeScript for frontend and proper type hints in Python for backend. API contracts must be validated using Pydantic models. No implicit any types in TypeScript, and all API responses must have proper typing. Type checking must pass before code can be merged.

### Minimalist Feature Development
Features should be implemented with the minimal viable approach that satisfies requirements. Avoid over-engineering or adding speculative functionality. Each feature must have clear business value and be testable. Follow YAGNI (You Aren't Gonna Need It) principles and prefer simple solutions over complex abstractions.

### API Contract Compliance
All backend endpoints must follow RESTful conventions and properly implement CRUD operations for tasks. Request/response schemas must match the defined API specifications. Proper HTTP status codes must be returned for all responses. Filtering, sorting, and pagination must be implemented where specified.

## Security Requirements
All data transmission must use HTTPS. JWT tokens must be properly secured and have appropriate expiration times. SQL injection prevention through parameterized queries is mandatory. Input validation must be implemented at all API boundaries. Sensitive data should never be exposed in client-side code or logs.

## Development Workflow
All development must follow the spec-driven approach: read relevant specs before implementing (@specs/features/task-crud.md, @specs/features/authentication.md, etc.). Use Next.js App Router patterns for frontend, FastAPI conventions for backend, and SQLModel for database interactions. All API calls must be made through the centralized API client at /lib/api.ts. Code reviews must verify compliance with all constitution principles.

## Governance
This constitution governs all development activities for the Todo Full-Stack Web Application. All team members must comply with these principles. Amendments require explicit documentation and team approval. Code reviews must verify compliance with all principles before merging. Each pull request must demonstrate adherence to these guidelines.

**Version**: 1.0.0 | **Ratified**: 2026-01-09 | **Last Amended**: 2026-01-09

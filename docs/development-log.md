# TinyScholar Development Log

A chronological record of development progress, decisions, and lessons learned.

---

## 2026-07-12

### Phase 1 – FastAPI Foundations

#### Completed

- Initialized FastAPI backend.
- Added root endpoint.
- Added health endpoint.
- Configured automatic Swagger/OpenAPI documentation.

#### Child Module (In-Memory)

The first domain module was intentionally implemented without a database. This keeps the focus on learning FastAPI and API design before introducing persistence.

| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | `/children` | Create a child profile |
| GET | `/children` | List all children |
| GET | `/children/{id}` | Retrieve a child by ID |

#### Concepts Learned

- FastAPI routing
- Pydantic models
- Model inheritance
- Request vs Response models
- Path parameters
- Response models
- HTTP status codes
- HTTPException
- In-memory data storage

#### Testing

Every endpoint was manually tested through Swagger UI before committing.

#### Upcoming Milestones

- Update child endpoint
- Delete child endpoint
- Refactor into routers
- Introduce PostgreSQL
- Authentication

#### Engineering Decisions

- Started with in-memory storage instead of a database to focus on API design.
- Used separate request (`ChildCreate`) and response (`Child`) models.
- Used HTTP status codes following REST conventions.
- Tested every endpoint before committing.

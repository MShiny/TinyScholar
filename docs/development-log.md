# TinyScholar Development Log

A chronological record of development progress, decisions, and lessons learned.

---

## 2026-07-12

### Phase 1 – FastAPI Foundations

#### Completed

* Initialized FastAPI backend.
* Added root endpoint.
* Added health endpoint.
* Configured automatic Swagger/OpenAPI documentation.

#### Child Module (In-Memory)

The first domain module was intentionally implemented without a database. This keeps the focus on learning FastAPI and API design before introducing persistence.

| Method | Endpoint         | Purpose                |
| ------ | ---------------- | ---------------------- |
| POST   | `/children`      | Create a child profile |
| GET    | `/children`      | List all children      |
| GET    | `/children/{id}` | Retrieve a child by ID |

#### Concepts Learned

* FastAPI routing
* Pydantic models
* Model inheritance
* Request vs Response models
* Path parameters
* Response models
* HTTP status codes
* HTTPException
* In-memory data storage

#### Testing

Every endpoint was manually tested through Swagger UI before committing.

#### Engineering Decisions

* Started with in-memory storage instead of a database to focus on API design.
* Used separate request (`ChildCreate`) and response (`Child`) models.
* Used HTTP status codes following REST conventions.
* Tested every endpoint before committing.

---

## 2026-07-16

### Child Module Enhancements

#### Completed

* Added `PATCH /children/{id}` endpoint.
* Added `DELETE /children/{id}` endpoint.
* Completed Create, Read, Update, and Delete (CRUD) operations for the in-memory Child API.

#### Concepts Learned

* Partial updates with PATCH.
* `ChildUpdate` model.
* `model_dump(exclude_unset=True)`.
* `model_copy(update=...)`.
* HTTP 204 No Content.
* Deleting items from an in-memory list.

#### Testing

All new endpoints were manually tested through Swagger UI.

* Verified partial updates.
* Verified validation errors.
* Verified 404 responses for non-existent child IDs.
* Verified successful deletion.
* Verified deleted children could no longer be retrieved.

#### Engineering Decisions

* Used PATCH instead of PUT because only the supplied fields should be updated.
* Introduced a dedicated `ChildUpdate` model instead of reusing `ChildCreate`.
* Used `model_dump(exclude_unset=True)` together with `model_copy(update=...)` to implement clean partial updates.
* Returned HTTP 204 No Content for successful DELETE operations to follow REST conventions.

---

## 2026-07-18

### Project Refactoring

#### Completed

* Refactored the Child module using `APIRouter`.
* Moved all child endpoints from `main.py` to `routers/children.py`.
* Registered the router using `app.include_router()`.
* Introduced a `routers` package for organizing API modules.

#### Concepts Learned

* APIRouter
* Router prefixes
* Router-level tags
* `app.include_router()`
* Decorator factories
* Functions as first-class objects
* * Route registration vs request handling

#### Testing

All endpoints were manually tested through Swagger UI after the refactor.

* Verified all CRUD endpoints remained functional.
* Verified route registration after moving endpoints into the router.
* Verified application startup after the refactor.

#### Engineering Decisions

* Moved child-related endpoints into a dedicated router to improve project organization.
* Used `prefix="/children"` to avoid repeating the base path across endpoints.
* Defined router-level tags instead of repeating tags for every endpoint.
* Kept `main.py` focused on application initialization and router registration.
* Preserved the existing API contract while improving the internal project structure.

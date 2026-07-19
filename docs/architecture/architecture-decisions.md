# Architecture Decisions

This is a quick-reference decision log, not an ADR collection.

## Accepted decisions

- FastAPI is the backend.
- PostgreSQL is the relational database and source of truth.
- SQLAlchemy 2.x is the ORM and Alembic manages database migrations.
- PostgreSQL with pgvector provides vector storage; a separate vector database is not introduced now.
- S3-compatible object storage is planned for production file storage.
- Authentication uses access tokens and refresh tokens.
- Redis is deferred until background jobs, caching, or rate limiting justifies it.
- Every login identity is a `User`.
- A `Family` is a shared workspace; users belong through `FamilyMembership`.
- Children have independent login identities and separate `ChildProfile` educational profiles.
- Shared resources belong to a family and require explicit child assignment.
- RAG retrieval enforces normal application authorization.

## Pending decisions

The unresolved product choices are maintained in [open product decisions](open-decisions.md), including parent invitations, child credential modes, multi-family membership, ownership transfer, account recovery, family-wide visibility, session lifetimes, retention, audit scope, and the learning model.

See the [system overview](system-overview.md) for the complete technology context.

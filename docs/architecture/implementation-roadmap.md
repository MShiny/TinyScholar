# Implementation Roadmap

The phases below sequence the confirmed architecture without treating later-phase choices as implemented features.

## Phase 1 — Foundation

**Objective:** Establish durable application persistence and database conventions.

**Main deliverables:** PostgreSQL configuration, SQLAlchemy 2.x, Alembic, base model conventions, database session management, and initial migrations.

**Important risks:** Migration discipline, environment configuration, and avoiding premature schema complexity.

**Exit criteria:** The application can create and migrate a PostgreSQL schema through repeatable migrations and use managed database sessions.

## Phase 2 — Identity and family

**Objective:** Establish independent identities, family membership, and secure sessions.

**Main deliverables:** `User`, `Family`, `FamilyMembership`, and `ChildProfile`; parent registration and login; child account creation and independent child login; password and PIN hashing; access and refresh tokens; role and family authorization; credential reset and session revocation.

**Important risks:** Incorrect cross-family authorization, insecure credential handling, and incomplete multi-record transaction handling.

**Exit criteria:** Parents and children can authenticate independently, and all protected family and child access is enforced through validated membership and role checks.

## Phase 3 — Shared-parent access

**Objective:** Safely support multiple parents in a shared `Family`.

**Main deliverables:** Parent invitations and acceptance, parent membership management, role-management rules, and parent-removal and account-deactivation rules.

**Important risks:** Invitation abuse, unclear role transitions, and accidental loss of family administration.

**Exit criteria:** An authorized adult can join a family through an invitation and all membership changes are authorized, auditable, and preserve a valid administration path.

## Phase 4 — Documents

**Objective:** Support family-owned learning materials with child-specific access.

**Main deliverables:** Object-storage abstraction, file upload, document metadata, document assignments, processing status, file validation, and deletion and cleanup rules.

**Important risks:** Inconsistent object-storage and database state, unsafe file handling, and assignment authorization failures.

**Exit criteria:** Authorized parents can manage documents and assignments, while children can access only their assigned, ready, non-deleted material.

## Phase 5 — RAG

**Objective:** Provide grounded answers from authorized learning material.

**Main deliverables:** Text extraction, chunking, embeddings, pgvector, access-filtered retrieval, LLM-generated grounded answers, processing retries, and background jobs when justified.

**Important risks:** Retrieval authorization failures, ungrounded answers, processing duplication, and operational complexity introduced too early.

**Exit criteria:** A child can receive a grounded answer only from permitted ready documents, with retrieval filters enforced in the PostgreSQL query.

## Phase 6 — Learning features

**Objective:** Deliver child-specific learning activities and parent visibility.

**Main deliverables:** Lessons, quizzes, questions, attempts, progress tracking, recommendations, and parent reporting.

**Important risks:** Mixing sibling progress, unreliable AI-generated learning content, and over-designing recommendation logic before product evidence exists.

**Exit criteria:** Children can complete authorized activities and see their own progress; parents can view authorized child progress and reports.

See [architecture decisions](architecture-decisions.md) and [open product decisions](open-decisions.md).

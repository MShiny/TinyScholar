# Proposed API Boundaries

The following endpoint groups are proposed organizational boundaries, not final API contracts. Names, public identifiers, request schemas, and exact operations may change during implementation.

## `/auth`

Establishes and manages independent user sessions. Proposed operations include parent registration, parent login, child login, refresh-token exchange, logout, and credential reset.

## `/families`

Provides the current family's workspace view and settings. Proposed operations include viewing the current family and updating family settings.

## `/family-memberships`

Manages `FamilyMembership` association and roles. Proposed operations include listing members, managing roles, and deactivating a membership.

## `/children`

Manages the lifecycle of child `User` accounts and associated `ChildProfile` records. Proposed operations include creating a child account, viewing a child profile, updating educational information, deactivating a child account, and resetting a child credential.

## `/invitations`

Manages the planned family invitation lifecycle. Proposed operations include creating, inspecting, accepting, and revoking an invitation.

## `/documents`

Manages the upload, processing, assignment, retrieval, and lifecycle of family-owned learning documents. Proposed operations include upload, list, assignment to a child, assignment removal, processing-status view, retrieval, and deletion.

## `/lessons`

Manages child-specific lessons. Proposed operations include creation, listing lessons for a child, viewing a lesson, and recording completion.

## `/quizzes`

Manages child-specific quizzes and attempts. Proposed operations include creating a quiz, starting an attempt, submitting answers, and viewing a result.

## `/progress`

Exposes learning progress and analytics at the appropriate authorization scope. Proposed operations include a parent viewing an authorized child's progress and a child viewing their own progress.

## `/questions`

Provides grounded question answering for a child. The proposed operation accepts a child question and returns an answer retrieved only from content assigned to that child.

## Current child endpoint

The existing `children` router is a temporary FastAPI learning exercise. It provides unauthenticated in-memory CRUD at `POST`, `GET`, `PATCH`, and `DELETE /children` (with `GET /children/{id}` for individual records), using a process-local list and sequential integer IDs.

Its Pydantic validation, REST status handling, and router organization can remain useful learning exercises. It requires redesign before it can be a product API: it has no `User` or `ChildProfile` split, child login identity, `Family` ownership, database persistence, or authorization. It must not be treated as proof that the caller may access, modify, or delete any child record.

See [authorization](authorization.md), [identity and family](identity-and-family.md), and [system overview](system-overview.md).

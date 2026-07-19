# Identity and Family

This is the confirmed target data and access design. Its tables, endpoints, and migrations are a later implementation phase; the current in-memory child endpoint does not implement this design.

## User

Every person who can log in is represented by a `User`. Suggested fields are `id`, `name`, `username`, `email` (nullable for children), `credential_hash`, `account_type`, `is_active`, `authentication_mode`, `must_change_credential`, `created_at`, and `updated_at`. Initial account types are `parent` and `child`.

## Family

A `Family` is a shared household or workspace, with `id`, `name`, `created_by_user_id`, `created_at`, and `updated_at`. The first parent creates it, but no user conceptually owns another user: users belong to the family through membership.

## FamilyMembership

`FamilyMembership` associates a user with a family and records its authorization role. Suggested fields are `id`, `family_id`, `user_id`, `role`, `status`, and `joined_at`; initial roles are `owner`, `parent`, and `child`.

The second parent does not belong to the first parent. Both parents belong to the same family, and children also belong to it through membership. Membership represents both family association and the authorization role within that family.

The database must enforce a unique constraint on `(family_id, user_id)` to prevent duplicate membership. It should also index family and user lookups, and constrain `role` and `status` to supported values.

## First-parent registration flow

First-parent registration creates the `User`, `Family`, and an `owner` `FamilyMembership` in one database transaction. If any step fails, the transaction must roll back so no partial family or orphaned user is created.

## Additional-parent invitation flow

The preferred future flow is:

1. An owner or authorized parent sends an invitation.
2. The invitation is associated with the family.
3. The invited adult accepts it.
4. The adult creates their own credentials.
5. A `parent` membership is created.

Invitation implementation is a later phase. The planned `family_invitations` table has `id`, `family_id`, `email`, `role`, `token_hash`, `expires_at`, `accepted_at`, `invited_by_user_id`, and `created_at`. Invitation tokens must be stored only as hashes.

See [child profiles](child-profiles.md), [authorization](authorization.md), and the [database schema](database-schema.md).

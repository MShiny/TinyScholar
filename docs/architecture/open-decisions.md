# Open Product Decisions

- Whether a normal parent may invite another parent.
- Whether children use PINs, passwords, or age-dependent credentials.
- Whether one `User` may belong to multiple `Family` workspaces.
- How family ownership can be transferred while preserving administration and audit history.
- The child-account recovery workflow.
- Whether some documents may be family-wide rather than explicitly assigned.
- Exact access-token and refresh-token expiry durations.
- Soft-deletion and retention policies for users, memberships, documents, and learning records.
- The scope and retention of audit logs.
- The exact learning, scoring, progress, and recommendation model.
- Minimum permitted PIN length and failed-attempt policy.
- Whether switching from password mode to PIN mode requires additional parent confirmation.
- Whether a child may request a switch to independent authentication.
- Which detailed activity data is visible in the parent dashboard.

See [architecture decisions](architecture-decisions.md) and [implementation roadmap](implementation-roadmap.md).

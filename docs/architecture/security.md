# Security

## Security and integrity rules

- Enforce unique usernames and unique adult emails when present.
- Hash passwords, PINs, invitation tokens, and refresh tokens; store no plaintext secrets.
- Use expiring, revocable sessions and revoke child sessions after credential reset.
- Apply family-scoped authorization and child-scoped access checks to every protected resource.
- Derive ownership from validated identity and database relationships; never accept client-controlled ownership.
- Use transactions for multi-record operations, with database constraints and indexes to preserve integrity.
- Audit sensitive operations, including invitations, membership changes, credential resets, and child-account lifecycle actions.
- Validate the minimum age and treat child information and dates of birth as sensitive data.
- Avoid sensitive personal data in JWT claims.
- Introduce rate limiting later when a concrete requirement justifies it.
- Never store a PIN or password in plaintext.
- Do not expose whether a failed child login used an incorrect username, PIN, or password.
- Apply stricter rate limiting and failed-attempt protection to PIN authentication because the credential has lower entropy than a password.
- A parent may reset an independent account's password, but cannot retrieve the existing password.
- Switching authentication mode or resetting credentials must revoke all existing child sessions.
- Record authentication-mode changes and credential resets in the security audit log.

See [authentication and sessions](authentication-and-sessions.md), [authorization](authorization.md), and [open product decisions](open-decisions.md).

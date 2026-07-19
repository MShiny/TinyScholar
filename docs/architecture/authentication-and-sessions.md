# Authentication and Sessions

Credentials are never stored in plaintext. Parents authenticate using email or username and password. Each child authenticates using a unique username and either a PIN or password, according to the authentication mode selected by an authorized parent. PIN-based accounts are parent-managed; password-based accounts become child-managed after the child replaces the temporary password.

## Parent login

An active parent logs in with email or username plus password. Successful authentication establishes that parent as the current user and issues an access token and refresh token. Family access is then determined from current memberships, not from a client-supplied family identifier.

## Child login

An active child logs in using their username and the credential required by the account's authentication mode. A parent-managed account accepts the parent-set PIN. An independent account accepts the child-managed password. Successful authentication establishes the child as the current user and issues independent access and refresh tokens. The child's membership and resource assignments determine permitted learning access; no active parent session is required.

## Session architecture

Sessions use short-lived access tokens and revocable refresh tokens. The planned `refresh_tokens` table has `id`, `user_id`, `token_hash`, `expires_at`, `revoked_at`, `device_info` (nullable), and `created_at`. Raw access and refresh tokens are never stored in plaintext.

This design supports independent sessions, multiple devices, logout from one device, logout from all devices, credential-reset session revocation, and simultaneous child usage. For example, Child A can study on Device A while Child B studies on Device B; each has independent token pairs, and their learning records and progress remain separate.

Credential changes and resets revoke existing child sessions. Related account-creation and authentication-mode rules are in [child profiles](child-profiles.md); security controls are in [security](security.md).

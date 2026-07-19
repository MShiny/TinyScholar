# Child Profiles

## ChildProfile

A child is both a `User` with an independent login identity and a `ChildProfile` with educational information. The profile contains `id`, `user_id`, `date_of_birth`, `grade`, `school_board` (nullable), `preferred_language` (nullable), `learning_preferences` (nullable), `created_at`, and `updated_at`.

Authentication information remains in `User`; educational information remains in `ChildProfile`. `ChildProfile.user_id` must be unique, so each child user has at most one profile. Creation and updates must validate the product minimum age of 6 years.

## Child account creation flow

An authorized parent creates a child account in one transaction:

1. Create a `User` with `account_type` `child`.
2. Create a `FamilyMembership` with role `child`.
3. Create the `ChildProfile`.

During child-account creation, the authorized parent selects either parent-managed or independent authentication.

In parent-managed mode, the parent chooses a PIN and may use it to help the child sign in. The child is not required to replace the PIN after first login.

In independent mode, the system generates a temporary password. The child must replace it after first login, after which the parent does not know the child's active password. The parent continues to view learning progress and perform permitted management actions through the parent account.

Authentication mode is chosen by the parent and is not automatically determined by the child's age. An authorized parent may later switch the child between modes. Changing or resetting the credential revokes the child's existing sessions.

See [identity and family](identity-and-family.md), [authentication and sessions](authentication-and-sessions.md), and [authorization](authorization.md).

# Authorization

## Authorization rules

A validated token establishes the current user. The backend must never trust client-supplied `user_id`, `parent_id`, `child_id`, or `family_id` without validating membership and permissions.

- **Owner:** manage family settings; invite or remove parents; create and deactivate child accounts; reset child credentials; view all child progress.
- **Parent:** create child accounts; reset child credentials; upload and assign documents; create learning activities; view child progress, reports, completed lessons, activity history, and other parent-visible learning information through the parent account without authenticating as the child.
- **Child:** access only assigned material; attend lessons; ask questions; take quizzes; and view their own progress.

A parent may directly access a child's learning session only when the child uses parent-managed PIN authentication. For an independent password account, the parent must not be able to retrieve or view the child's current password.

Whether a normal parent can invite another parent remains a configurable product decision. A child cannot manage a family, invite users, access sibling progress, access another child's unassigned content, or reset another user's credentials.

## API authorization principles

The backend derives the current user from the validated token. Parent APIs operate only within validated `FamilyMembership`; child APIs operate only within the current `ChildProfile`. A child identifier in a URL is not authorization: resource ownership and permissions must be validated for every read and write.

Internal database IDs should not be exposed unnecessarily; public identifiers may be preferable when the public API is designed. Exact endpoint names and request schemas remain implementation decisions.

See [identity and family](identity-and-family.md), [documents and RAG](documents-and-rag.md), and [security](security.md).

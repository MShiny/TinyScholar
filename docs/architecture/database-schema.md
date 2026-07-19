# Database Schema

The following planned ER diagram is consistent with the [identity and family](identity-and-family.md) architecture. Document entities and their ER extension are in [documents and RAG](documents-and-rag.md).

## Mermaid ER diagram

```mermaid
erDiagram
    USERS {
        uuid id PK
        string username UK
        string email UK
        string account_type
        string authentication_mode
        boolean must_change_credential
    }
    FAMILIES {
        uuid id PK
        uuid created_by_user_id FK
        string name
    }
    FAMILY_MEMBERSHIPS {
        uuid id PK
        uuid family_id FK
        uuid user_id FK
        string role
        string status
    }
    CHILD_PROFILES {
        uuid id PK
        uuid user_id FK
        date date_of_birth
        string grade
    }
    REFRESH_TOKENS {
        uuid id PK
        uuid user_id FK
        string token_hash
        datetime expires_at
        datetime revoked_at
    }
    FAMILY_INVITATIONS {
        uuid id PK
        uuid family_id FK
        uuid invited_by_user_id FK
        string email
        string token_hash
        datetime expires_at
        datetime accepted_at
    }

    USERS ||--o{ FAMILY_MEMBERSHIPS : has
    FAMILIES ||--o{ FAMILY_MEMBERSHIPS : has
    USERS ||--o| CHILD_PROFILES : has
    USERS ||--o{ REFRESH_TOKENS : has
    USERS ||--o{ FAMILIES : creates
    FAMILIES ||--o{ FAMILY_INVITATIONS : has
    USERS ||--o{ FAMILY_INVITATIONS : sends
```

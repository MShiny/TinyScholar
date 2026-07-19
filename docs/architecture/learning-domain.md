# Learning Domain Architecture

The following entities describe the planned learning domain at a high level. They are not final schemas and should evolve with validated product requirements.

## Lessons

A `Lesson` is a child-specific learning activity. Suggested fields are `id`, `child_profile_id`, `document_id` (nullable), `title`, `content`, `generated_by_ai`, `created_by_user_id` (nullable), `created_at`, and `updated_at`.

`child_profile_id` owns the lesson activity. When a lesson originates from a source document, `document_id` preserves that traceability. `generated_by_ai` makes AI-generated content identifiable.

## Quizzes

A `Quiz` is a child-specific assessment, optionally connected to a lesson. Suggested fields are `id`, `child_profile_id`, `lesson_id` (nullable), `title`, `difficulty`, `generated_by_ai`, `created_at`, and `updated_at`.

## Quiz questions

`QuizQuestion` belongs to a quiz and has suggested fields `id`, `quiz_id`, `question_type`, `prompt`, `answer_data`, `explanation` (nullable), and `order_index`. `answer_data` may require a structured representation such as JSONB, but that is a later implementation decision.

## Quiz attempts

`QuizAttempt` records a child's submitted attempt and has suggested fields `id`, `quiz_id`, `child_profile_id`, `score`, `started_at`, and `completed_at`. An attempt always belongs to the child who submitted it, even where a quiz was created from shared family material.

## Progress records

`ProgressRecord` remains conceptual. Progress may eventually be derived from lessons, quiz attempts, completion records, and activity events instead of being stored as one large mutable field. Recommendation logic is intentionally not designed yet.

## Ownership rules

Child-specific activity and progress belong to `child_profile_id`. Shared resources, such as source documents, belong to the `Family` and must be explicitly assigned to children before child use. Quiz attempts and progress remain separate for siblings. AI-generated lessons and quizzes must be identifiable as generated content, and original source documents must remain traceable where applicable.

See [child profiles](child-profiles.md), [documents and RAG](documents-and-rag.md), and [authorization](authorization.md).

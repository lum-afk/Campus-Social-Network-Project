## **2.6 Data Model**

The implemented PoC stores a Python list of records containing only integer `post_id` and string `body`. IDs start at 1 and the list disappears when the process restarts. The relational model below is the proposed Assignment 2 design; no tables or migrations currently exist in the application.

### **2.6.1 Types and records**

PostgreSQL entity IDs use `BIGINT GENERATED ALWAYS AS IDENTITY` primary keys. Foreign keys use `BIGINT`; timestamps use `TIMESTAMPTZ` with UTC values; free text uses `TEXT`. Status and role values use `TEXT` with `CHECK` constraints. Fields are required unless marked nullable. Each main entity has `created_at`; mutable entities also have `updated_at`. API identifiers retain Section 2.4's names, such as `post_id`, rather than changing the PoC contract.

| Record | Principal fields and relationships |
| ----- | ----- |
| User (`users`) | `user_id`; unique normalized `email`; `password_hash`; nullable `verified_at`; `global_role` (student/moderator/admin); `status` (active/disabled) |
| Community | `community_id`; `created_by` → User; `name`; `visibility` (open/restricted); `is_official BOOLEAN` |
| Membership | Composite primary key (`community_id`, `user_id`), referencing Community and User; `role` (member/organizer); `status` (pending/approved/rejected) |
| Post | `post_id`; `author_id` → User; nullable `community_id` → Community; sanitized HTML `body`; `audience` (university/community); independent nullable `hidden_at` and `deleted_at` |
| Draft | `draft_id`; `community_id` → Community; `created_by` and `updated_by` → User; sanitized HTML `body`; positive `version INTEGER`; nullable unique `published_post_id` → Post; nullable `published_at` |
| Comment | `comment_id`; `post_id` → Post; `author_id` → User; plain-text `body`; independent nullable `hidden_at` and `deleted_at` |
| Like | Composite primary key (`post_id`, `user_id`), referencing Post and User; `created_at`; unlike removes the row |
| OfficialRequest | `request_id`; `community_id` → Community; `requested_by` → User; `reason`; `status` (pending/approved/rejected); nullable `reviewed_by` → User and `reviewed_at` |
| Report | `report_id`; `reporter_id` → User; exactly one of nullable `post_id` → Post or `comment_id` → Comment; `reason`; protected `evidence_body` snapshot of the reported content |
| Decision | `decision_id`; unique `report_id` → Report; `moderator_id` → User; `action` (dismiss/hide); `reason`; `decided_at` |
| Appeal | `appeal_id`; unique `decision_id` → Decision; `appellant_id` → User; `reason`; `status` (pending/escalated/resolved); nullable `reviewer_id` → User, `outcome` (upheld/reversed), `resolution_reason`, and `resolved_at` |
| AuditRecord | `audit_id`; `actor_id` → User; `action`; `target_type`; `target_id BIGINT`; `reason`; `occurred_at`; reference information for moderation and appeal events |

User global roles are separate from organizer roles held through Membership. `target_id` in AuditRecord is a historical reference selected by `target_type`, not a foreign key to several tables. C6 validates it when appending the record. Report's two concrete foreign keys preserve referential integrity for either supported target.

The API derives a report's `status` from whether a Decision exists, maps an appeal's `created_at` to `submitted_at`, and maps `resolution_reason` to the resolution request's `reason`. The report request's `target_type` and `target_id` select the corresponding concrete target foreign key.

The supporting records complete the authentication and retry design:

| Record | Fields and rules |
| ----- | ----- |
| Session | `session_id`; `user_id` → User; unique `token_hash`; `csrf_token_hash`; `created_at`, `last_seen_at`, `expires_at`; nullable `revoked_at`. Raw session tokens are not stored. |
| EmailVerification | `verification_id`; `user_id` → User; unique `token_hash`; `created_at`, `expires_at`; nullable `used_at`. Consuming a valid token and verifying the account occur in one transaction. Resending invalidates earlier outstanding tokens. |
| DraftSaveReceipt | Composite primary key (`draft_id`, `actor_id`, `request_id`), referencing Draft and User; `request_id VARCHAR(64)`; `payload_hash`; `result_version INTEGER`; sanitized `result_body`; `created_at`. Stores the outcome of a successful save for retry detection. |

The editable relationship diagram is `docs/diagrams/assignment-2-data-model.mmd`. It supplements the original [Canva ER figures](https://canva.link/mnbu5ng6gg0l7hs), which must be reconciled with these fields before the final PDF is exported.

### **2.6.2 Integrity and authorization**

Database primary keys, foreign keys, uniqueness, and row checks enforce structural rules. PostgreSQL row checks do not replace authorization or rules involving other records; those belong in service transactions. See [PostgreSQL's constraint documentation](https://www.postgresql.org/docs/current/ddl-constraints.html).

- Membership and Like composite keys prevent duplicates. A partial unique index permits only one pending OfficialRequest per community.
- A Report check requires exactly one target. Unique Decision.report_id and Appeal.decision_id enforce one initial decision per report and one appeal per decision.
- A community audience requires a non-null community. C2 additionally checks membership and prevents restricted-community content from using a university audience. Changes to community visibility must preserve that restriction for existing content in the same transaction.
- Draft versions start at 1. A save locks/checks the current draft, validates organizer access and the submitted version, updates the body and version, and inserts its receipt atomically. A repeated request ID with the same payload returns its recorded result after current authorization; a changed payload is rejected. A unique published-post link and locking the draft during publication prevent duplicate posts.
- `published_post_id` and `published_at` are either both null or both populated. Publication checks valid nonempty content and creates the post in the same transaction. The publishing organizer is recorded as the post author.
- Only the affected author may appeal, and only up to seven days after `decided_at`. C6 enforces the deadline and independent reviewer rule. Decision, content visibility change, and audit insertion commit together; appeal resolution likewise updates its outcome, any permitted visibility change, and audit history atomically.
- Report snapshots preserve evidence if an author later edits the content. Hidden and author-deleted states are separate, so reversing moderation cannot restore author-deleted material. Resolving one report must not undo another active decision to hide the same content.

### **2.6.3 Queries, migrations, and retention**

Initial indexes support membership checks (`user_id`, `status`), community feeds (`community_id`, `created_at`, `post_id`), university feeds (`audience`, `created_at`, `post_id`), comments (`post_id`, `created_at`), drafts (`community_id`, `updated_at`), pending appeals (`status`, `created_at`), reports by each non-null target, and audit history (`target_type`, `target_id`, `occurred_at`). Token hashes are uniquely indexed; expiry timestamps support cleanup. Referencing foreign keys also receive indexes where not already covered. Query plans and representative data will determine refinements.

SQLAlchemy models will live in `backend/app/models/`; reviewed Alembic revisions will live in `backend/migrations/`. Migrations will be tested against an empty database and the preceding schema before deployment, with a backup and recovery plan for destructive changes. [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) manages schema revisions; it does not make a backup or prove a migration safe.

The development baseline uses fictional data. Expired or consumed verification records and expired/revoked sessions are cleaned daily. Successful draft-save receipts remain for the draft's lifetime, preserving retry results. Author deletion immediately removes content from normal views and AI input; restricted evidence and audit records remain available to authorized reviewers. Account disabling revokes sessions. Foreign keys restrict deletion of referenced evidence rather than cascading away moderation history; the normal application role can insert/read audit records but cannot update/delete them.

A production retention period for account data, evidence, drafts, and audits requires university approval before real student data is collected. A later approved purge must address dependent receipts, evidence, and backup expiry as well as primary records. Daily backups retain seven copies under the proposed deployment plan. AI summaries are returned on demand without a persistent summary table in this baseline.

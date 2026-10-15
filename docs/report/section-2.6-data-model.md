## **2.6 Data Model**

The PoC stores only integer `post_id` and string `body` in memory. The ER diagram describes the planned PostgreSQL model for Assignment 2, not an existing database.

### **2.6.1 Entities and relationships**

Each entity has an ID. References link related records; for example, `author_id` links a post to a user. Membership and Like identify their records using a pair of IDs.

| Entity | Main information and links |
| ----- | ----- |
| User | `user_id`, unique `email`, `password_hash`, `verified`, `global_role` |
| Community | `community_id`, `creator_id`, `name`, `visibility`, `official` |
| Membership | `user_id`, `community_id`, `role`, `status` |
| Post | `post_id`, `author_id`, optional `community_id`, `audience`, `body`, `status` |
| Draft | `draft_id`, `community_id`, `owner_id`, `body`, `version`, `status`, optional unique `published_post_id` |
| Comment | `comment_id`, `post_id`, `author_id`, `body`, `status` |
| Like | `user_id`, `post_id` |
| OfficialRequest | `request_id`, `community_id`, `requester_id`, optional `reviewer_id`, `reason`, `status` |
| Report | `report_id`, `reporter_id`, one target (`post_id` or `comment_id`), `reason`, `status` |
| Decision | `decision_id`, `report_id`, `moderator_id`, `action`, `reason`, `decided_at` |
| Appeal | `appeal_id`, `decision_id`, `appellant_id`, optional `reviewer_id`, `reason`, `status`, `submitted_at`; resolution adds `outcome`, `resolution_reason`, `resolved_at` |
| AuditRecord | `audit_id`, `actor_id`, `action`, `target_type`, `target_id`, `reason`, `recorded_at` |

Supporting account records hold login sessions and email verification information; their implementation details are outside this ER overview.

### **2.6.2 Constraints and policies**

- Users join communities through Membership. Organizer roles belong to a community, not the whole university. Only approved organizers edit and publish its drafts.
- A user has at most one membership per community and one like per post. Removing a like removes that pair.
- A university-wide post may have no community. Community-only posts require one; restricted-community content is limited to approved members.
- Posts contain sanitized rich text, limited to 2,000 visible characters. Comments contain plain text, limited to 500. Published content cannot be empty.
- Post and Comment `status` is `published`, `hidden`, or `deleted`. Reversing moderation only changes `hidden` back to `published`; it never restores `deleted` content. Content stays hidden if another active decision still requires it.
- Draft saves check the loaded version and increase it on success. Publication creates the post and records Draft's unique `published_post_id` together, after checking the draft. Repeated publication returns the linked post instead of creating another.
- Each report targets exactly one post or comment. Each report has at most one initial decision; each decision has at most one appeal. Only the affected author may appeal within seven days of `decided_at`; a different moderator reviews it.
- Decisions and appeal outcomes are recorded. Hidden content remains available as review evidence, but not in normal views or AI input. Ordinary users cannot change audit records.

The backend checks permissions; database keys and constraints prevent broken links and duplicates. `docs/diagrams/assignment-2-data-model.mmd` shows the same core relationships.

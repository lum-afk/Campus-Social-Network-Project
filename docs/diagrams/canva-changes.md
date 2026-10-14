# Canva changes for the simplified Sila report

Apply these edits to the original figures before exporting the final report. This checklist compares the revised report with the Canva figures embedded in the supplied team-report PDF (pages 12–14, 16, and 19–20). It does not claim that the live Canva document has been updated. All diagrams describe the planned Assignment 2 system.

## Context diagram

No label changes are needed. Keep the one-university boundary, four user groups, external email service, and external LLM service. Provider selection remains pending.

## Container diagram

| Location | Old label → new label |
| ----- | ----- |
| API → email arrow | `Verification over TLS` → `Verification address and link over HTTPS` |
| Bottom caption | `Verified users access WEB in a browser. Containers are applications or data stores.` → `Users register or log in through WEB in a browser. Protected features require verified accounts. Containers are applications or data stores.` |

The second change allows the registration and login pages to be reached before verification. Keep WEB/React, API/FastAPI, DB/PostgreSQL, and the HTTPS/WebSocket connections. No low-level hosting or backup labels need to be added.

## Backend component diagram

No label changes are needed. Keep C1–C7 inside one API application. Short names such as `C4 Publishing` are abbreviations of the report's component names, not additional components.

## Collaboration sequence diagram

Use `version`, `request_id`, `draft_id`, and `body` throughout. The report example uses draft 42 and request `save-42-a`; use `save-42-b` for the conflicting save. `body A` and `body B` below mean the organizers' proposed rich-text strings.

| Location | Old label → new label |
| ----- | ----- |
| Organizer A → API | `Save d1, content A, baseVersion 7, requestId a1` → `draft.save: draft_id 42, body A, version 7, request_id save-42-a` |
| Both API → DB save arrows | `Atomic update where version = 7` → `Check version = 7 and save together` |
| DB → API successful result | `Commit content A, version 8` → `Saved body A, version 8` |
| API → Organizer A acknowledgement | `Saved a1, version 8` → `draft.saved: draft_id 42, request_id save-42-a, body A, version 8` |
| API → Organizer B broadcast | `Draft updated: content A, version 8` → `draft.saved: draft_id 42, request_id save-42-a, body A, version 8` |
| Organizer B → API | `Save d1, content B, baseVersion 7, requestId b1` → `draft.save: draft_id 42, body B, version 7, request_id save-42-b` |
| API → Organizer B conflict | `Conflict b1: latest content, version 8` → `draft.conflict: draft_id 42, request_id save-42-b, body A, version 8, detail: Review the latest version.` |
| Bottom failure caption | `Database failure: return a save error and broadcast nothing. Successful updates follow commit.` → `Database failure: return draft.error with draft_id, request_id, code, and detail; broadcast nothing. Send successful updates only after saving succeeds.` |

Keep the note that both organizers loaded version 7, the permission checks, `No update: current version 8`, the note about B preparing an earlier save, and `REVIEW AND RETRY`. These still match the design.

## ER figure 5A — Users and communities

| Location | Old label → new label |
| ----- | ----- |
| Community fields | No `name` field → add `name` |
| OfficialRequest fields | No `reason` field → add `reason` |

Keep `verified`, `creator_id`, `official`, `requester_id`, and `reviewer_id`. The simplified report now uses these names. Keep the existing membership keys and relationships.

## ER figure 5B — Publishing

| Location | Old label → new label |
| ----- | ----- |
| Post fields | `body and status` → separate lines: `body` and `status: published / hidden / deleted` |
| Comment fields | `body and status` → separate lines: `body` and `status: published / hidden / deleted` |
| Draft fields | `FK UK published_post_id` → `FK UK published_post_id (optional)` |
| Draft fields | `body, version and status` → separate lines: `body`, `version`, `status` |
| Figure note | No moderation-reversal note → add `Reversing moderation changes hidden to published only; never restore deleted content. Keep hidden if another active decision requires it.` |
| Figure note | No publication note → add `Check the draft and save the post and unique published_post_id together. Repeated publication returns the linked post.` |

Keep Draft's `owner_id`, unique `published_post_id`, optional one-to-one Post/Draft relationship, and the one-like-per-user/post rule. Do not remove the unique marker. The existing optional community link is correct.

## ER figure 5C — Moderation and appeals

| Location | Old label → new label |
| ----- | ----- |
| Appeal fields | No resolution fields → add `outcome (optional)`, `resolution_reason (optional)`, `resolved_at (optional)` |
| AuditRecord fields | `action and target_id` → separate lines: `action`, `target_type`, `target_id` |
| Figure note | `Appeal within 7 days.` → `Affected author may appeal within 7 days of decided_at.` |

Keep `submitted_at` and `recorded_at`. Keep the exactly-one-report-target rule, the seven-day appeal rule, the independent reviewer rule, and all current relationships. `target_type` identifies whether an audit target is a post, comment, decision, or appeal; it does not add a new entity.

## Export checks

- Keep each figure readable when placed in the final PDF; wrap long sequence labels if needed.
- Include the context, container, component, sequence, and all three ER figures in the report, with their editable sources in the repository.
- The simplified core ER diagram does not need Session, EmailVerification, or DraftSaveReceipt boxes. They were not present in the supplied Canva figures.
- Keep team-member names exactly as written in the existing team report.

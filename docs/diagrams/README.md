# Assignment 2 diagram sources

These diagrams describe the planned Assignment 2 system, not the implemented PoC.

## Canva source and report figures

[Sila diagrams — editable Canva source](https://canva.link/mnbu5ng6gg0l7hs)

The link was accessible without signing in when checked on 15 October 2026, so the teaching team can view the design. Its current guest access also permits editing; no sharing permissions were changed.

The following PNG files are the exact images embedded in [the report PDF](../report/Sila-Assignment-1.pdf). They were extracted without image conversion from the same Google Docs revision on 15 October 2026. The PNGs are static exports; use Canva to edit the original figures.

| File | Figure |
| --- | --- |
| `c4-context.png` | C4 system context |
| `c4-containers.png` | React, FastAPI, PostgreSQL, and external services |
| `c4-components.png` | Backend components C1–C7 |
| `collaboration-sequence.png` | Saved draft updates and conflict handling |
| `er-users-communities.png` | ER 5A: users and communities |
| `er-publishing.png` | ER 5B: posts, drafts, comments, and likes |
| `er-moderation-appeals.png` | ER 5C: reports, decisions, appeals, and audit records |

## Supplementary editable Mermaid files

- `assignment-2-deployment.mmd`: React, one FastAPI process, PostgreSQL, and external services from Section 2.2.
- `assignment-2-data-model.mmd`: the 12 core entities and relationships in Section 2.6. Field types explain the model rather than specifying a SQL schema. Each report targets exactly one post or comment; the two optional lines alone cannot express that rule. Audit targets use `target_type` and `target_id` as recorded references.
- `canva-changes.md`: the original diagram change checklist and its verification status.

Login sessions and email verification need supporting account records but are outside this core ER diagram. Save retry tracking is described in Section 2.4 without a separate entity here.

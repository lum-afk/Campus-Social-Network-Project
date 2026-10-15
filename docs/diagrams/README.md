# Assignment 2 diagram sources

These files describe the planned Assignment 2 design, not the implemented PoC.

- `assignment-2-deployment.mmd`: React, one FastAPI process, PostgreSQL, and external services from Section 2.2.
- `assignment-2-data-model.mmd`: the 12 core entities and relationships in Section 2.6. Field types are explanatory, not a SQL schema. Each report targets exactly one post or comment; the two optional lines alone cannot express that rule. Audit targets use `target_type` and `target_id` as recorded references.
- `canva-changes.md`: exact changes for the owner of the original Canva figures.

Login sessions and email verification need supporting account records but are outside this core ER diagram. Save retry tracking is described in Section 2.4 without a separate entity here.

The Mermaid files supplement the Canva context, container, component, sequence, and three ER figures.

## Editable Canva source

[Sila diagrams — editable source](https://canva.link/mnbu5ng6gg0l7hs)

The shared design contains seven pages: context, containers, backend components, collaboration sequence, users and communities, publishing, and moderation and appeals. The link was accessible without signing in when checked on 15 October 2026, so the teaching team can view the design. Its current guest access also permits editing; no sharing permissions were changed.

The live design contains revised sequence and ER field labels. `canva-changes.md` records the requested changes, not proof that every checklist item is complete. The diagram owner is replacing the images in the shared report. Final diagram exports and the report PDF must come from that completed revision.

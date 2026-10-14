# Assignment 2 diagram sources

These files describe the planned Assignment 2 design, not the implemented PoC.

- `assignment-2-deployment.mmd`: React, one FastAPI process, PostgreSQL, and external services from Section 2.2.
- `assignment-2-data-model.mmd`: the 12 core entities and relationships in Section 2.6. Field types are explanatory, not a SQL schema. Each report targets exactly one post or comment; the two optional lines alone cannot express that rule. Audit targets use `target_type` and `target_id` as recorded references.
- `canva-changes.md`: exact changes for the owner of the original Canva figures.

Login sessions and email verification need supporting account records but are outside this core ER diagram. Save retry tracking is described in Section 2.4 without a separate entity here.

The Mermaid files supplement the original Canva context, container, component, sequence, and ER diagrams. The Canva figures have not been edited. Include readable figures and their editable sources in the final submission.

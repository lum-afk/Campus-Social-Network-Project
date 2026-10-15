## **2.5 Code and Repository Structure**

The current repository contains the Assignment 1 PoC. Assignment 2 folders below are planned, not implemented.

| Current location | Contents |
| ----- | ----- |
| `poc/app/main.py` | FastAPI routes, validation, and in-memory posts |
| `poc/app/index.html` | Browser page, styling, and JavaScript |
| `poc/tests/` | Contract tests |
| `poc/requirements.txt`, `poc/README.md` | Dependencies, setup, tests, and demo instructions |
| `docs/contracts/`, `docs/report/` | PoC contract and report sections |
| `docs/diagrams/` | Mermaid sources and Canva change checklist |
| `.github/workflows/poc-tests.yml` | Automated PoC checks on GitHub |
| `CLAUDE.md`, `.gitignore` | AI workflow instructions and files excluded from Git |

| Planned location | Responsibility |
| ----- | ----- |
| `frontend/` | React pages, rich-text editor, and WebSocket client |
| `backend/app/api/` | C1: HTTP routes and WebSocket messages |
| `backend/app/services/` | C2–C7: permission checks and business rules |
| `backend/app/models/`, `backend/app/repositories/` | Database records and access |
| `backend/app/integrations/` | Email and AI service calls |
| `backend/app/core/` | Shared settings and login helpers |
| `backend/tests/`, `frontend/tests/` | Backend, browser, and integration tests |
| `config/`, `.env.example` | Configuration examples with placeholders only |

This separates pages, business rules, and data access so each can be tested. Assignment 2 will sit alongside `poc/`, keeping the demonstration reproducible. Mohammed is responsible for the current PoC under the recorded team allocation; Assignment 2 ownership must be agreed in Section 3.1.

Secrets belong only in backend environment variables, never in Git or browser code. Local environments and personal settings are excluded from Git. Existing documentation folders will also hold Assignment 2 material.

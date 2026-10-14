## **2.5 Code and Repository Structure**

The current repository contains the Assignment 1 proof of concept, its contract, tests, report text, and GitHub Actions workflow. The planned React frontend and modular backend for Assignment 2 have not yet been implemented.

**Current repository**

| Location | Contents |
| ----- | ----- |
| `poc/app/main.py` | FastAPI routes, validation handling, and in-memory post storage |
| `poc/app/index.html` | Browser interface, styling, and JavaScript |
| `poc/app/__init__.py` | Python package marker |
| `poc/tests/test_posts.py` | Automated contract tests |
| `poc/requirements.txt` | Pinned direct Python dependencies |
| `poc/README.md` | Setup, run and test commands, demo steps, and limitations |
| `docs/contracts/poc-posts.md` | Approved PoC interface specification |
| `docs/report/assignment-1-source.md` | Working report text based on the Google Doc export |
| `docs/report/section-*.md` | Individual report sections for review and transfer to the shared report |
| `docs/diagrams/` | New Mermaid sources for the proposed deployment and data relationships, with a scope README |
| `.github/workflows/poc-tests.yml` | GitHub Actions contract-test workflow |
| `CLAUDE.md` | Project scope, commands, and AI-assisted workflow instructions |
| `.gitignore` | Excludes local environments, caches, credentials, and personal settings |

The local Python environment at `poc/.venv/` and personal Claude settings are not committed. The report text export does not contain the original diagram images. The new Mermaid sources supplement the design; the original Canva sources and a final PDF containing readable figures remain submission deliverables.

`poc/requirements.txt` pins FastAPI, Uvicorn, pytest, and httpx2. The existing GitHub Actions workflow runs the PoC tests on Python 3.13 for PRs targeting `main` and pushes to `main` or `feature/poc-posts`. It does not build a React application, provision PostgreSQL, or test the proposed Assignment 2 system.

**Planned Assignment 2 structure**

| Planned location | Responsibility |
| ----- | ----- |
| `frontend/` | React pages, forms, Tiptap editor, and WebSocket client |
| `backend/app/api/` | HTTP routes and WebSocket gateway |
| `backend/app/services/` | Business components C2–C7 |
| `backend/app/models/` | SQLAlchemy PostgreSQL models and constraints |
| `backend/app/repositories/` | Database access and transaction operations |
| `backend/app/integrations/` | Email and AI HTTPS adapters, with development mocks |
| `backend/app/core/` | Settings, session handling, and shared security helpers |
| `backend/migrations/` | Reviewed Alembic schema revisions |
| `backend/tests/` and `frontend/tests/` | Component and integration tests |
| `docs/diagrams/` | Additional editable architecture figures and final exports alongside the existing Mermaid sources |
| `docs/contracts/` | HTTP and WebSocket specifications |
| `docs/adr/` | Architecture decision records |
| `config/` and `.env.example` | Nonsecret examples for approved domains, database connection, session/token lifetimes, provider settings, and disabled live AI by default |
| `ops/` | Deployment, backup, restore, and monitoring procedures |

This table describes planned additions; only the locations in the current-repository table already exist. Assignment 2 will be developed alongside `poc/`, preserving the Assignment 1 contract and reproducible demonstration. Its dependency lockfiles and PostgreSQL integration checks will be added with that implementation. Mohammed is responsible for the current proof-of-concept implementation under the recorded team task allocation. Assignment 2 code-maintenance responsibilities will be agreed with the team and recorded in Section 3.1 before those components are developed.

Database passwords, session secrets, email credentials, and AI keys must remain in backend environment variables or a secret manager. They must not appear in repository files or browser code. Configuration examples contain placeholders only.

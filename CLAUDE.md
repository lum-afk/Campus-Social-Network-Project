# Sila — AI1220 team project
University assignment: campus social network. The report in docs/report/
describes the planned Assignment 2 system (React, FastAPI, PostgreSQL,
WebSockets, LLM). It is context, not the scope of this proof of concept.

## Current work: Assignment 1 proof of concept (poc/)
- Source of truth: docs/contracts/poc-posts.md. Match the approved field names,
  status codes, and error messages exactly.
- If that contract is missing or marked incomplete, stop before implementation
  and ask for the finalized contract. Do not invent requirements.
- Keep code small and readable; I must explain every line in an oral exam.
- No features beyond the contract: no authentication, database, React,
  WebSockets, or AI in this proof of concept.
- Explain decisions and verification results in plain language.

## Commands (macOS, from poc/)
Python 3.13 is available. The virtual environment is already created.
- Activate: source .venv/bin/activate
- Install, once requirements.txt exists: python -m pip install -r requirements.txt
- Run, once app/main.py exists: python -m uvicorn app.main:app --reload
- Open: http://127.0.0.1:8000
- Test, once tests exist: python -m pytest
These application paths are provisional; update them to match the final code.

## Git and workflow
- Use one local feature branch; do not create a worktree.
- Plan first and wait for my approval before implementation.
- Commit only relevant files and describe AI assistance honestly.
- Never push or open a PR; I do those myself, then request teammate review.
- Never commit secrets, local Claude settings, or the virtual environment.

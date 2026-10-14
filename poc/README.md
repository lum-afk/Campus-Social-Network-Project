# Sila — Assignment 1 proof of concept

A small FastAPI backend and a plain HTML/CSS/JavaScript page that create and list posts.
It implements the contracts in [`docs/contracts/poc-posts.md`](../docs/contracts/poc-posts.md),
which demonstrate the creation and retrieval part of FR-03. All content is fictional.

## Setup (macOS, from `poc/`)

```bash
python3.13 -m venv .venv          # only if .venv does not exist yet
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Run

```bash
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000. The page and the API are served from the same address.

## Test

```bash
python -m pytest
```

Use `python -m pytest` (not plain `pytest`) so that `poc/` is on the import path and the tests can import `app.main`.

GitHub Actions runs this suite on Python 3.13 for pull requests into `main` and
pushes to `main` or `feature/poc-posts`. See the PR Checks tab for the result.
These automated API tests do not replace the browser demo or teammate review.

## Files

| File | Purpose |
|---|---|
| `app/main.py` | API: `POST /posts`, `GET /posts`, the validation-error handler, and `GET /` for the page |
| `app/index.html` | The page: textbox, character counter, Publish button, status message, feed |
| `tests/test_posts.py` | Automated checks of the contract |

## API summary

- `POST /posts` with `{"body": "text"}` returns `201` and `{"post_id": 1, "body": "text"}`.
  The body is trimmed and must then contain 1–2000 Unicode code points.
  Invalid requests return `422` with `{"detail": "<message>"}`.
- `GET /posts` returns `200` and all posts, newest first (`[]` when empty).

## Demo (about three minutes)

1. Start the server and open the page. It shows "No posts yet."
2. Type `😀😀`. The counter shows 2, because emoji are counted as one code point each.
3. Publish `  Hello Sila  `. It appears trimmed, and the textbox clears.
4. Publish a second post. It appears above the first.
5. Publish `<b>bold?</b>`. The tags appear as text, not bold.
6. Publish only spaces. The backend's error message appears, and the text stays in the box.
7. Reload the page. The posts are still there.
8. Stop the server (Ctrl+C) and click Publish. The page says the request could not be confirmed.
9. Start the server again and reload. The feed is empty, and IDs start again at 1.

## Limitations (deliberate simplifications)

- Posts live in a Python list in memory. Restarting the backend deletes them and resets IDs.
- No login, authors, or audience controls. Anyone who can reach the local server can post.
- Plain text only. Posts are shown with `textContent`, so HTML appears as text. This is not
  the planned rich-text editor or sanitizer.
- No edit, delete, communities, comments, likes, moderation, WebSockets, or AI.
- Designed for one local backend process.

The planned Assignment 2 architecture (React, PostgreSQL, WebSockets, and an LLM) is described in `docs/report/`.

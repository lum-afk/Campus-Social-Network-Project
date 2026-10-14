# **4 Proof of Concept**

## **4.1 Purpose and scope**

The Sila proof of concept demonstrates how a browser communicates with a Python backend to create and retrieve posts. It implements the creation and retrieval portion of FR-03 using fictional content. The application is a local demonstration, with no authentication or audience controls. It does not claim to implement the full planned campus social network.

The submitted interface specification is `docs/contracts/poc-posts.md`, summarized in Section 2.4. The implementation is in `poc/`, with setup, execution, tests, and a demonstration checklist in `poc/README.md`.

## **4.2 Implementation**

The application uses FastAPI and a single HTML page containing CSS and JavaScript. FastAPI serves both the page and the JSON API from the same address. The page includes a textbox, a character counter, a Publish button, and a feed displaying the newest post first.

`POST /posts` accepts a JSON object containing a string `body`. The backend trims surrounding whitespace and checks that the result contains 1–2,000 Unicode code points. It then assigns an integer `post_id`, starting at 1, and appends the post to an in-memory Python list. Only successful creations consume an ID. The response uses HTTP `201` and returns the ID and trimmed body.

`GET /posts` returns HTTP `200` and the posts in descending ID order. An empty list returns `[]`. The backend stores only `post_id` and `body`; it does not store users, audiences, or other fields from the planned data model.

FastAPI validates the request structure before the create route runs. A custom `RequestValidationError` handler maps framework validation errors to the exact messages specified in the contract. The route handles empty or over-limit trimmed text. Both paths return HTTP `422` with a string `detail`.

The browser sends the entered text using `fetch`. It disables Publish while the request is pending, clears the textbox after success, and retrieves the updated feed. A validation failure preserves the input and displays the backend's message. A network failure is reported as an unconfirmed request, because a lost response does not prove that the backend failed to create the post. A successful creation followed by a failed feed refresh has a separate message.

The frontend counts code points with `Array.from(text.trim()).length`; the backend uses Python's `len()` after trimming and is authoritative. A simple emoji such as 😀 is one code point, although some visible emoji contain several code points. Feed content is inserted with `textContent`, so HTML-like input is displayed as text rather than interpreted as markup.

## **4.3 Verification**

The automated suite in `poc/tests/test_posts.py` contains 28 passing test cases. It checks creation and retrieval, every documented validation error, trimming, preservation of internal whitespace, newest-first ordering, and ID behaviour. Boundary tests accept exactly 2,000 code points and reject 2,001, including emoji inputs. The suite also checks that the page is served and that HTML-like input is stored unchanged.

GitHub Actions runs the suite on Python 3.13. Successful runs were recorded for the feature-branch push and PR at commit `c48f332`, and for `main` after the merge at `bd56619`:

- [Feature-branch checks](https://github.com/lum-afk/Campus-Social-Network-Project/actions/runs/38594017193)
- [Pull-request checks](https://github.com/lum-afk/Campus-Social-Network-Project/actions/runs/38594017665)
- [Checks after merging to main](https://github.com/lum-afk/Campus-Social-Network-Project/actions/runs/38594983200)

These tests exercise the API and page response; they do not execute the page's JavaScript. The implementation record in [PR #1](https://github.com/lum-afk/Campus-Social-Network-Project/pull/1) separately records browser checks for the counter, text rendering, input preservation, loading state, refresh behaviour, and failure messages. The README provides the steps to reproduce the demonstration. No production load, uptime, usability-study, or full accessibility compliance result is claimed for this PoC.

## **4.4 Simplifications and limitations**

| Planned Assignment 2 system | Implemented Assignment 1 PoC |
| ----- | ----- |
| React frontend and rich-text editor | One HTML/CSS/JavaScript page with plain text |
| PostgreSQL and the full relational model | A Python list containing post IDs and bodies |
| Verified users, ownership, and audiences | No login or access checks; fictional local data |
| Modular components C1–C7 | One small FastAPI module demonstrating posting |
| WebSocket draft collaboration | Ordinary HTTP requests for posts |
| Communities, likes, comments, moderation, appeals, and AI | Not implemented |

The list survives browser refreshes while the same backend process is running. Restarting that process deletes all posts and resets the IDs. The PoC is intended for one local backend process: multiple worker processes would have separate lists and would not provide a shared feed. Development auto-reload can also restart the process when source files change.

The three-minute demonstration follows the README: show the empty feed, publish trimmed text and a second post, show newest-first ordering and literal HTML-like input, reject whitespace-only input, refresh the browser, and restart the backend to show the storage limitation. This is a demonstration plan, not a claim that every team member has completed a timed rehearsal.

## **4.5 Development record and AI assistance**

Development used `feature/poc-posts`, with separate commits for the approved contract, implementation and tests, documentation, and automated checks. PR #1 was merged into `main` on 14 October 2026, preserving those commits.

Claude Code assisted with the implementation plan, code, tests, and README. Codex assisted with repository setup, CI configuration, workflow documentation, and this report draft. AI assistance is identified in the commit messages and PR description. Passing tests and AI review do not constitute a teammate's review or establish that every student understands the implementation.

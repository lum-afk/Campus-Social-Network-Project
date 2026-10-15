# **4 Proof of Concept**

## **4.1 Purpose and scope**

The PoC demonstrates a browser creating and retrieving posts through a Python backend. It covers part of FR-03 using fictional data. The code is in `poc/`; `poc/README.md` explains setup, execution, tests, and the demonstration. Section 2.4.1 describes the implemented contract.

## **4.2 Implementation**

FastAPI serves one HTML page containing CSS and JavaScript. The page has a textbox, character counter, Publish button, and newest-first feed.

The browser sends `body` to `POST /posts`. The backend trims outer whitespace, checks the 1–2,000-code-point limit, assigns `post_id`, and stores the post in a Python list. Success returns `201`. `GET /posts` returns the list newest first with `200`. Invalid input returns `422` with the contract's exact message. Rejected requests consume no ID.

The backend decides whether text is valid. Both sides count Unicode code points; some visible emoji contain several. `textContent` displays HTML-like input as text, so it cannot become page markup.

Publish is disabled while saving. Success clears the input and reloads the feed. Validation failures preserve the input. A lost network response leaves the result uncertain; a successful save followed by a failed feed refresh has a separate message.

## **4.3 Verification**

The recorded automated run passed 28 tests covering the contract's valid and invalid inputs, trimming, IDs, ordering, and the 2,000/2,001 boundaries, including emoji. GitHub Actions also passed on the branch, PR, and merged `main`.

These tests check the API and page response, not execution of browser JavaScript. [PR #1](https://github.com/lum-afk/Campus-Social-Network-Project/pull/1) records separate browser checks. The README explains how to repeat the demonstration. No production performance or full accessibility result is claimed.

## **4.4 Simplifications and limitations**

| Planned system | PoC |
| ----- | ----- |
| React and rich text | HTML/CSS/JavaScript and plain text |
| PostgreSQL | Temporary Python list |
| Verified users and audience controls | No login or permissions |
| C1–C7 and WebSocket collaboration | One small backend using HTTP |
| Communities, moderation, and AI | Omitted |

Browser refresh preserves posts while the backend runs. Restarting it clears posts and resets IDs. The PoC uses one process because separate processes would have separate lists.

The demo plan has a three-minute limit: show an empty feed; publish two posts; show trimming, newest-first order, and literal HTML; reject whitespace-only input; refresh; then restart to show data loss. A timed rehearsal has not been recorded.

## **4.5 Development record and AI assistance**

Development used `feature/poc-posts`, with separate commits for the contract, code/tests, documentation, and CI. PR #1 was merged into `main` on 14 October 2026, preserving those commits.

Claude Code assisted with the plan, code, tests, and README. Codex assisted with repository setup, CI, workflow documentation, and the report. Commits and the PR identify AI assistance. The team remains responsible for reviewing and understanding the work.

PR #1 was merged before any teammate review. A post-merge review was requested from @lum-afk.

**Sila — Assignment 1 Proof of Concept Specification**

**1. Purpose and scope**

The PoC demonstrates how a browser interface communicates with a Python backend to create and retrieve posts.

The page will contain:

- A textbox with a character counter.
- A **Publish** button.
- A feed displaying posts, newest first.
- Clear loading, success, and error feedback.

All content is fictional. The PoC demonstrates the creation and retrieval portion of **FR-03: Publishing Posts**. It does not implement the complete requirement, authentication, or audience permissions.

**2. Technologies and storage**

| Part | Choice |
|---|---|
| Frontend | HTML, CSS, and JavaScript |
| Backend | Python with FastAPI |
| Communication | HTTP requests with JSON responses |
| Storage | A Python list in backend memory |
| Execution | Locally, with one backend process |

FastAPI serves the webpage and API from the same address.

Each stored post contains:

| Field | Type | Meaning |
|---|---|---|
| `post_id` | Integer | Backend-generated identifier, starting at 1 and increasing with each successful creation |
| `body` | String | Validated, trimmed plain-text post |

These field names match the planned data model. Author records and other planned fields are omitted from this simplified PoC.

Posts remain available after a browser refresh while the backend is running. **Restarting the backend clears all posts and resets the IDs.**

**3. Validation and text handling**

The backend:

1. Requires `body` to be a string; numbers and other types are rejected without conversion.
2. Removes leading and trailing whitespace.
3. Checks that the trimmed text contains **1–2,000 Unicode code points**.
4. Stores and returns the **trimmed text**. Internal spaces and line breaks are preserved.

The backend’s character count is authoritative. The frontend counter uses `Array.from(text).length` on its trimmed input rather than JavaScript’s `.length`. Backend validation determines whether the submission is accepted.

Posts are displayed using **`textContent`, not `innerHTML`**. HTML entered into a post appears as text. This is plain-text rendering, not an implementation of the planned rich-text editor or sanitization.

**4. Interface contract: create a post**

| Item | Definition |
|---|---|
| Method and endpoint | `POST /posts` |
| Request content type | `application/json` |
| Required field | `body`: string |
| Example request | `{"body":"  Our fictional coding club meets on Thursday.  "}` |
| Success status | `201 Created` |
| Example response | `{"post_id":1,"body":"Our fictional coding club meets on Thursday."}` |
| Invalid request status | `422 Unprocessable Entity` |
| Error format | `{"detail":"Readable error message"}` |

Required validation responses:

| Invalid input | `detail` message |
|---|---|
| Malformed JSON | `Request body must be valid JSON.` |
| JSON value that is not an object | `Request body must be a JSON object.` |
| Missing `body` field | `The body field is required.` |
| Non-string `body`, including `null` | `Post body must be a string.` |
| Empty, whitespace-only, or over-limit body | `Post body must contain 1–2000 characters after trimming.` |

A custom FastAPI **`RequestValidationError` handler** converts framework validation errors into the agreed string-based error format. Application validation uses the same format.

Rejected requests do not create posts or consume a post ID.

**5. Interface contract: retrieve posts**

| Item | Definition |
|---|---|
| Method and endpoint | `GET /posts` |
| Request body | None |
| Success status | `200 OK` |
| Response | JSON array of stored posts |
| Ordering | `post_id` descending—newest first |
| Example response | `[{"post_id":2,"body":"Welcome to the club!"},{"post_id":1,"body":"Our first announcement."}]` |
| Empty feed | `[]`, with status `200 OK` |

**Authorization for both endpoints:** no login or permission checks. Anyone able to reach the local application can create and retrieve demonstration posts. No privacy or authenticated-identity claims are made.

**6. Frontend behaviour**

- Retrieve posts when the page opens.
- Submit the textbox value to `POST /posts`.
- Disable Publish while its request is pending.
- After successful creation, clear the textbox and retrieve the updated feed.
- On validation failure, preserve the input and display the backend’s error message.
- On a network failure, explain that the request could not be confirmed.
- If creation succeeds but refreshing the feed fails, explain that the post was created but the feed could not be refreshed.
- Display an empty-state message when no posts exist.

**7. Simplifications from the planned architecture**

| Planned Sila application | Assignment 1 PoC |
|---|---|
| React with rich-text editing | HTML/CSS/JavaScript with plain text |
| PostgreSQL and full data model | Temporary Python list with two post fields |
| Verified users and audience controls | Shared local demonstration feed |
| Modular backend components | Small FastAPI application |
| WebSocket collaboration | Ordinary HTTP requests |
| Communities, comments, likes, moderation, and AI | Omitted |

The full architecture remains the plan for Assignment 2. These simplifications will be explained in Section 4 and the README. The two contracts above are explicitly **PoC contracts**.

**8. Completion checks and deliverables**

The PoC is complete when:

- Valid posts can be created and retrieved using these contracts.
- Surrounding whitespace is removed from stored and returned text.
- Empty, whitespace-only, missing, non-string, and over-limit inputs are rejected.
- Malformed JSON and non-object JSON return the specified errors.
- Every documented validation failure returns `422` with a string `detail`.
- Exactly 2,000 code points are accepted; 2,001 are rejected, including tests involving emoji.
- Posts appear in descending `post_id` order.
- HTML-like content is displayed as text.
- Browser refresh preserves posts while the backend runs; backend restart clears them.
- The README documents setup, execution, checks, and limitations.
- Section 4 explains the implementation and simplifications.
- The demonstration runs within **three minutes**.

Work will use a feature branch and meaningful commits. A teammate will review the pull request before it is merged into the shared repository. Git history and review records must reflect work that actually occurred.

The separate team-report update must also cover Section 3.3: development methodology, iterations, prioritization, feedback, and scheduling of testing, documentation, and technical tasks.
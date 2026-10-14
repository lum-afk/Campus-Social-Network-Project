## **2.4 Interfaces**

Sila has two interface scopes. The Assignment 1 proof of concept implements a local browser-to-backend interface for creating and retrieving plain-text posts. The planned Assignment 2 system adds verified identities, audience controls, collaboration, moderation, and external services. The proposed Assignment 2 interfaces below describe that design; they are not features of the current PoC.

### **2.4.1 Implemented proof-of-concept interface**

FastAPI serves the HTML/CSS/JavaScript page at `GET /` and the API at the same address, normally `http://127.0.0.1:8000`. The browser sends HTTP requests and receives JSON. The authoritative PoC specification is `docs/contracts/poc-posts.md`.

**Create a post**

| Item | Contract |
| ----- | ----- |
| Endpoint | `POST /posts` |
| Request | JSON object with required string field `body`; content type `application/json` |
| Success | `201 Created`, returning `post_id` and `body` |
| Validation failure | `422 Unprocessable Entity`, returning a string `detail` |
| Authorization | None; this is a local demonstration using fictional content |

Example request:

```json
{"body":"  Our fictional coding club meets on Thursday.  "}
```

Example response from a fresh backend:

```json
{"post_id":1,"body":"Our fictional coding club meets on Thursday."}
```

The backend requires `body` to be a string without converting other types. It removes leading and trailing whitespace, then accepts 1–2,000 Unicode code points. Internal spaces and line breaks are preserved. The stored and returned text is the trimmed value. Successful creations receive increasing integer IDs starting at 1; rejected requests neither create a post nor consume an ID.

Every documented validation failure returns HTTP `422` with exactly one of these messages in `detail`:

| Invalid input | Exact `detail` value |
| ----- | ----- |
| Malformed JSON | `Request body must be valid JSON.` |
| JSON value that is not an object | `Request body must be a JSON object.` |
| Missing `body` field | `The body field is required.` |
| Non-string `body`, including `null` | `Post body must be a string.` |
| Empty, whitespace-only, or over-limit body | `Post body must contain 1–2000 characters after trimming.` |

For example, `{"body":"   "}` returns:

```json
{"detail":"Post body must contain 1–2000 characters after trimming."}
```

A custom `RequestValidationError` handler converts FastAPI validation errors into this string-based format. Length validation uses the same format.

**Retrieve posts**

| Item | Contract |
| ----- | ----- |
| Endpoint | `GET /posts` |
| Request body | None |
| Success | `200 OK`, with a JSON array of posts |
| Ordering | `post_id` descending, newest first |
| Empty feed | `[]`, also with `200 OK` |
| Authorization | None |

Example response after two successful creations:

```json
[
  {"post_id":2,"body":"Welcome to the club!"},
  {"post_id":1,"body":"Our first announcement."}
]
```

The posts are stored in a Python list in one backend process. Refreshing the browser preserves them while that process runs. Restarting the backend clears the list and resets the IDs. These endpoints demonstrate only the creation and retrieval part of FR-03; they do not implement identity, audience privacy, editing, or deletion.

**Browser handling**

The page retrieves the feed when it opens. Its character counter uses `Array.from(text.trim()).length`; backend validation remains authoritative. Publish is disabled while a submission is pending. After a successful creation, the page clears the textbox and retrieves the feed again. Validation failures preserve the input and display the backend's `detail` message.

If the submission cannot be confirmed because of a network failure, the page tells the user to check the server and refresh to see whether the post was created. It does not automatically resubmit the post. If creation succeeds but feed retrieval fails, it reports those two outcomes separately. Posts are rendered with `textContent`, so HTML-like input appears as text. This is plain-text rendering, not the planned rich-text editor.

### **2.4.2 Proposed Assignment 2 HTTP interfaces**

The planned React frontend communicates with C1, the FastAPI HTTP and WebSocket Gateway, using HTTPS and JSON. The proposed routes use `/api/v1` to distinguish them from the simplified PoC routes. C2 checks the authenticated identity, verification state, roles, ownership, membership, and audience before the appropriate component performs an operation. Client-supplied IDs never establish permission.

The proposed session design uses an opaque session identifier in a `Secure`, `HttpOnly`, `SameSite=Lax` cookie. State-changing browser requests also require CSRF protection and origin validation. Login establishes a session; logout invalidates it. Registration, verification, and login remain accessible without an existing session. Section 2.2 specifies backend-managed accounts, password hashing, session lifetimes, and the deployment baseline; live email and AI providers still require selection and approval.

Successful reads and updates use `200`, creations use `201`, accepted asynchronous operations use `202`, and successful deletions without a response body use `204`. Errors use a JSON object with a string `detail`: `401` for missing or invalid authentication, `403` for a known operation the user cannot perform, `404` for an unavailable resource, `409` for a conflicting state, and `422` for invalid input. Resource lookups use `404` where revealing that restricted content exists would disclose information. Unexpected internal failures return a generic `500` without credentials, database errors, or stack traces.

The following are the main proposed frontend/backend interactions. Path IDs identify the target; the server derives the acting user's identity from the session.

| Area and routes | Main request and response fields | Permission and failure rules |
| ----- | ----- | ----- |
| Accounts: `POST /api/v1/accounts`, `POST /api/v1/accounts/verify`, `POST /api/v1/sessions`, `DELETE /api/v1/sessions/current` | Registration: `email`, `password`; verification: `token`; login: `email`, `password`. Responses report verification status or authenticated `user_id` and roles; never return passwords. | C2 validates the approved university domain and verification token. Invalid input returns `422`; invalid login returns a generic `401`; unverified users cannot access protected features. Email delivery failures permit retry without granting verified access. |
| Communities: `POST /api/v1/communities`, `POST /api/v1/communities/{community_id}/memberships` | Community: `name`, `visibility`; response: `community_id`, `name`, `visibility`. Joining returns `community_id`, `user_id`, and membership `status`. | Verified users may create communities. Open-community joins become approved; restricted-community joins become pending. Organizer approval is checked by C2/C3. Invalid visibility returns `422`; unauthorized membership decisions return `403`. |
| Official status: `POST /api/v1/communities/{community_id}/official-requests`, `PATCH /api/v1/official-requests/{request_id}` | Request: `reason`; decision: `status`. Response includes `request_id`, `community_id`, and `status`. | Organizers request status; university administrators approve or reject it. Unauthorized decisions return `403`; incompatible repeat decisions return `409`. |
| Posts and audiences: `POST /api/v1/posts`, `GET /api/v1/posts`, `PATCH /api/v1/posts/{post_id}`, `DELETE /api/v1/posts/{post_id}` | Create/update: rich-text `body`, `audience`, optional `community_id`. Returned posts include `post_id`, `body`, `author_id`, `audience`, and `community_id`. | C2/C4 enforce ownership and audience permissions. Restricted-community posts cannot target a wider audience. Validate sanitized visible text against the 2,000-character limit. Invalid content or audience combinations return `422`; denied actions return `403` or a non-disclosing `404`. |
| Interaction: `PUT /api/v1/posts/{post_id}/likes/me`, `DELETE /api/v1/posts/{post_id}/likes/me`, `POST /api/v1/posts/{post_id}/comments` | Likes use no client-supplied user ID; response reports `post_id` and `liked`. Comments accept `body` and return `comment_id`, `post_id`, `author_id`, and `body`. | Only users who can access the post may interact. Repeating the same like does not create another like. Comments must contain 1–500 visible characters; invalid comments return `422`. |
| Moderation: `POST /api/v1/reports`, `POST /api/v1/reports/{report_id}/decisions` | Report: `target_type`, `target_id`, `reason`; response: `report_id`, `status`. Decision: `action`, `reason`; response: `decision_id`, `action`, `decided_at`. | A report targets one post or comment. C6 restricts decisions to authorized moderators and records the actor and timestamp. Invalid targets return `422`; unauthorized action returns `403`; an already decided report returns `409`. |
| Appeals: `POST /api/v1/decisions/{decision_id}/appeals`, `PATCH /api/v1/appeals/{appeal_id}` | Appeal: `reason`; response: `appeal_id`, `status`, `submitted_at`. Resolution: `outcome`, `reason`; response includes the outcome and resolution timestamp. | Only the affected author may appeal within seven days. C6 checks the deadline using server timestamps. Late appeals return `422`. A different moderator reviews; escalated cases require an administrator. Unauthorized resolution returns `403`. |
| AI: `POST /api/v1/posts/{post_id}/summary` | No client-supplied discussion text is trusted. Response: `post_id`, `summary`, `ai_generated: true`. | C2/C7 authorize the published discussion and collect permitted posts/comments. Hidden content and drafts are excluded. Provider failure or invalid output returns `502`, unavailability `503`, and timeout `504`; the original discussion remains unchanged. |

For example, a proposed comment request is `{"body":"What time does it start?"}`. A successful `201` response is `{"comment_id":12,"post_id":2,"author_id":7,"body":"What time does it start?"}`. The server supplies the identifiers. This route and its authorization are planned Assignment 2 behaviour, not part of the PoC.

### **2.4.3 Proposed collaboration interface**

Authorized community organizers retrieve a draft through `GET /api/v1/drafts/{draft_id}` and subscribe to `/api/v1/drafts/{draft_id}/events` over a secure WebSocket. C1/C2 validate the session and origin when the connection opens. C2/C5 recheck permissions for saves and before sending protected updates. Removed permissions stop further access; reconnecting requires authorization and retrieval of the latest saved draft.

A proposed save message includes its type, draft ID, a unique request ID, the version the editor loaded, and the updated rich-text body:

```json
{"type":"draft.save","draft_id":42,"request_id":"save-42-a","version":7,"body":"<p>Club meeting at 4 pm.</p>"}
```

C5 validates the content and atomically checks the version while saving. Only after the database commits does it acknowledge the save and broadcast the new version to authorized subscribers:

```json
{"type":"draft.saved","draft_id":42,"request_id":"save-42-a","version":8,"body":"<p>Club meeting at 4 pm.</p>"}
```

A second save based on version 7 is rejected without overwriting version 8:

```json
{"type":"draft.conflict","draft_id":42,"request_id":"save-42-b","version":8,"body":"<p>Club meeting at 4 pm.</p>","detail":"The draft has changed. Review the latest version before saving."}
```

Other failures use `draft.error` with `draft_id`, `request_id`, a machine-readable `code` such as `invalid_content`, `forbidden`, or `save_failed`, and a safe string `detail`. A denied user receives no protected draft body. These are WebSocket message fields, not HTTP response statuses after the connection is established. Database failure produces no successful save acknowledgement or broadcast.

The proposed retry design records successful request IDs with their outcomes. Repeating the same request and payload returns its saved result without incrementing the version again; reusing the ID for different content is rejected. After losing an acknowledgement, the client retrieves the latest draft before deciding whether to retry. Conflicts require the organizers to review the latest text and resolve their changes manually.

Publishing uses `POST /api/v1/drafts/{draft_id}/publish` with `request_id` and the expected `version`. C5 rechecks organizer permissions and atomically creates the post and marks the draft published. A unique draft-to-post association prevents duplicate publication. First publication returns `201` with `draft_id`, `post_id`, and `status: "published"`; a repeat for the already published draft returns the same post with `200`. An outdated unpublished draft returns `409` with its latest version to an authorized caller.

### **2.4.4 Proposed external service interfaces**

Only the backend calls the external email and AI services over HTTPS. Provider credentials remain in backend configuration and never enter frontend code.

- **Email service:** C2 sends the recipient university email address and a verification link containing an expiring, single-use token. The adapter returns delivery acceptance or a failure result. Provider acceptance does not mean the user verified their account; verification requires a valid token. Failed delivery supports a controlled resend.
- **AI service:** C7 sends only the authorized published discussion text needed for the selected summary, excluding drafts, hidden content, unrelated discussions, and account metadata. The backend retains the requested post ID so the result is attached to the correct discussion. It validates nonempty output and labels it AI-generated. Permission is checked again before returning restricted content if the request was long-running. External processing requires university permission; timeouts and invalid output leave the discussion unchanged.

Email and AI adapters will be tested with mocked success, timeout, and failure responses before live integration. Provider-specific payloads will be defined when the team selects those services. None of these external calls are made by the Assignment 1 PoC.

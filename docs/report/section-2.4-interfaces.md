## **2.4 Interfaces**

Section 2.4.1 describes the implemented PoC. The remaining interfaces are planned for Assignment 2.

### **2.4.1 Implemented proof-of-concept interface**

FastAPI serves the page at `GET /` and the API from the same local address. The browser exchanges JSON with the backend. Both post routes need no login and use fictional content. The contract is `docs/contracts/poc-posts.md`.

- `POST /posts` requires `application/json` containing a JSON object with a string `body`. Success returns `201` with integer `post_id` and string `body`. Invalid input returns `422` with a string `detail`.
- `GET /posts` takes no request body and returns `200` with a JSON array, ordered by descending `post_id`. An empty feed returns `[]`.

Example creation on a fresh backend:

```json
{"body":"  Club meeting today.  "}
```

```json
{"post_id":1,"body":"Club meeting today."}
```

Retrieving that feed returns `[{"post_id":1,"body":"Club meeting today."}]`.

The backend rejects non-string values without conversion, trims outer whitespace, and accepts 1–2,000 Unicode code points. Internal spaces and line breaks remain. Stored and returned text is trimmed. IDs start at 1 and increase only after successful creation. Rejected requests create nothing and consume no ID.

Every documented validation failure returns `422` with one exact `detail` message:

| Invalid input | Exact message |
| ----- | ----- |
| Malformed JSON | `Request body must be valid JSON.` |
| JSON that is not an object | `Request body must be a JSON object.` |
| Missing `body` | `The body field is required.` |
| Non-string `body`, including `null` | `Post body must be a string.` |
| Empty, whitespace-only, or over-limit text | `Post body must contain 1–2000 characters after trimming.` |

Posts remain in memory after browser refresh. Restarting the backend clears posts and resets IDs. The backend's count decides acceptance; the browser counter also counts code points. HTML-like input is displayed literally using `textContent`.

The page loads the feed on opening. Publish is disabled while saving. Success clears the input and reloads the feed; validation failure keeps the input and shows the error. A network failure means the result is unconfirmed, so the page does not automatically retry. It reports separately when creation succeeds but feed refresh fails.

### **2.4.2 Proposed Assignment 2 HTTP interfaces**

All routes below start with `/api/v1` and use HTTPS and JSON. A login cookie identifies the user. C2 checks verification, ownership, roles, and audience; sending a user ID cannot grant permission.

Success uses `200` for reads/updates, `201` for creation, and `204` for deletion with no response body. Errors contain a string `detail`: `401` means login is missing or invalid; `403`, permission denied; `404`, unavailable or hidden resource; `409`, conflicting state; `422`, invalid input; `500`, unexpected server failure; `502`, failed or invalid provider response; `503`, service unavailable; and `504`, provider timeout. Errors do not expose secrets.

| Route, after `/api/v1` | Main fields exchanged | Who is allowed; main failures |
| ----- | ----- | ----- |
| `POST /accounts`, `POST /accounts/verify`, `POST /sessions`, `DELETE /sessions/current` | `email`, `password`, or verification `token`; return verification status or `user_id` and roles | Registration/login need no session; logout needs one. Approved university email required. `401`, `422`. |
| `POST /communities`, `POST /communities/{community_id}/memberships` | `name`, `visibility`; return `community_id` or membership `status` | Verified users. Restricted joins await organizer approval. `403`, `422`. |
| `POST /communities/{community_id}/official-requests`, `PATCH /official-requests/{request_id}` | Request `reason`; decision `status`; return `request_id`, `community_id`, `status` | Organizers request; administrators decide. `403`, `409`, `422`. |
| `GET /posts`, `POST /posts`, `PATCH /posts/{post_id}`, `DELETE /posts/{post_id}` | `body`, `audience`, optional `community_id`; returned posts include `post_id`, `author_id` | Verified users; viewers must be in the audience, authors edit/delete. Restricted-community posts stay restricted. `403`, `404`, `422`. |
| `PUT /posts/{post_id}/likes/me`, `DELETE /posts/{post_id}/likes/me`, `POST /posts/{post_id}/comments` | Like result: `post_id`, `liked`; comment: `body` → `comment_id`, `post_id`, `author_id`, `body` | Permitted viewers. One like per user/post; comments 1–500 characters. `403`, `404`, `422`. |
| `POST /reports`, `POST /reports/{report_id}/decisions` | `target_type`, `target_id`, `reason`; decision `action`, `reason`; return `report_id`, `status` or `decision_id`, `action`, `decided_at` | Users report accessible content; authorized moderators decide. `403`, `404`, `409`, `422`. |
| `POST /decisions/{decision_id}/appeals`, `PATCH /appeals/{appeal_id}` | `reason`; resolution `outcome`, `reason`; return `appeal_id`, `status`, `submitted_at` or outcome/time | Affected author appeals within seven days. A different moderator reviews; escalations need an administrator. `403`, `422`. |
| `GET /drafts/{draft_id}`, `POST /drafts/{draft_id}/publish` | Read: `draft_id`, `body`, `version`; publish: `request_id`, `version` → `draft_id`, `post_id`, `status` | Approved organizers of that community. `403`, `404`, `409`, `422`. |
| `POST /posts/{post_id}/summary` | Return `post_id`, `summary`, `ai_generated: true` | Permitted viewers; backend selects the discussion text. `403`, `404`, `502`, `503`, `504`. |

Post content is sanitized before its 2,000-character limit is checked. Only permitted content is returned.

### **2.4.3 Proposed collaboration interface**

Organizers connect to `/api/v1/drafts/{draft_id}/events` over WebSocket. Permissions are checked before saves and protected updates. A save sends the version the organizer loaded:

```json
{"type":"draft.save","draft_id":42,"request_id":"save-42-a","version":7,"body":"<p>Club meeting at 4 pm.</p>"}
```

The backend checks the version and saves together. Success sends `draft.saved` with `draft_id`, `request_id`, saved `body`, and the new `version` (8 here), then broadcasts the saved update. An outdated save gets `draft.conflict` with those identifiers, the latest body/version, and an explanatory `detail`. Organizers resolve the conflict manually.

Other failures send `draft.error` with `draft_id`, `request_id`, `code`, and `detail`. Denied users receive no draft content. A failed save broadcasts nothing. These are WebSocket messages, not HTTP status codes.

Each save has a request ID so a retried save is not applied twice. Reconnecting reloads the latest draft after checking permission.

Publishing saves the post and its draft link together. Draft's unique `published_post_id` identifies the published result. First publication returns `201`; repeating it returns that same post with `200`. An outdated unpublished draft returns `409`.

### **2.4.4 Proposed external service interfaces**

The backend sends the email service a university address and verification link, and receives acceptance or failure. Acceptance does not verify the account; the user must follow a valid link. Failed delivery can be retried.

For AI, the backend sends only authorized published discussion text, excluding drafts and hidden/deleted content. It checks that the response is nonempty and belongs to the requested discussion, then labels it AI-generated. Failure leaves the discussion unchanged. University permission is required before external processing. These services are planned, not connected in the PoC.

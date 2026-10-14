<!-- Working report text based on the 2026-10-14 Google Doc export. Sections 2.2, 2.4, 2.5, and 2.6 updated and Section 4 added locally on 2026-10-15. Related open questions and ADR wording aligned with the proposed baseline. Original diagram images are not included; new supporting Mermaid sources are in docs/diagrams/. Original: https://docs.google.com/document/d/1BZzcQYcdMwUVwqeCP_boOUC6ZeL1ItNhos_O01MjAJY/edit -->

# **Sila (صِلة)**

## **Assignment 1**

**Course:** AI1220 — Software, Web & Mobile Engineering

### **Project Overview**

**Sila (صِلة)** is an Arabic word meaning *connection* or *bond*. The name represents the purpose of our platform: bringing university students together and strengthening connections within the campus community.

Sila is a private social network designed for students within one university. Verified students can create and join communities, share posts, interact through likes and comments, and collaborate on event announcements. The platform also includes audience controls, moderation, and AI-powered discussion summaries.

The aim is to provide a safe and organized space where students can communicate, discover campus activities, and participate in university life.

---

## ***1  Requirements Engineering*** 

## **1.1 Stakeholder Analysis**

The following stakeholders have been identified for Sila.

| Stakeholder | Goals | Concerns | Influence |
| ----- | ----- | ----- | ----- |
| **SH-01 Students** | Share posts, join communities, and interact with others | Privacy, inappropriate content, and account security | High |
| **SH-02 Community Organizers** | Manage communities and collaborate on announcements | Unauthorized edits and low participation | High |
| **SH-03 Moderators** | Review reports and enforce community rules | False reports and unfair decisions | High |
| **SH-04 University Administrators** | Approve official communities and oversee university policies | Misinformation and policy violations | High |
| **SH-05 Development/IT Team** | Build and maintain a secure and reliable platform | Security, performance, and maintenance | Medium |

### **Stakeholder Interests and Potential Conflicts**

Different stakeholder groups may have competing interests:

* **Students and moderators:** Students want freedom to share opinions, while moderators need to maintain a safe environment. Clear community rules and an appeal process help balance these interests.  
* **Students and university administrators:** Students value privacy, while administrators need to oversee university policies. Access permissions limit unnecessary exposure of student content.  
* **Community organizers and members:** Organizers need control over community activities, while members want to participate. Role-based permissions define who can edit shared content.  
* **Moderators and administrators:** Moderators handle individual reports, while administrators oversee policy enforcement and escalated appeals.

These are potential differences in stakeholder interests, not disagreements within our project team.

---

## **1.2 Functional Requirements**

The functional requirements describe what Sila must allow users to do. Each requirement is written so it can be tested.

### **FR-01 — Identity and Account Verification**

The system shall allow students to register using an approved university email domain, verify their email address, log in, and log out.

* Students must verify their email before accessing the platform.  
* Registration using an unapproved email domain shall be rejected.  
* Invalid login credentials shall be rejected.

### **FR-02 — Community Creation and Membership**

The system shall allow verified students to create and join university communities.

* Students can create communities without administrator approval.  
* University administrators must approve a community before it receives official university status.  
* Students can join open communities immediately.  
* Restricted communities require membership approval from an authorized organizer.  
* Users without permission cannot access restricted community content.

### **FR-03 — Publishing Posts**

The system shall allow authenticated users to create, view, edit, and delete posts according to their permissions.

* Posts may contain rich text.  
* Posts must not exceed **2,000 characters**.  
* Empty posts and posts exceeding the character limit shall be rejected.  
* Users cannot edit or delete posts they are not authorized to manage.

### **FR-04 — Real-Time Collaboration**

The system shall allow authorized users to collaborate on shared event and announcement drafts.

* Authorized collaborators can edit shared drafts.  
* Changes shall be shown to other active collaborators in real time.  
* Unauthorized users cannot edit shared drafts.  
* The system shall detect conflicting or outdated edits and prevent them from silently overwriting newer changes.  
* Reconnected collaborators shall be able to retrieve the latest saved version.

### **FR-05 — Audience Control and Privacy**

The system shall allow post authors to select the audience for their posts.

* Authors can make posts visible to all verified students or only to members of a selected community.  
* The system shall check access permissions before displaying restricted posts.  
* Users outside the selected audience cannot view the post.

### **FR-06 — Likes and Comments**

The system shall allow authorized users to like, unlike, and comment on posts they can access.

* Each user can have only one active like per post.  
* Users can remove their likes.  
* Comments must not be empty.  
* Comments must not exceed **500 characters**.  
* Users cannot interact with posts they are not authorized to access.

### **FR-07 — Reporting, Moderation, and Appeals**

The system shall allow users to report inappropriate content and authorized moderators to review reports.

* Verified users can submit content reports.  
* Dedicated moderators can review reports and dismiss them or take moderation action.  
* Moderation decisions shall be recorded.  
* Affected users can submit an appeal within **seven days** of a moderation decision.  
* Appeals submitted after seven days shall be rejected.  
* University administrators shall review escalated appeals.  
* Users without moderation permissions cannot perform moderation actions.

### **FR-08 — AI Discussion Summarization**

The system shall allow authorized users to request AI-generated summaries of discussions they can access.

* A summary is generated only when the user selects **Summarize**.  
* The AI shall use only discussion content the requesting user is authorized to access.  
* The generated result shall be clearly labeled as an AI-generated summary.  
* The system shall verify that the result is nonempty and associated with the requested discussion.  
* Users shall be able to view the original discussion to check the summary.  
* If summarization fails, the system shall display an error message without changing or deleting the original discussion.

**AI requirement details**

* **User need:** Students need a quicker way to understand long discussion threads.  
* **Input data:** Text from discussion posts and comments that the requesting user is allowed to view.  
* **Output:** A short, clearly labeled summary of the selected discussion.  
* **Verification:** The system checks the response structure and discussion association. Users can compare the summary with the original content to check accuracy. The system does not guarantee that every AI-generated statement is correct.

---

## **1.3 Non-Functional Requirements**

The non-functional requirements define the quality standards Sila should meet to provide a secure, reliable, and user-friendly platform. Each requirement includes a measurable target and a justification.

### **NFR-01 — Performance**

The system shall respond to at least 95% of post creation and retrieval requests within 3 seconds under a test load of 50 concurrent users.

**Justification:** Students should be able to browse and publish posts without unnecessary delays.

### **NFR-02 — Scalability**

The system shall support at least 500 registered users and handle 50 concurrent users while meeting the performance target.

**Justification:** The platform should support increasing participation as more students join.

### **NFR-03 — Availability**

The system shall target 99% monthly availability, excluding scheduled maintenance.

**Justification:** Students need reliable access to campus discussions and announcements.

### **NFR-04 — Recovery**

The system shall back up stored data at least once every 24 hours and aim to restore service within 4 hours after a recoverable system failure.

**Justification:** Posts, community information, and announcements should be protected against data loss.

### **NFR-05 — Security**

The system shall securely hash stored passwords and reject unauthorized access to protected functions. Production communication shall use HTTPS.

**Justification:** Student accounts and platform functions must be protected against unauthorized access.

### **NFR-06 — Privacy**

The system shall restrict community-only posts to authorized members and prevent unauthorized discussion content from being sent to the AI summarization service.

**Justification:** Students should have control over who can access their content.

### **NFR-07 — Usability**

At least 4 out of 5 first-time test users shall be able to create a post and select its audience without assistance.

**Justification:** Students should be able to use the main features without training.

### **NFR-08 — Accessibility**

The system shall support keyboard navigation for its main functions and meet WCAG 2.2 Level AA requirements for text contrast.

**Justification:** The platform should be accessible to students with different needs.

### **NFR-09 — Auditability**

The system shall record moderation decisions with the moderator ID, action taken, affected content ID, and timestamp.

**Justification:** Moderation decisions must be traceable to support accountability and appeals.

### **NFR-10 — Real-Time Collaboration**

Under a test load of 10 active collaborators, at least 95% of successfully saved draft updates shall appear to other connected collaborators within 2 seconds.

**Justification:** Community organizers need timely updates when working together on announcements.

**Verification of Non-Functional Requirements**

This will be verified through performance testing, access-control testing, usability testing, accessibility checks, and review of system logs. The proposed targets will be evaluated using the available testing environment during Assignment 2\.

---

## **1.4 User Stories and Acceptance Criteria**

### **US-01 — Student Publishing a Post**

**As a student,** I want to create a post and select who can see it so that I can share information with the appropriate audience.

**Related requirements:** FR-03, FR-05

**Acceptance criteria:**

1. Given a verified student enters valid post content within 2,000 characters and selects an allowed audience, when the student publishes the post, then the system saves it and displays it to the selected audience.  
2. Given the student submits an empty post or exceeds 2,000 characters, when they try to publish, then the system rejects the post and displays an error.  
3. Given a user is outside the selected audience, when they try to access the post, then access is denied.

### **US-02 — Organizer Collaborating on an Announcement**

**As a community organizer,** I want to edit an announcement with other authorized collaborators so that we can prepare community events together.

**Related requirement:** FR-04

**Acceptance criteria:**

1. Given two authorized collaborators are editing a shared draft, when one saves a change, then the other receives the updated content in real time.  
2. Given an unauthorized user attempts to edit the draft, when the request is submitted, then the system denies the action.  
3. Given a collaborator submits an outdated edit that conflicts with a newer version, when the system processes it, then the conflict is detected and the newer content is not silently overwritten.  
4. Given a collaborator reconnects after losing connection, when the draft is reopened, then the latest saved version is retrieved.

### **US-03 — Student Requesting an AI Summary**

**As a student,** I want to summarize a long discussion so that I can understand its main points more quickly.

**Related requirement:** FR-08

**Acceptance criteria:**

1. Given a student can access a discussion, when they select Summarize, then the system generates and displays a clearly labeled AI summary.  
2. Given the summary is displayed, when the student wants to check its accuracy, then the original discussion remains available.  
3. Given the student does not have access to a discussion, when they request a summary, then the system denies the request.  
4. Given the AI service fails, when summarization is attempted, then an error is displayed and the original discussion remains unchanged.

### **US-04 — Moderator Reviewing a Report**

**As a moderator,** I want to review reported content so that I can help maintain a safe university community.

**Related requirement:** FR-07

**Acceptance criteria:**

1. Given a moderator opens a submitted report, when they review the content, then they can dismiss the report or take an authorized moderation action.  
2. Given a moderator makes a decision, when the action is confirmed, then the decision is recorded.  
3. Given a user without moderation permissions attempts to resolve a report, when the action is submitted, then access is denied.  
4. Given an affected user appeals within seven days, when the appeal is submitted, then the system accepts it for review.  
5. Given an appeal is submitted after seven days, when the system checks the deadline, then the appeal is rejected.  
6. Given an appeal is escalated, when it reaches the appropriate stage, then an authorized university administrator can review it.

---

## **1.5 Requirements Validation and Traceability**

**Requirements Review**

The draft was checked for coverage, testability, and consistency. The review identified unclear rules concerning university configuration, restricted-community audiences, collaboration permissions, and appeal escalation. The following policies clarify these areas.

### **Policies and Assumptions**

* Each deployment serves one university with configurable approved email domains.  
* Different universities use separate deployments and databases.  
* Only verified university users access the platform.  
* Open communities allow immediate joining; restricted communities require organizer approval.  
* Restricted-community posts remain visible only to approved members.  
* Posts outside restricted communities may target all verified students or members of a selected community.  
* Only approved organizers of the relevant community edit and publish shared announcements.  
* Outdated draft saves are rejected without overwriting newer content.  
* Administrators approve official-community requests submitted by organizers.  
* Affected authors may appeal within seven days.  
* A different moderator reviews an appeal. It escalates when independent review is unavailable or university policy is involved.  
* AI summarizes authorized published discussions on request. Drafts and hidden content are excluded.

The appeal workflow and proposed technical design require team confirmation before submission.

### **Open Questions**

| Question | Owner |
| ----- | ----- |
| Which university domains will be accepted? | University administrator |
| Is external AI processing permitted? | University policy owner |
| Which deployment account/domain, email provider, and permitted AI provider/model will be used? The database, editor, and authentication baseline is specified in Section 2.2. | Coder with university approval |
| Who will operate the monitoring and backup plan in Section 2.2, and approve production retention in Section 2.6? | Team and university deployment owner |

### **Architecture Identifiers**

| ID | Component |
| ----- | ----- |
| WEB | React frontend |
| API | FastAPI backend |
| DB | PostgreSQL database |
| C1  | HTTP and WebSocket Gateway |
| C2 | Identity and Access Control |
| C3 | Community Management |
| C4 | Publishing and Interaction |
| C5 | Draft Collaboration |
| C6 | Moderation and Appeals |
| C7 | AI Integration |
| OPS | Configuration, monitoring, and backup procedures |

**Traceability Matrix**

| Stakeholder Need | Requirements | Story / Scenario | Components |
| :---- | :---- | :---- | :---- |
| SH-01: Secure access | FR-01, NFR-05 | SC-01: Registration and login | WEB, C1, C2, DB |
| SH-01, SH-02: Community participation | FR-02 | SC-02: Joining and approval | WEB, C2, C3, DB |
| SH-01: Publishing and privacy | FR-03, FR-05, NFR-06 | US-01 | WEB, C2, C4, DB |
| SH-02: Shared announcements | FR-04, NFR-10 | US-02 | WEB, C1, C2, C5, DB |
| SH-01: Likes and comments | FR-06 | SC-03: Post interaction | WEB, C2, C4, DB |
| SH-03, SH-04: Moderation and appeals | FR-07, NFR-09 | US-04 | WEB, C2, C6, DB |
| SH-04: Official communities | FR-02 | SC-04: Official approval | WEB, C2, C3, DB |
| SH-01: Discussion summaries | FR-08, NFR-06 | US-03 | WEB, C2, C7, DB |
| SH-01, SH-05: Responsive service | NFR-01, NFR-02 | SC-05: Load testing | WEB, API, DB |
| SH-05: Reliable service | NFR-03, NFR-04 | SC-06: Monitoring and restoration | API, DB, OPS |
| SH-01: Usability and accessibility | NFR-07, NFR-08 | SC-07: Interface testing | WEB |

**Additional Scenarios**

* **SC-01:** Reject unapproved domains, unverified access, and invalid credentials.  
* **SC-02:** Allow open joining and require approval for restricted joining.  
* **SC-03:** Enforce one active like per user per post and validate comments.  
* **SC-04:** Allow only administrators to approve official status.  
* **SC-05–SC-07:** Perform the corresponding checks in Section 1.3.

**Scope Clarification**

Multiple universities sharing one deployment are outside scope. The existing feature exclusions remain unchanged..

---

## ***2  System Architecture***

## **2.1 Architectural Drivers**

The following requirements have the greatest influence on Sila’s design.

| Rank | Driver | Design Response |
| :---- | :---- | :---- |
| 1 | Security and privacy | Check identity, roles, ownership, membership, and audience in the backend. |
| 2 | Safe collaboration | Use draft-version checks to prevent silent overwrites and WebSockets to distribute saved updates. |
| 3 | Moderation accountability | Store decisions, appeals, and audit records. |
| 4 | Required technologies and manageable development | Use React, FastAPI, WebSockets, and an LLM integration within one modular backend. |
| 5 | Performance and reliability | Use indexed queries, testing, monitoring, backups, and restoration procedures. |

One backend divided into modules keeps development and deployment manageable. The proposed Assignment 2 baseline selects PostgreSQL because Sila’s records have relationships and draft saves require reliable transactions.

## **2.2 System Design**

The Assignment 2 design uses a React frontend, one modular FastAPI backend, and PostgreSQL. The choices below form the proposed implementation baseline for team review. The current Assignment 1 application remains the smaller plain-text PoC described in Sections 2.4 and 4; it has no database, authentication, rich-text editor, WebSockets, or AI integration.

### **2.2.1 Context and containers**

Sila serves students, community organizers, moderators, and administrators at one university per deployment. Approved university email domains are configuration values. Email verifies account ownership; an external AI service supplies summaries only when university policy permits processing the selected discussion.

| Container | Selected design | Responsibility |
| ----- | ----- | ----- |
| WEB | React with the Tiptap editor | Pages, forms, audience selection, rich-text editing, and display of saved draft updates |
| API | Python/FastAPI, components C1–C7 | Authentication, authorization, business rules, HTTP endpoints, and WebSocket connections |
| DB | PostgreSQL, accessed through SQLAlchemy; Alembic migrations | Persistent records, constraints, and transactions |

The browser and API share one HTTPS origin. A reverse proxy serves the React build and forwards `/api/v1/` requests, including secure WebSocket connections, to FastAPI. Only the backend accesses PostgreSQL and external service credentials. Database access is private to the deployment network.

The existing context, container, and component figures are maintained in [the team's Canva design](https://canva.link/mnbu5ng6gg0l7hs). They must use the WEB/API/DB and C1–C7 names above. The text export lacks those images. The new editable deployment diagram in `docs/diagrams/assignment-2-deployment.mmd` supplements the figures; it does not replace their original editable sources.

### **2.2.2 Backend components**

| Component | Responsibility |
| ----- | ----- |
| C1: HTTP and WebSocket Gateway | Validate and route requests and events |
| C2: Identity and Access Control | Check accounts, global roles, ownership, membership, and audiences |
| C3: Community Management | Manage communities, membership, and official status |
| C4: Publishing and Interaction | Manage posts, comments, likes, and content validation |
| C5: Draft Collaboration | Manage draft versions, publication, and saved-update notifications |
| C6: Moderation and Appeals | Manage reports, decisions, appeals, and audit records |
| C7: AI Integration | Collect authorized discussion text, call the provider, and validate results |

These are modules within one application. Services own business transactions; repositories perform database operations within those transactions. C2 checks permissions for HTTP actions, WebSocket subscriptions, saves, and delivery of protected updates.

### **2.2.3 Authentication and rich text**

Authentication will use university email verification, passwords hashed with Argon2 through `pwdlib`, and opaque server-side sessions stored in PostgreSQL. This avoids adding a separate identity provider to the initial implementation. The password-hashing library choice follows [FastAPI's password-hashing guidance](https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/); Sila's proposed session mechanism does not use that tutorial's JWT flow.

Each login generates a fresh random session token. The database stores its hash; the browser receives it in a `Secure`, `HttpOnly`, `SameSite=Lax` cookie. State-changing requests require CSRF protection and origin checks. WebSocket handshakes check the origin and session; expiry, logout, or lost permissions stop further protected actions and updates. Proposed defaults are a 30-minute idle timeout, a 12-hour absolute session lifetime, and a 30-minute single-use email verification token. Login, registration, and resend attempts are rate limited. These controls follow [OWASP's session-management guidance](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).

Tiptap will expose paragraphs, bold, italic, lists, line breaks, and links. Its HTML output fits the `body` string in the proposed interfaces. C4 sanitizes incoming HTML with `nh3`, allowing only the corresponding tags and safe HTTP/HTTPS links; scripts, event handlers, styles, images, and embeds are excluded. Only sanitized HTML is stored and rendered. Both libraries support these capabilities: [Tiptap content formats](https://tiptap.dev/docs/guides/output-json-html) and [nh3 allowlists](https://nh3.readthedocs.io/en/stable/index.html).

For validation, C4 extracts text from the sanitized HTML, decodes entities, represents line breaks and block boundaries as newlines, trims outer whitespace, and counts Unicode code points. A published post must contain 1–2,000 code points. Drafts may be empty while being prepared but cannot publish empty. Comments use plain text with a 1–500 code-point limit. Shared fixtures will keep the browser counter consistent with backend validation. Collaboration uses the versioned save protocol in Section 2.4, with manual conflict resolution.

### **2.2.4 Deployment and external services**

The initial deployment target is one Linux host with a TLS reverse proxy, one FastAPI worker, and PostgreSQL on a persistent volume. A single worker allows connected draft clients to share the same in-process broadcast registry. Database transactions remain authoritative; clients retrieve the latest snapshot after reconnecting. Scaling to multiple workers requires shared event distribution and is a later change.

OPS will collect health checks, error counts, request latency, and connection failures without logging passwords, tokens, or discussion bodies. The proposed backup plan is a daily encrypted database backup to separate storage, seven daily copies, and a restore rehearsal before demonstration. Section 1.3's availability and recovery figures remain targets until measured; this single-host design provides no automatic failover.

Email and AI use backend HTTPS adapters with timeouts and mocked responses for development. Live service selection requires an approved account, budget, and university data-handling permission. Until those are available, verification delivery is simulated in development and the live AI feature remains disabled. A mock summary must be labelled as a test response. No hosting subscription, email delivery, or live AI integration is claimed by this report.

The remaining external decisions are the deployment account/domain, approved university email domains, email provider, and permitted AI provider/model. The application structure, database, editor, authentication approach, and migration approach above can proceed without inventing those approvals.

## **2.3 Behaviour and Design Decisions**

**Audience and Authorization**

C2 checks permissions before protected requests, draft subscriptions, saves, and AI requests.

* Authors manage their own ordinary posts.  
* Restricted-community posts remain visible only to approved members.  
* Only approved community organizers edit and publish shared announcements.  
* Moderators and administrators access only the evidence needed for their assigned reviews.

C4 sanitizes rich text and rejects empty content. Limits apply to visible text: 2,000 characters per post and 500 per comment.

**Publishing and Collaboration**

C5 checks the submitted draft version and updates it in one database transaction. Successful saves increase the version and are broadcast after the transaction commits.

Outdated saves are rejected. Organizers review the latest content and manually resolve conflicts. After reconnecting, they retrieve the latest saved draft.

Publishing rechecks organizer permissions, creates the post, and marks the draft published in one transaction. Repeated requests must not create duplicate posts.

**Sequence Diagram**

The diagram shows two organizers who loaded version 7\. The first save creates version 8\. The second save still references version 7 and is rejected without overwriting the newer content.

**![][image4]**

[**https\://canva.link/mnbu5ng6gg0l7hs**](https://canva.link/mnbu5ng6gg0l7hs)

**Failure Handling**

| Situation | System Response |
| ----- | ----- |
| Outdated draft save | Reject the save and provide the latest version. |
| Lost connection | Reauthorize and retrieve the latest draft. |
| Database save failure | Return an error and broadcast no successful update. |
| Lost save acknowledgement | Retrieve the current snapshot before retrying. |
| Permission removed | Reject further actions and stop protected updates. |
| AI timeout or invalid response | Return an error without changing the discussion. |

**Moderation and Appeals**

C6 allows moderators to dismiss reports or hide reported content. Decisions record the actor, action, target, reason, and timestamp.

Affected authors may appeal within seven days. A different moderator reviews the appeal. It escalates to an administrator when independent review is unavailable or university policy is involved.

Hidden content remains review evidence but is excluded from normal access and AI. Appeal resolutions are recorded. Reversing moderation does not restore content independently deleted by its author.

**AI Summarization**

C7 collects only the selected discussion content the requester may access. It excludes drafts, hidden content, unrelated discussions, and account metadata.

External processing requires university permission. Results are labeled AI-generated and checked for nonempty content and association with the request. The original discussion remains accessible.

These checks do not guarantee accuracy. Personal information entered in discussion text may still be present.

**Development and Testing**

Test permissions, draft-version checks, appeal deadlines, and AI filtering separately. Then test browsers, API, and DB together.

Use browser sessions to test conflicting saves, reconnection, and permission changes. Mock email and AI services to test failures without paid calls.

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

## **2.6 Data Model**

The implemented PoC stores a Python list of records containing only integer `post_id` and string `body`. IDs start at 1 and the list disappears when the process restarts. The relational model below is the proposed Assignment 2 design; no tables or migrations currently exist in the application.

### **2.6.1 Types and records**

PostgreSQL entity IDs use `BIGINT GENERATED ALWAYS AS IDENTITY` primary keys. Foreign keys use `BIGINT`; timestamps use `TIMESTAMPTZ` with UTC values; free text uses `TEXT`. Status and role values use `TEXT` with `CHECK` constraints. Fields are required unless marked nullable. Each main entity has `created_at`; mutable entities also have `updated_at`. API identifiers retain Section 2.4's names, such as `post_id`, rather than changing the PoC contract.

| Record | Principal fields and relationships |
| ----- | ----- |
| User (`users`) | `user_id`; unique normalized `email`; `password_hash`; nullable `verified_at`; `global_role` (student/moderator/admin); `status` (active/disabled) |
| Community | `community_id`; `created_by` → User; `name`; `visibility` (open/restricted); `is_official BOOLEAN` |
| Membership | Composite primary key (`community_id`, `user_id`), referencing Community and User; `role` (member/organizer); `status` (pending/approved/rejected) |
| Post | `post_id`; `author_id` → User; nullable `community_id` → Community; sanitized HTML `body`; `audience` (university/community); independent nullable `hidden_at` and `deleted_at` |
| Draft | `draft_id`; `community_id` → Community; `created_by` and `updated_by` → User; sanitized HTML `body`; positive `version INTEGER`; nullable unique `published_post_id` → Post; nullable `published_at` |
| Comment | `comment_id`; `post_id` → Post; `author_id` → User; plain-text `body`; independent nullable `hidden_at` and `deleted_at` |
| Like | Composite primary key (`post_id`, `user_id`), referencing Post and User; `created_at`; unlike removes the row |
| OfficialRequest | `request_id`; `community_id` → Community; `requested_by` → User; `reason`; `status` (pending/approved/rejected); nullable `reviewed_by` → User and `reviewed_at` |
| Report | `report_id`; `reporter_id` → User; exactly one of nullable `post_id` → Post or `comment_id` → Comment; `reason`; protected `evidence_body` snapshot of the reported content |
| Decision | `decision_id`; unique `report_id` → Report; `moderator_id` → User; `action` (dismiss/hide); `reason`; `decided_at` |
| Appeal | `appeal_id`; unique `decision_id` → Decision; `appellant_id` → User; `reason`; `status` (pending/escalated/resolved); nullable `reviewer_id` → User, `outcome` (upheld/reversed), `resolution_reason`, and `resolved_at` |
| AuditRecord | `audit_id`; `actor_id` → User; `action`; `target_type`; `target_id BIGINT`; `reason`; `occurred_at`; reference information for moderation and appeal events |

User global roles are separate from organizer roles held through Membership. `target_id` in AuditRecord is a historical reference selected by `target_type`, not a foreign key to several tables. C6 validates it when appending the record. Report's two concrete foreign keys preserve referential integrity for either supported target.

The API derives a report's `status` from whether a Decision exists, maps an appeal's `created_at` to `submitted_at`, and maps `resolution_reason` to the resolution request's `reason`. The report request's `target_type` and `target_id` select the corresponding concrete target foreign key.

The supporting records complete the authentication and retry design:

| Record | Fields and rules |
| ----- | ----- |
| Session | `session_id`; `user_id` → User; unique `token_hash`; `csrf_token_hash`; `created_at`, `last_seen_at`, `expires_at`; nullable `revoked_at`. Raw session tokens are not stored. |
| EmailVerification | `verification_id`; `user_id` → User; unique `token_hash`; `created_at`, `expires_at`; nullable `used_at`. Consuming a valid token and verifying the account occur in one transaction. Resending invalidates earlier outstanding tokens. |
| DraftSaveReceipt | Composite primary key (`draft_id`, `actor_id`, `request_id`), referencing Draft and User; `request_id VARCHAR(64)`; `payload_hash`; `result_version INTEGER`; sanitized `result_body`; `created_at`. Stores the outcome of a successful save for retry detection. |

The editable relationship diagram is `docs/diagrams/assignment-2-data-model.mmd`. It supplements the original [Canva ER figures](https://canva.link/mnbu5ng6gg0l7hs), which must be reconciled with these fields before the final PDF is exported.

### **2.6.2 Integrity and authorization**

Database primary keys, foreign keys, uniqueness, and row checks enforce structural rules. PostgreSQL row checks do not replace authorization or rules involving other records; those belong in service transactions. See [PostgreSQL's constraint documentation](https://www.postgresql.org/docs/current/ddl-constraints.html).

- Membership and Like composite keys prevent duplicates. A partial unique index permits only one pending OfficialRequest per community.
- A Report check requires exactly one target. Unique Decision.report_id and Appeal.decision_id enforce one initial decision per report and one appeal per decision.
- A community audience requires a non-null community. C2 additionally checks membership and prevents restricted-community content from using a university audience. Changes to community visibility must preserve that restriction for existing content in the same transaction.
- Draft versions start at 1. A save locks/checks the current draft, validates organizer access and the submitted version, updates the body and version, and inserts its receipt atomically. A repeated request ID with the same payload returns its recorded result after current authorization; a changed payload is rejected. A unique published-post link and locking the draft during publication prevent duplicate posts.
- `published_post_id` and `published_at` are either both null or both populated. Publication checks valid nonempty content and creates the post in the same transaction. The publishing organizer is recorded as the post author.
- Only the affected author may appeal, and only up to seven days after `decided_at`. C6 enforces the deadline and independent reviewer rule. Decision, content visibility change, and audit insertion commit together; appeal resolution likewise updates its outcome, any permitted visibility change, and audit history atomically.
- Report snapshots preserve evidence if an author later edits the content. Hidden and author-deleted states are separate, so reversing moderation cannot restore author-deleted material. Resolving one report must not undo another active decision to hide the same content.

### **2.6.3 Queries, migrations, and retention**

Initial indexes support membership checks (`user_id`, `status`), community feeds (`community_id`, `created_at`, `post_id`), university feeds (`audience`, `created_at`, `post_id`), comments (`post_id`, `created_at`), drafts (`community_id`, `updated_at`), pending appeals (`status`, `created_at`), reports by each non-null target, and audit history (`target_type`, `target_id`, `occurred_at`). Token hashes are uniquely indexed; expiry timestamps support cleanup. Referencing foreign keys also receive indexes where not already covered. Query plans and representative data will determine refinements.

SQLAlchemy models will live in `backend/app/models/`; reviewed Alembic revisions will live in `backend/migrations/`. Migrations will be tested against an empty database and the preceding schema before deployment, with a backup and recovery plan for destructive changes. [Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) manages schema revisions; it does not make a backup or prove a migration safe.

The development baseline uses fictional data. Expired or consumed verification records and expired/revoked sessions are cleaned daily. Successful draft-save receipts remain for the draft's lifetime, preserving retry results. Author deletion immediately removes content from normal views and AI input; restricted evidence and audit records remain available to authorized reviewers. Account disabling revokes sessions. Foreign keys restrict deletion of referenced evidence rather than cascading away moderation history; the normal application role can insert/read audit records but cannot update/delete them.

A production retention period for account data, evidence, drafts, and audits requires university approval before real student data is collected. A later approved purge must address dependent receipts, evidence, and backup expiry as well as primary records. Daily backups retain seven copies under the proposed deployment plan. AI summaries are returned on demand without a persistent summary table in this baseline.

## **2.7 Architecture Decision Records**

**ADR-01 — Modular Backend**

**Context:** Sila’s features share authorization and database transactions.

**Options:** Unstructured backend, modular backend, or microservices.

**Decision:** Use one FastAPI application divided into components C1–C7.

**Consequences:** Development, deployment, and testing remain manageable. Multiple WebSocket processes would require shared event distribution.

**ADR-02 — Relational Database**

**Context:** Records have relationships, and concurrent draft saves require transactions.

**Options:** In-memory storage, SQLite, PostgreSQL, or a document database.

**Decision:** Use PostgreSQL with SQLAlchemy models and Alembic migrations in the proposed Assignment 2 baseline. The Assignment 1 PoC retains its in-memory list.

**Consequences:** Supports constraints and atomic updates; requires setup, migrations, and backups.

**ADR-03 — Versioned Collaboration**

**Context:** Conflicting saves must not silently overwrite newer content.

**Options:** Last-save-wins, version checks, or automatic merging.

**Decision:** Use atomic version checks and WebSocket broadcasts after saving.

**Consequences:** Prevents silent overwrites, but organizers must manually reconcile conflicts.

**ADR-04 — Backend AI Integration**

**Context:** Summarization must respect permissions and protect credentials.

**Options:** Browser calls, provider calls across multiple routes, or a dedicated backend adapter.

**Decision:** C7 handles input filtering, provider calls, response checks, and failures.

**Consequences:** Supports mocks and provider replacement. Accuracy is not guaranteed, and external processing requires university permission.

**Status:** Sections 2.2 and 2.6 specify the proposed technical baseline for team review before submission. Deployment accounts, provider selection, university permissions, and production retention remain external decisions; no implementation or team approval is implied.

---

## **Project Scope**

### **In Scope**

* University email verification and authentication  
* Student-created and official university communities  
* Open and restricted community membership  
* Rich-text posts, likes, and comments  
* Post audience controls  
* Real-time collaboration on event and announcement drafts  
* Content reporting, moderation, and appeals  
* On-demand AI discussion summarization

### **Out of Scope**

* Public access for users outside the university  
* Support for multiple universities  
* Private direct messaging  
* Polls and voting  
* Native mobile application  
* Advanced search  
* Online shopping, advertising, or payments  
* Academic grading and student assessment

These excluded features may be considered for future development, but they are not part of the current project scope.

---

# ***3\. Project Management and Team Collaboration***

## **3.1 Team Roles and Responsibilities**

At the beginning of the Sila project, Fatma took responsibility for dividing the tasks among the team members. She assigned the work based on each member's strengths and what she believed they would feel comfortable doing.

After sharing the task division through Microsoft Teams, Fatma asked everyone whether they were comfortable with their responsibilities. She also explained that the tasks could be rearranged if anyone preferred a different role. All team members agreed to their original assignments, so no changes were needed.

Our responsibilities were divided as follows:

| Team Member | Responsibilities |
| ----- | ----- |
| Fatma and Fatima | Sections 1.1, 1.2, 1.4, and 1.5: Stakeholders, Functional Requirements, User Stories, and Requirements Validation and Traceability |
| Salama | Section 1.3: Nonfunctional Requirements, and Section 2: System Architecture |
| Fatma | Section 3: Project Management and Team Collaboration |
| Mohammed | Section 4: Proof of Concept, including coding and implementation |

Although each member had specific responsibilities, the team could still support one another and improve the overall report.

## **3.2 Task Organization and Progress Tracking**

The team followed a sequential workflow, meaning each member or group completed their assigned work before passing it to the next person.

Fatma and Fatima were the first to complete their sections. Once they finished, they shared their work in the Microsoft Teams group chat and informed the team that the next stage could begin.

Salama then continued from their work. She reviewed the existing sections, made improvements, and added her assigned parts, with Fatma's help when needed. After finishing, Salama shared the updated document with the group and informed everyone that it was Mohammed's turn to continue with the proof of concept.

This approach helped the team track progress because everyone knew which stage had been completed and who was responsible for the next stage.

## **3.3 Communication and Collaboration Tools**

The team used four main tools throughout the project:

* **Microsoft Teams:** The main communication platform, used to discuss responsibilities, share progress updates, and inform each other when tasks were completed.  
* **Google Docs:** The main workspace for writing the report. Fatma shared the document link in the Teams group chat so everyone could access it, edit their sections, and review the work.  
* **Canva:** Used by Salama to create and edit the diagrams and visual frameworks included in the report.  
* **GitHub:** Used by Mohammed to upload and merge the project code. Other team members could also view the repository to follow his progress and check the latest updates.

These tools helped the team keep the report and code organized while allowing everyone to stay informed about the project's progress.

## **3.4 Time Management**

The team did not set separate deadlines for each member. Instead, everyone agreed that the main goal was to complete the assignment before the official submission deadline.

Each member began their assigned work once the previous stage was completed. Everyone worked efficiently and shared their work without unnecessary delays.

This approach allowed the team to make steady progress while keeping the workload manageable and avoiding unnecessary pressure.

## **3.5 Teamwork and Challenges**

The team's collaboration has gone smoothly so far, without any disagreements or conflicts.

One reason for this was that everyone had the opportunity to agree to their responsibilities before starting. Communication also remained open through Microsoft Teams, allowing members to share updates and ask for help when needed.

Team members supported one another by reviewing and improving existing work rather than treating every section as completely separate. For example, Salama reviewed the requirements sections before adding her own work, and Fatma helped her with some of the improvements.

Overall, the collaboration has been organized and positive, allowing the team to move through the assignment without major difficulties.

## **3.6 Reflection on the Project Management Approach**

The team's approach worked well because everyone understood their responsibilities and felt comfortable with their tasks. Allowing members to agree to their assignments helped establish a clear division of work from the beginning.

The sequential workflow also made it easy to follow progress, since each completed stage was shared with the group before the next stage began.

One improvement for future projects would be to set smaller internal deadlines, even when the team is working efficiently. This would provide extra time for final reviews and unexpected delays.

Overall, the Sila project has been managed through clear responsibilities, open communication, shared documents, and regular progress updates.

---

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

The PR was merged at Mohamed's explicit request before a teammate submitted a review. That did not follow the review-before-merge process stated in the PoC specification. Post-merge review was requested from `lum-afk`; no submitted teammate review was present when this section was checked on 15 October 2026. Findings should be recorded on the PR and addressed through a follow-up PR. The history must retain the actual order of events.

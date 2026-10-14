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

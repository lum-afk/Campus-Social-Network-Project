## **2.2 System Design**

The planned Assignment 2 system uses React, FastAPI, and PostgreSQL. This design is separate from the smaller Assignment 1 PoC and remains subject to team review.

### **2.2.1 Context and containers**

The context diagram shows students, organizers, moderators, and administrators using Sila at one university. Email verification and AI summaries use external services outside Sila's boundary.

The container diagram shows three parts inside that boundary:

| Part | Technology and purpose |
| ----- | ----- |
| WEB | React: pages, forms, rich-text editing, and display of live updates |
| API | Python/FastAPI: requests, permissions, business rules, and WebSocket connections |
| DB | PostgreSQL: linked records such as users, posts, and communities |

React sends requests to FastAPI over HTTPS. WebSockets carry saved draft updates. FastAPI accesses PostgreSQL and calls the email and AI services; the browser does not access them directly.

React, rich text, FastAPI, WebSockets, and an LLM meet Assignment 2's technology constraints. PostgreSQL fits the linked data and lets related changes succeed or fail together.

### **2.2.2 Backend components**

The component diagram looks inside API. C1–C7 are modules in one backend, not separate applications.

| Component | Responsibility |
| ----- | ----- |
| C1: HTTP and WebSocket Gateway | Receive and route requests and events |
| C2: Identity and Access Control | Check accounts, roles, ownership, and audiences |
| C3: Community Management | Manage communities, membership, and official status |
| C4: Publishing and Interaction | Validate and manage posts, comments, and likes |
| C5: Draft Collaboration | Check draft versions, save, publish, and send updates |
| C6: Moderation and Appeals | Handle reports, decisions, appeals, and their records |
| C7: AI Integration | Send permitted content and check summary responses |

One backend keeps shared permission rules and database changes together.

### **2.2.3 Authentication and rich text**

Users verify an approved university email address. Passwords are stored as hashes, not readable passwords. A cookie identifies the login session; logout ends it. The backend checks permissions before protected actions and updates.

The server sanitizes rich text by removing unsafe markup before storing it. Posts allow 1–2,000 visible characters; plain-text comments allow 1–500. Empty drafts may be saved but cannot be published. These limits count Unicode code points after trimming outer whitespace.

### **2.2.4 Deployment and external services**

The plan uses one server running one FastAPI process so WebSocket updates share memory; more processes would need shared messaging. OPS covers health checks, daily database backups, and restore procedures, supporting NFR-03 and NFR-04.

Email verifies accounts. AI summarizes only content the requester may access, and its result is labelled AI-generated. Failure leaves the discussion unchanged. Secrets stay in backend environment variables.

Hosting and providers have not been set up. External AI processing needs university permission. Development can use mocks, meaning simulated service responses, without paid calls.

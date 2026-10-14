<!-- Text snapshot exported 2026-10-14 from the team Google Doc. Diagram images are not included in this text export. Original: https://docs.google.com/document/d/1BZzcQYcdMwUVwqeCP_boOUC6ZeL1ItNhos_O01MjAJY/edit -->

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
| Which hosting, authentication, editor, email, and AI services will be used? | Coder |
| How will monitoring, backups, and restoration be configured? | Coder or deployment owner |

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

| Rank | Driver | Design Response                      Design Response |
| :---- | :---- | :---- |
| 1 | Security and privacy | Check identity, roles, ownership, membership, and audience in the backend. |
| 2 | Safe collaboration | Use draft-version checks to prevent silent overwrites and WebSockets to distribute saved updates. |
| 3 | Moderation accountability | Store decisions, appeals, and audit records. |
| 4 | Required technologies and manageable development | Use React, FastAPI, WebSockets, and an LLM integration within one modular backend. |
| 5 | Performance and reliability | Use indexed queries, testing, monitoring, backups, and restoration procedures. |

One backend divided into modules keeps development and deployment manageable. PostgreSQL is proposed because Sila’s records have relationships and draft saves require reliable transactions.

## **2.2 System Design**

The architecture uses three C4 diagrams.

**System Context Diagram**

Sila serves students, community organizers, moderators, and administrators. Each deployment serves one university with configurable approved email domains. External email and AI services support verification and discussion summaries.**![][image1]**

[**https\://canva.link/mnbu5ng6gg0l7hs**](https://canva.link/mnbu5ng6gg0l7hs)

**Container Diagram**

| Container | Technology | Responsibility |
| ----- | ----- | ----- |
| WEB | React | Forms, audience selection, rich-text editing, and live-update display |
| API | Python/FastAPI | Permissions, business rules, HTTP requests, and WebSocket connections |
| DB | Proposed PostgreSQL | Persistent user, community, content, and moderation records |

WEB communicates with API through HTTPS and secure WebSockets. API accesses DB and calls the email and AI services. Provider credentials remain on the backend.

React, FastAPI, WebSockets, rich-text capabilities, and an LLM integration meet Assignment 2’s technology constraints

**![][image2]**

[**https\://canva.link/mnbu5ng6gg0l7hs**](https://canva.link/mnbu5ng6gg0l7hs)

**Component Diagram**

| Component | Responsibility |
| ----- | ----- |
| C1: HTTP and WebSocket Gateway | Validate and route requests and events |
| C2: Identity and Access Control | Check accounts, roles, ownership, membership, and audiences |
| C3: Community Management | Manage communities, membership, and official status |
| C4: Publishing and Interaction | Manage posts, comments, likes, and content validation |
| C5: Draft Collaboration | Manage draft versions, publishing, and live updates |
| C6: Moderation and Appeals | Manage reports, decisions, appeals, and audit records |
| C7: AI Integration | Prepare authorized input, call the provider, and check responses |

These components run within one FastAPI application and access the database through repositories.

**![][image3]**

[**https\://canva.link/mnbu5ng6gg0l7hs**](https://canva.link/mnbu5ng6gg0l7hs)

**Coder Task:** Confirm the database, editor, authentication, hosting, and provider choices. Keep the diagrams consistent with the final design.

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

**Coder Task — Complete Before Submission**

Define the HTTP endpoints and WebSocket events for accounts, communities, posts, interaction, collaboration, moderation, appeals, and AI.

Each contract must specify:

* Request and response fields.  
* Required permissions.  
* Validation and failure responses.  
* Example messages.

Draft contracts must include the draft ID, request ID, version, content, save acknowledgement, and conflict response. The coder must also define authentication, retries, and duplicate-publication prevention.

The proof of concept must match one submitted contract.

## **2.5 Code and Repository Structure**

**Coder Task — Confirm Against the Actual Repository**

| Proposed Location | Contents |
| ----- | ----- |
| frontend/ | React pages, forms, editor, and WebSocket client |
| backend/app/api/ | HTTP routes and WebSocket gateway |
| backend/app/services/ | Backend business components |
| backend/app/models/ | Database definitions |
| backend/app/repositories/ | Database queries and transactions |
| backend/tests/ and frontend/tests/ | Component and integration tests |
| docs/report/ | Final report |
| docs/diagrams/ | Editable diagrams and exports |
| docs/contracts/ | Interface specifications |
| docs/adr/ | Architecture decision records |
| config/ and .env.example | Nonsecret configuration examples |
| poc/ | Proof-of-concept implementation |
| [README.md](http://README.md) | Setup and run instructions |

The coder must confirm actual folders and assign ownership.

Database passwords, session secrets, email credentials, and AI keys must remain in backend environment variables or a secret manager. They must not appear in the repository or browser code.

## 

## 

## 

## 

## 

## 

## **2.6 Data Model**

## The ER diagram shows the records needed to support Sila’s features and policies.

## **![][image5]**

## **![][image6]**

**![][image7]**

[**https\://canva.link/mnbu5ng6gg0l7hs**](https://canva.link/mnbu5ng6gg0l7hs)

| Entity | Purpose |
| ----- | ----- |
| User | Store verified accounts and global roles |
| Community | Store community information, visibility, and official status |
| Membership | Connect users and communities with membership status and role |
| Post | Store published content, author, audience, and visibility status |
| Draft | Store shared content, version, and publication state |
| Comment | Store comments associated with posts |
| Like | Store one active like per user and post |
| OfficialRequest | Store official-community requests and review outcomes |
| Report | Store reports against posts or comments |
| Decision | Store initial moderation decisions |
| Appeal | Store appeals and their outcomes |
| AuditRecord | Store moderation and appeal action history |

**Relationships and Constraints**

* Users and communities have a many-to-many relationship through Membership.  
* Organizer roles apply to individual communities.  
* Communities contain posts and drafts; ordinary university-wide posts may have no community.  
* Posts have comments and likes.  
* Each user has at most one active like per post.  
* Each report targets exactly one post or comment.  
* Each report has at most one initial decision, and each decision has at most one appeal.  
* A draft may link to one published post; the link is unique.  
* Restricted content requires approved membership.  
* Only affected authors may appeal within seven days.  
* Ordinary users cannot modify audit records.

**Coder Task:** Finalize field types, foreign keys, indexes, authentication support records, migrations, and retention rules.

## **2.7 Architecture Decision Records**

**ADR-01 — Modular Backend**

**Context:** Sila’s features share authorization and database transactions.

**Options:** Unstructured backend, modular backend, or microservices.

**Decision:** Use one FastAPI application divided into components C1–C7.

**Consequences:** Development, deployment, and testing remain manageable. Multiple WebSocket processes would require shared event distribution.

**ADR-02 — Relational Database**

**Context:** Records have relationships, and concurrent draft saves require transactions.

**Options:** In-memory storage, SQLite, PostgreSQL, or a document database.

**Decision:** Propose PostgreSQL for the planned application.

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

**Status:** Technical decisions require coder and team confirmation before submission.

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
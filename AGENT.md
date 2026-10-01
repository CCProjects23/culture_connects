# AGENT.md
# Culture Connects Network – AI Development Agent Instructions

## 0. Mission

You are an AI development agent working on **Culture Connects Network**.

Your primary objective is:

> **Build a working, maintainable MVP as quickly as possible without sacrificing logical architecture, security, data integrity, or future extensibility.**

The project is intentionally developed in stages.

Do not attempt to implement the entire long-term Culture Connects vision at once.

The current priority is the **MVP core loop**:

```text
User
  ↓
Profile
  ↓
Topics / Interests
  ↓
Matching
  ↓
Structured Text Debate
  ↓
Debate Completion
  ↓
AI Analysis
  ↓
User Reflection / Feedback
  ↓
Repeat Encounter
```

Everything else is secondary until this loop works reliably.

---

# 1. Project Principles

## 1.1 MVP first

Always distinguish between:

- required for MVP
- useful for MVP
- future feature
- experimental idea

Do not implement future functionality merely because it appears in the project vision.

If a requested feature is not required for the current milestone, prefer creating a clean extension point rather than implementing the complete feature immediately.

---

## 1.2 Logic over complexity

Prefer:

- simple solutions
- explicit logic
- predictable behavior
- small modules
- reusable services
- clear interfaces
- minimal dependencies

Avoid:

- unnecessary abstraction
- speculative frameworks
- premature microservices
- duplicated logic
- clever code that is difficult to maintain
- over-engineering

The best implementation is usually the simplest implementation that preserves the required architecture.

---

## 1.3 Build before polishing

Development priority:

```text
Correctness
↓
Core functionality
↓
Maintainability
↓
Security
↓
Performance
↓
UX polish
```

Do not spend significant development time polishing functionality whose underlying product value has not yet been validated.

---

# 2. Source of Truth

The project documentation defines the intended product direction.

Important project documents include:

- `README.md` – project overview, stack and setup
- `ROADMAP.md` – milestone checklist (what to build now)
- `AGENT.md` – these agent instructions
- `docs/Culture_Connects_Gemeinsame_Erkenntnisse.md` – long-term vision & strategic reflection
- `docs/Culture_Connects_Onion_Service.md` – privacy/Tor concept (future)

Use the roadmap to determine what should be built now.

Use the documents in `docs/` to understand the long-term vision and strategic decisions.

When documents conflict:

1. Prefer the most recent explicit decision.
2. Prefer the MVP scope over future vision.
3. Do not silently invent a resolution.
4. Document important architectural decisions when necessary.

---

# 3. Current MVP Scope

The MVP consists primarily of:

1. Registration
2. Authentication
3. Pseudonymous user identity
4. Basic profile
5. Interests / categories
6. Topics
7. Matching
8. Structured text debate
9. Debate completion
10. AI debate analysis
11. User feedback
12. Basic personal statistics
13. Repeat encounter

These features form the first product validation loop.

---

# 4. Explicitly NOT MVP

Do not implement these unless explicitly requested or required by the current milestone:

- blockchain integration
- token system
- cryptocurrency economy
- complex rewards
- video infrastructure
- Tor / Onion infrastructure
- full professional network
- full project marketplace
- complex social-media feed
- follower system
- infinite scrolling
- advertising platform
- complex premium billing
- large creator ecosystem
- advanced international infrastructure

These are future roadmap items.

The existence of a future feature is not permission to implement it now.

---

# 5. Modular Architecture

The application should be structured so future modules can be added without rewriting the core.

Conceptual architecture:

```text
Frontend
   │
   ▼
Application / API Layer
   │
   ├── Users
   ├── Profiles
   ├── Topics
   ├── Matching
   ├── Debates
   ├── Reputation
   ├── Moderation
   └── AI
          │
          └── AI Provider Adapter
```

Future layers:

```text
Communication
    ├── Text
    ├── Voice
    └── Video

Language
    └── Translation

Community
    ├── Events
    ├── Curated Content
    └── Statistics

Projects
    └── Collaboration

Blockchain Adapter
    ├── Reputation
    ├── Rewards
    └── Attestations
```

Do not couple the core application directly to future technologies where an adapter/interface is sufficient.

---

# 6. Blockchain Policy

Blockchain is a **future optional module**.

Never introduce blockchain solely because the project contains a blockchain concept.

First identify a concrete product requirement.

Potential future use cases include:

- reputation
- rewards
- attestations
- achievements
- community contributions

If a blockchain-related abstraction is required early, use an interface such as:

```text
ReputationService
RewardService
AttestationService
```

The MVP implementation may use a normal database.

Later implementations may use blockchain adapters.

Example:

```text
ReputationService
    ├── DatabaseReputationService
    └── BlockchainReputationService
```

The application should not need to know which implementation is being used.

---

# 7. AI Architecture

AI functionality must be isolated behind a service boundary.

Prefer:

```text
DebateService
    ↓
AIAnalysisService
    ↓
AI Provider Adapter
```

Avoid scattering direct AI API calls throughout the application.

This allows:

- provider changes
- testing with mocks
- cost control
- fallback behavior
- prompt versioning
- future local models

AI output must be treated as generated data, not unquestionable truth.

---

# 8. AI Debate Analysis

The AI should primarily analyze completed debates.

Possible dimensions:

- argument quality
- logical quality
- fairness
- listening
- understanding
- factual/source handling
- similarities
- differences
- terminology differences
- learning opportunities

The AI should not automatically determine:

> “Person A is correct.”

or:

> “Person B won.”

The product goal is understanding and reflection, not ideological arbitration.

---

# 9. Observation vs Interpretation

Where AI analyzes user development, clearly distinguish:

### Observation

```text
This pattern appeared in 8 of 12 debates.
```

from:

### Interpretation / Hypothesis

```text
This may indicate that ...
```

Never present an inference about a user's internal motivation as established fact.

---

# 10. Matching

The MVP matching system should remain understandable.

Initial factors may include:

- language
- interests
- topic
- conversation duration
- desired perspective difference
- optional age group
- optional region

Conceptually:

```text
User Preferences
       ↓
Candidate Pool
       ↓
Eligibility Filtering
       ↓
Match Selection
```

Do not build a machine-learning matching system before there is sufficient real user data to justify it.

Start deterministic.

Improve later.

---

# 11. Debate Engine

The debate engine is a core domain component.

Keep debate state explicit.

Example:

```text
CREATED
   ↓
MATCHED
   ↓
WAITING
   ↓
ACTIVE
   ↓
REFLECTION
   ↓
COMPLETED
```

Avoid hidden state transitions.

Every important transition should be validated server-side.

A client must never be trusted to enforce the debate lifecycle.

---

# 12. Database Design

Priorities:

1. data integrity
2. clear relationships
3. simple queries
4. useful indexes
5. migration safety

Avoid storing structured domain information as arbitrary JSON when a relational model is more appropriate.

JSON is appropriate for genuinely flexible or provider-specific data.

Never change database structure manually in production when the framework's migration system is available.

---

# 13. API Design

APIs should be:

- explicit
- predictable
- validated
- versionable where appropriate
- documented sufficiently for frontend integration

Never expose internal database structures unnecessarily.

Use domain-oriented endpoints/services where they improve clarity.

Validate:

- authentication
- authorization
- input
- object ownership
- state transitions

on the server.

---

# 14. Security

Security is part of the implementation, not a later feature.

At minimum consider:

- authentication
- authorization
- CSRF where applicable
- input validation
- output escaping
- rate limiting
- abuse prevention
- secure secret handling
- logging
- permission boundaries
- privacy controls

Never place secrets in:

- source code
- committed configuration
- frontend bundles
- documentation

Use environment variables or the project's secret-management mechanism.

---

# 15. Privacy

Culture Connects deals with potentially sensitive conversations and personal reflections.

Therefore:

- collect only necessary data
- make visibility explicit
- separate public and private profile information
- protect private AI analysis
- require consent before publication
- support pseudonymous use
- avoid unnecessary retention
- document important privacy decisions

Do not expose internal AI profiles through public APIs.

---

# 16. Moderation

The platform is intended to allow broad disagreement.

Moderation should focus primarily on concrete behavior and clearly defined prohibited content.

Potential issues include:

- harassment
- repeated insults
- spam
- manipulation
- deliberate disruption
- abuse of reputation systems

Avoid implementing ideological classification as a moderation shortcut.

Prefer explicit behavioral rules.

---

# 17. Code Quality

Write code that another developer can understand quickly.

Prefer:

```python
def find_available_match(user, topic):
    ...
```

over overly generic abstractions whose purpose is unclear.

Use meaningful names.

Avoid:

```text
foo
bar
tmp
data2
thing
manager_final
```

unless the variable is genuinely temporary and local.

Keep functions focused.

Avoid giant files when domain boundaries are clear.

---

# 18. Dependencies

Before adding a dependency, ask:

1. Is it necessary?
2. Is there already a project dependency that solves this?
3. Is the maintenance burden justified?
4. Does it create architectural coupling?
5. Can the functionality reasonably be implemented with existing tools?

Prefer fewer dependencies.

Do not introduce libraries simply because they are popular.

---

# 19. Performance

Do not prematurely optimize.

First make the correct implementation.

Then measure.

Optimize actual bottlenecks.

However, avoid obvious performance mistakes such as:

- N+1 database queries
- loading huge datasets unnecessarily
- repeated expensive AI calls
- synchronous operations where asynchronous processing is clearly appropriate
- unnecessary network requests

AI calls should be treated as potentially expensive operations.

---

# 20. AI Cost Control

AI usage should be designed with cost awareness from the beginning.

Prefer:

- structured prompts
- limited context
- reusable summaries
- caching where safe
- asynchronous processing
- model selection based on task complexity

Do not send an entire database record or entire conversation history to an AI model if a smaller structured context is sufficient.

---

# 21. Testing Strategy

Testing priority:

### Unit tests

For:

- matching logic
- debate state transitions
- permissions
- scoring/reputation logic
- validation

### Integration tests

For:

- registration
- matching
- debate lifecycle
- AI service integration
- database interactions

### End-to-end tests

Only for the most important user journeys.

Primary E2E path:

```text
Register
→ Profile
→ Match
→ Debate
→ Complete
→ AI Analysis
→ Feedback
→ Repeat
```

Do not attempt 100% test coverage before the product has validated its core workflow.

---

# 22. Development Workflow

For every task:

## Step 1 – Understand

Read the relevant code before modifying it.

## Step 2 – Define

Identify:

- exact objective
- affected modules
- dependencies
- potential regressions

## Step 3 – Implement

Make the smallest coherent change.

## Step 4 – Test

Run the narrowest relevant tests first.

Then run broader tests if appropriate.

## Step 5 – Review

Check:

- correctness
- security
- duplication
- unnecessary complexity
- consistency with the roadmap

## Step 6 – Report

Briefly report:

- what changed
- what was tested
- known limitations
- recommended next step

---

# 23. Do Not Rewrite Working Code Without Reason

Existing working functionality should not be rewritten merely because another implementation looks cleaner.

Refactoring is justified when it:

- fixes a real problem
- removes significant duplication
- improves maintainability
- enables the next required feature
- improves security
- removes obsolete complexity

Avoid large refactors during feature work unless necessary.

---

# 24. Git Discipline

Keep commits logically focused.

Prefer:

```text
feat: add debate lifecycle
fix: validate debate completion permissions
feat: add AI analysis service
test: add matching edge cases
refactor: isolate AI provider adapter
```

Avoid giant commits containing unrelated changes.

Do not commit:

- secrets
- API keys
- local databases
- generated credentials
- private user data
- unnecessary build artifacts

---

# 25. Documentation Discipline

Do not create documentation for every trivial implementation detail.

Document:

- architecture decisions
- important domain rules
- public APIs
- non-obvious security decisions
- AI behavior
- deployment requirements
- significant deviations from the roadmap

Prefer updating an existing document over creating another document with overlapping information.

---

# 26. Definition of Done

A task is not complete merely because code exists.

A feature is considered done when:

- implementation works
- relevant validation exists
- relevant tests pass
- security implications are considered
- errors are handled
- no obvious regression is introduced
- documentation is updated when necessary

For MVP features, also ask:

> Does this contribute directly to validating the core product hypothesis?

---

# 27. Decision Rule for Ambiguous Tasks

When a request is ambiguous, choose the option that:

1. satisfies the immediate user goal
2. preserves the current architecture
3. requires the least unnecessary code
4. keeps future extension possible
5. minimizes irreversible decisions

Do not ask for clarification when a safe, obvious implementation can reasonably be made.

Ask when different interpretations would materially change architecture, data, security, or product behavior.

---

# 28. Fast-Execution Rule

The project values speed.

Therefore:

> **Prefer a small working implementation today over a theoretically perfect architecture next month.**

But speed does not mean careless shortcuts.

The acceptable shortcut is:

```text
simple implementation
+
clear module boundary
+
easy replacement later
```

The unacceptable shortcut is:

```text
temporary hack
+
hidden coupling
+
no migration path
```

---

# 29. Feature Gate

Before implementing a new feature, classify it:

```text
P0 = MVP critical
P1 = post-MVP / validation dependent
P2 = growth
P3 = long-term
```

If the feature is P1–P3 and does not enable the current milestone:

> Do not implement it unless explicitly requested.

Create an interface, placeholder, TODO, or architectural extension point only if it provides real value.

---

# 30. Current Priority Order

Until the MVP is validated:

```text
1. Core architecture
2. Authentication / users
3. Profiles
4. Topics
5. Matching
6. Debate engine
7. AI analysis
8. Reflection / feedback
9. Basic statistics
10. Repeat encounters
11. Testing
12. Pilot preparation
```

Everything else is secondary.

---

# 31. Future Feature Backlog

The following features are intentionally retained for later development.

## Communication

- Voice
- Speech-to-text
- Video

## Language

- multilingual UI
- automatic translation
- cross-language debate

## AI

- advanced matching
- challenge mode
- long-term development analysis
- personal reflection engine
- improved topic generation

## Community

- Debate of the Week
- Debate of the Month
- events
- community statistics
- curated discovery

## Growth

- organic referrals
- creator experiments
- university/community partnerships

## Collaboration

- projects
- project matching
- events
- research initiatives

## Professional

- optional professional profile
- skills discovery
- organization-facing features

## Blockchain

- reputation
- rewards
- attestations
- achievements
- ecosystem mechanisms

## Infrastructure

- advanced scaling
- distributed processing
- optional Tor / Onion service

---

# 32. The Core Product Principle

Always remember:

> **Culture Connects is not primarily a social network.**

It is a system for creating meaningful human encounters.

The desired outcome is:

> **“I understand better why this person thinks the way they do, even if I still disagree.”**

Technology exists to make that outcome easier, safer and more scalable.

---

# 33. Final Agent Rule

When in doubt:

```text
Can this be simpler?
        ↓
Can this be modular?
        ↓
Does this help the MVP?
        ↓
Can we test it?
        ↓
Can we replace it later?
```

And above all:

> **Build the smallest correct thing that moves Culture Connects toward a real-world test.**

# TaskLite MVP - TEA Risk-Based Test Design (POISED + T1T5)

## 1) Scope, Intent, and Evidence Base

This test design defines a pragmatic, MVP-scoped strategy for TaskLite using TEA principles (risk-first, traceability-first), aligned to POISED/T1T5 thinking.

### Source of truth reviewed
- `bmad-poc-tasklite/product.md`
- `bmad-poc-tasklite/architecture.md`
- `bmad-poc-tasklite/tasks.md` (currently empty)
- `bmad-poc-tasklite/app.py`
- `bmad-poc-tasklite/models.py`
- `bmad-poc-tasklite/database.py`
- `bmad-poc-tasklite/templates/index.html`
- `bmad-poc-tasklite/test-architecture.md`
- `bmad-poc-tasklite/test-cases.md`
- `bmad-poc-tasklite/tests/test_api.py`

### In scope (MVP)
- Core behavior for `POST /tasks`, `GET /tasks`, `PUT /tasks/{task_id}`
- Basic UI flow at `/` for create/list/toggle affordances
- Error handling for invalid create input and missing task update
- Persistence behavior consistency for create/toggle/list

### Out of scope (MVP)
- Authentication/authorization
- Advanced concurrency/load characteristics
- Full accessibility/cross-browser matrix
- Multi-user conflict management

## 2) Requirement-to-Test Traceability Matrix

| Req ID | Requirement (from product/architecture) | Implementation point | Risk | Current coverage | Planned tests (this design) | Gate impact |
| --- | --- | --- | --- | --- | --- | --- |
| RQ-01 | Add task with non-empty description | `POST /tasks` in `app.py` | P0 | API automated (`tests/test_api.py`) | Add boundary/value tests, schema/contract checks | Release-blocking |
| RQ-02 | Reject empty description | `POST /tasks` validation in `app.py` | P0 | API automated | Add null/missing/wrong-type payload tests | Release-blocking |
| RQ-03 | View full task list | `GET /tasks` in `app.py` | P1 | API automated | Add ordering/shape/empty-list expectations | High-confidence required |
| RQ-04 | Toggle completion and persist | `PUT /tasks/{task_id}` in `app.py` | P0 | API automated | Add idempotence sequence and persistence check via subsequent `GET` | Release-blocking |
| RQ-05 | 404 for unknown task update | `PUT /tasks/{task_id}` not-found branch | P1 | API automated | Add negative ID and invalid path parameter tests | High-confidence required |
| RQ-06 | Homepage shows tasks and allows add/toggle | `GET /` template render + JS fetch calls | P1 | Manual/smoke only | Add minimal UI/E2E smoke for add/toggle/visual state | High-confidence required |
| RQ-07 | If no tasks, show "No tasks yet" | `templates/index.html` | P2 | Not covered | Add UI assertion and implementation fix recommendation | Non-blocking for MVP if documented |
| RQ-08 | POST returns 201 Created (architecture) | `POST /tasks` response code in `app.py` | P1 (contract drift) | Not covered; opposite behavior exists | Add contract test and choose doc/code alignment action | Must be resolved or explicitly waived |

## 3) Risk Model (P0-P3)

### P0 - Critical (release blockers)
- Data integrity failure in create/toggle flow (wrong persisted state).
- Validation hole allowing empty or malformed task creation.
- Core endpoint unavailable or unstable for happy path.

### P1 - High (must be addressed for confidence)
- API contract drift (`POST /tasks` documented `201`, implemented `200`).
- List/toggle behavior deviates from expected UX state reflection.
- Error handling inconsistency for invalid/missing resources.

### P2 - Medium (can ship with documented mitigation)
- Missing explicit empty-state UI message ("No tasks yet").
- Very long description behavior undefined (no length guardrails).
- Limited semantic assertions on returned JSON structure.

### P3 - Low (defer for MVP unless easy win)
- Cosmetic UI variance and non-critical styling regressions.
- Non-critical browser-specific behavior beyond target dev browser.

## 4) Test Strategy by Level

### A) API/Integration (primary quality signal)
- Framework: `pytest` + FastAPI `TestClient` + in-memory SQLite override.
- Keep tests deterministic and isolated using dependency override from `tests/conftest.py`.
- Validate status codes, response schema shape, and persisted state transitions.
- Expand negative-path payload matrix (missing fields, `null`, wrong type, whitespace).

### B) UI/E2E (minimal but meaningful)
- One happy-path UI flow: load `/`, add task, observe rendered item, toggle via checkbox, observe completed style.
- One empty-state UI flow: no tasks present, verify explicit empty-state text.
- Keep UI assertions semantic and minimal (visible text/state), avoid brittle DOM coupling.

### C) Negative/Error-path coverage
- `POST /tasks`: whitespace-only, missing key, non-string input, oversized input (behavior observation).
- `PUT /tasks/{task_id}`: unknown ID, invalid ID format.
- Root page load with empty DB should render gracefully.

### D) NFR recommendations (MVP-scoped)
- Performance: simple response-time sanity check for list endpoint under small dataset.
- Security: input handling checks for script-like text to ensure no backend failure; output encoding review in template rendering.
- Reliability: repeat toggle sequence test (state flips consistently over multiple operations).

## 5) Entry/Exit Criteria and Quality Gates

### Entry criteria
- App runs locally with dependencies installed.
- Test DB override is active for automated tests.
- Baseline API tests execute green.

### Exit criteria
- All P0 scenarios pass in CI/local regression run.
- P1 scenarios pass, or remaining exceptions are explicitly documented with owner + due date.
- Known spec/code mismatches are resolved or formally waived.

### Quality gates
- Gate G1 (Functional Core): all P0 API tests pass.
- Gate G2 (Contract Confidence): P1 contract/error-path tests pass, including `POST /tasks` status decision.
- Gate G3 (User-visible Confidence): minimal UI smoke passes (add/list/toggle and empty-state policy).

## 6) Prioritized Test Scenarios (with rationale)

| Scenario ID | Scenario | Level | Priority | Risk mapping | Rationale |
| --- | --- | --- | --- | --- | --- |
| TS-01 | Create task with valid description persists and returns task object | API | P0 | RQ-01 | Core value path must never fail |
| TS-02 | Reject whitespace-only description | API | P0 | RQ-02 | Prevent invalid data entering system |
| TS-03 | Toggle existing task twice returns to original state and persists | API | P0 | RQ-04 | Protect state integrity over repeated operations |
| TS-04 | List returns created tasks with required fields | API | P1 | RQ-03 | Confirms retrieval contract and shape |
| TS-05 | Update unknown task returns 404 with stable error payload | API | P1 | RQ-05 | Error-path predictability for clients |
| TS-06 | POST contract check for expected create status (`201` vs `200`) | API | P1 | RQ-08 | Detect and force decision on doc/code drift |
| TS-07 | UI smoke: add + toggle updates visible state/class | UI/E2E | P1 | RQ-06 | Confirms end-user flow beyond API-only checks |
| TS-08 | Empty state message rendered when no tasks exist | UI/E2E | P2 | RQ-07 | Validates product acceptance expectation |
| TS-09 | POST payload robustness (`null`, missing field, non-string) | API | P1 | RQ-02 | Strengthens input validation boundaries |
| TS-10 | Basic response-time sanity for `GET /tasks` on small dataset | NFR | P3 | Reliability/perf | Low-cost guard against severe regressions |

## 7) Spec/Code Mismatches, Coverage Gaps, and Assumptions

### Confirmed mismatches
1. `POST /tasks` status code:
   - `bmad-poc-tasklite/architecture.md` says `201 Created`.
   - `bmad-poc-tasklite/app.py` currently returns default `200 OK`.
2. Empty-state message:
   - `bmad-poc-tasklite/product.md` expects "No tasks yet" when list is empty.
   - `bmad-poc-tasklite/templates/index.html` currently has no explicit empty-state message block.

### Coverage gaps
- No automated UI/E2E tests currently in `bmad-poc-tasklite/tests/`.
- No contract-level test enforcing chosen create-status policy.
- No explicit payload robustness matrix beyond whitespace test.
- `bmad-poc-tasklite/tasks.md` is empty, so story-level traceability is partial.

### Assumptions
- MVP favors deterministic local test execution over broad environment matrix.
- SQLite behavior is representative for current MVP needs.
- For this phase, API reliability is weighted higher than UI polish.

## 8) Suggested Automation Sequence (what to automate first, second, third)

### First wave (must-do): P0 API guardrails
- Generate/keep tests for TS-01, TS-02, TS-03.
- Ensure each includes persistence verification by follow-up read.

### Second wave (high-value): P1 contract + negative paths
- Generate tests for TS-04, TS-05, TS-06, TS-09.
- Add explicit assertion for agreed `POST /tasks` status policy.

### Third wave (confidence extension): minimal UI + light NFR
- Add UI smoke for TS-07 and TS-08.
- Add basic NFR sanity test TS-10 (non-gating unless severe).

## 9) Next Action for TEA Automate

Run TEA Automate with this exact intent:

1. **Generate/upgrade API tests** in `bmad-poc-tasklite/tests/test_api.py` to cover TS-01..TS-06 and TS-09 with deterministic fixtures from `tests/conftest.py`.
2. **Add minimal UI smoke tests** (new file, e.g. `bmad-poc-tasklite/tests/test_ui_smoke.py`) for TS-07 and TS-08 using the project's preferred UI test approach.
3. **Enforce contract decision** for `POST /tasks`:
   - Either update code to return `201`, or
   - Update architecture/docs to `200`.
   In both cases, automate a test that locks the chosen contract.
4. **Output a short execution report** listing generated tests, risk priority covered (P0/P1/P2), and any unresolved blockers.


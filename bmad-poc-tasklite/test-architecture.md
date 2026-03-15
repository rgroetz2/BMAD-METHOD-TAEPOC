# TaskLite Test Strategy

## Objective
Validate the MVP requirements for task creation, listing, and completion toggling, with primary focus on API correctness and persistence behavior.

## Scope
- In scope: FastAPI endpoints `GET /tasks`, `POST /tasks`, `PUT /tasks/{task_id}`
- In scope: input validation for task creation, not-found handling, and toggle behavior
- In scope: minimal UI rendering check for root page response and task list binding
- Out of scope: authentication, authorization, performance/load, cross-browser compatibility

## Test Levels
- Unit: model and validation behavior where practical
- Integration/API: endpoint behavior with isolated SQLite database (primary)
- Smoke/manual: basic browser verification for end-to-end flow

## Approach
- Use `pytest` + FastAPI `TestClient`
- Override database dependency to a test SQLite DB to keep tests isolated and repeatable
- Reset schema per test session and test data per test
- Verify status codes, response payloads, and state transitions

## Risk-Based Focus
- High risk: data integrity when toggling completion state
- High risk: invalid input handling (empty description)
- Medium risk: contract drift vs architecture doc (doc says `POST /tasks` -> 201; code currently returns 200)
- Medium risk: missing guardrails for very long descriptions

## Entry/Exit Criteria
- Entry: app runs locally, dependencies installed, test DB override in place
- Exit:
  - All critical API tests pass
  - Validation and not-found behavior covered
  - Known spec/code mismatches documented

## Coverage Matrix
| Requirement | Endpoint | Test Type | Status |
| --- | --- | --- | --- |
| Add task with non-empty description | `POST /tasks` | API automated | Covered |
| Reject empty task description | `POST /tasks` | API automated | Covered |
| View all tasks | `GET /tasks` | API automated | Covered |
| Toggle completed status | `PUT /tasks/{task_id}` | API automated | Covered |
| Return 404 for unknown task | `PUT /tasks/{task_id}` | API automated | Covered |


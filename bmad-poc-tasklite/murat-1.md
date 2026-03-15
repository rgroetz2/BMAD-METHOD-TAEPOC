Act as Murat, the TEA Master Test Architect.
Goal: Create a comprehensive, risk-based Test Design for the TaskLite MVP in this workspace: bmad-poc-tasklite
Use these inputs as source of truth:
bmad-poc-tasklite/product.md
bmad-poc-tasklite/architecture.md
bmad-poc-tasklite/tasks.md
bmad-poc-tasklite/app.py
bmad-poc-tasklite/models.py
bmad-poc-tasklite/database.py
bmad-poc-tasklite/templates/index.html
Existing QA docs for comparison:
bmad-poc-tasklite/test-architecture.md
bmad-poc-tasklite/test-cases.md
Context: TaskLite supports creating tasks, listing tasks, and toggling completion. Primary API endpoints:
POST /tasks
GET /tasks
PUT /tasks/{task_id}
Required output:
Requirements-to-test traceability matrix
Risk model with P0/P1/P2/P3 prioritization
Test strategy by level:
API/integration
UI/E2E (minimal but meaningful)
Negative/error-path coverage
NFR recommendations (performance/security/basic reliability), scoped for MVP
Entry/exit criteria and quality gates
Prioritized test scenarios (include rationale and risk mapping)
Explicit coverage gaps and assumptions
Suggested automation sequence (what to automate first, second, third)
Constraints:
Keep scope MVP-focused and realistic.
Highlight any spec/code mismatches (for example response codes).
Prefer maintainable, deterministic tests.
No unnecessary framework complexity.
Deliverables:
Produce a markdown design doc ready to save as: bmad-poc-tasklite/POISED-T1T5-TestDesign.md
Also provide a short “next action” section that tells me exactly what TEA Automate should generate next.
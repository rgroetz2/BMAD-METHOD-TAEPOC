# TaskLite Test Cases (API)

## TC-01 Create task with valid description
- Requirement: Add Task
- Preconditions: API is running, DB reachable
- Steps:
  1. Send `POST /tasks` with `{ "description": "Buy milk" }`
- Expected Result:
  - Status is `200` (current implementation)
  - Response contains `id`, `description = "Buy milk"`, `completed = false`
  - Task is persisted and appears in `GET /tasks`

## TC-02 Reject empty description
- Requirement: Add Task validation
- Preconditions: API is running
- Steps:
  1. Send `POST /tasks` with `{ "description": "   " }`
- Expected Result:
  - Status is `400`
  - Response detail is `Description cannot be empty`
  - No new task is created

## TC-03 List tasks
- Requirement: View Task List
- Preconditions: At least two tasks exist
- Steps:
  1. Send `GET /tasks`
- Expected Result:
  - Status is `200`
  - Response is a JSON array containing existing tasks
  - Each task has `id`, `description`, `completed`

## TC-04 Toggle task completion
- Requirement: Mark Task as Completed
- Preconditions: One task exists with `completed = false`
- Steps:
  1. Send `PUT /tasks/{id}` for that task
  2. Send `PUT /tasks/{id}` again
- Expected Result:
  - First call sets `completed = true`
  - Second call sets `completed = false`
  - Both responses return status `200`

## TC-05 Toggle non-existing task
- Requirement: Error handling for update
- Preconditions: No task exists with id `99999`
- Steps:
  1. Send `PUT /tasks/99999`
- Expected Result:
  - Status is `404`
  - Response detail is `Task not found`


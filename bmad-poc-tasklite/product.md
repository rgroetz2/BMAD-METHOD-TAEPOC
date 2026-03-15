# Product Brief

TaskLite is a minimal viable product (MVP) web application designed for simple task management. It allows users to add tasks, view a list of tasks, and mark tasks as completed. Built with a FastAPI backend for robust API handling, SQLite for persistent storage (with in-memory option for testing), and a simple HTML frontend for ease of use and quick deployment.

## Feature List

1. **Add Task**: Users can input and submit new tasks to the list.
2. **View Task List**: Users can see all current tasks in a list format.
3. **Mark Task as Completed**: Users can toggle tasks between completed and incomplete states.

## Acceptance Criteria

### Add Task
- Given the user is on the TaskLite homepage, when they enter a task description in the input field and click "Add Task", then the task should be added to the list and displayed immediately.
- The task description must not be empty.
- Tasks are stored persistently using SQLite.

### View Task List
- Given tasks exist in the system, when the user loads the page, then all tasks should be displayed in a list.
- Each task shows its description and completion status.
- If no tasks exist, a message indicating "No tasks yet" is shown.

### Mark Task as Completed
- Given a task is displayed in the list, when the user clicks on the task or a checkbox next to it, then the task's completion status should toggle.
- Completed tasks are visually distinguished (e.g., strikethrough or different color).
- The status change is persisted in storage.

# System Architecture

TaskLite follows a simple client-server architecture with separation of concerns:

- **Frontend**: A single-page HTML application with minimal JavaScript for interactivity. Serves static files and communicates with the backend via RESTful API calls.
- **Backend**: FastAPI application handling business logic, API endpoints, and data persistence.
- **Database**: SQLite for persistent storage of tasks. In-memory option available for testing or development.

The architecture is minimal to support the MVP features: adding tasks, viewing the list, and marking tasks as completed. No authentication or advanced features are included.

## API Endpoints

The backend exposes the following RESTful API endpoints:

1. **GET /tasks**
   - Description: Retrieve all tasks.
   - Response: JSON array of task objects.
   - Status: 200 OK

2. **POST /tasks**
   - Description: Create a new task.
   - Request Body: JSON object with `description` (string, required).
   - Response: JSON object of the created task.
   - Status: 201 Created
   - Validation: Description must not be empty.

3. **PUT /tasks/{task_id}**
   - Description: Toggle the completion status of a task.
   - Path Parameter: `task_id` (integer, required).
   - Response: JSON object of the updated task.
   - Status: 200 OK
   - Error: 404 Not Found if task does not exist.

## Data Model

The application uses a single entity: **Task**.

- **id**: Integer (primary key, auto-increment).
- **description**: String (required, non-empty).
- **completed**: Boolean (default: false).

Example JSON representation:
```json
{
  "id": 1,
  "description": "Buy groceries",
  "completed": false
}
```

## Project Folder Structure

```
tasklite/
├── backend/
│   ├── __init__.py
│   ├── main.py          # FastAPI app entry point
│   ├── models.py        # Pydantic models and SQLAlchemy models
│   ├── database.py      # Database setup and session management
│   └── crud.py          # CRUD operations for tasks
├── frontend/
│   ├── index.html       # Main HTML page
│   └── app.js           # JavaScript for frontend logic
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── tests/
    └── test_api.py      # Basic API tests
```

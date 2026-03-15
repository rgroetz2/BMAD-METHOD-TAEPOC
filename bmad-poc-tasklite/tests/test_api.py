def test_create_task_success(client):
    response = client.post("/tasks", json={"description": "Buy milk"})

    assert response.status_code == 200
    payload = response.json()
    assert payload["description"] == "Buy milk"
    assert payload["completed"] is False
    assert isinstance(payload["id"], int)


def test_create_task_empty_description_returns_400(client):
    response = client.post("/tasks", json={"description": "   "})

    assert response.status_code == 400
    assert response.json()["detail"] == "Description cannot be empty"


def test_read_tasks_returns_created_items(client):
    client.post("/tasks", json={"description": "Task A"})
    client.post("/tasks", json={"description": "Task B"})

    response = client.get("/tasks")

    assert response.status_code == 200
    payload = response.json()
    descriptions = [task["description"] for task in payload]
    assert "Task A" in descriptions
    assert "Task B" in descriptions


def test_update_task_toggles_completion(client):
    created = client.post("/tasks", json={"description": "Toggle me"}).json()
    task_id = created["id"]

    first_toggle = client.put(f"/tasks/{task_id}")
    second_toggle = client.put(f"/tasks/{task_id}")

    assert first_toggle.status_code == 200
    assert first_toggle.json()["completed"] is True
    assert second_toggle.status_code == 200
    assert second_toggle.json()["completed"] is False


def test_update_missing_task_returns_404(client):
    response = client.put("/tasks/99999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"


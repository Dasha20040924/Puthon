import uuid


def test_create_project_positive(api, project_data):
    response = api.create_project(project_data)

    assert response.status_code == 201, response.text
    assert response.json()["id"]


def test_create_project_negative_missing_title(api):
    response = api.create_project({"users": {}})

    assert response.status_code >= 400


def test_update_project_positive(api, created_project):
    title = f"updated-{uuid.uuid4().hex}"
    response = api.update_project(created_project, {"title": title})

    assert response.status_code in (200, 201)
    assert api.get_project(created_project).json()["title"] == title


def test_update_project_negative_unknown_id(api):
    response = api.update_project("invalid-project-id", {"title": "updated"})

    assert response.status_code >= 400


def test_get_project_positive(api, created_project):
    response = api.get_project(created_project)

    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_get_project_negative_unknown_id(api):
    response = api.get_project("invalid-project-id")

    assert response.status_code >= 400
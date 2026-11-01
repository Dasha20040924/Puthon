import os
import uuid

import pytest

from api_client import YougileApi


@pytest.fixture(scope="session")
def api():
    base_url = os.getenv("https://yougile.com/api-v2")
    token = os.getenv("n04psQuBZS4SKTyx7X7wTs-BY1BRuXhyQte2oO3fQ0QlwdCG4xc-7N-kxQk81dH4")

    if not base_url or not token:
        pytest.skip("Задайте переменные окружения YOUGILE_URL и YOUGILE_TOKEN")

    return YougileApi(base_url, token)


@pytest.fixture
def project_data():
    return {
        "title": f"pytest-{uuid.uuid4().hex}",
        "users": {},
    }


@pytest.fixture
def created_project(api, project_data):
    response = api.create_project(project_data)
    assert response.status_code == 201, response.text
    project_id = response.json()["id"]
    return project_id

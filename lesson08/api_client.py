import requests


class YougileApi:
    def __init__(self, base_url, token):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        })

    def create_project(self, data):
        return self.session.post(
            f"{self.base_url}/api-v2/projects", json=data
        )

    def update_project(self, project_id, data):
        return self.session.put(
            f"{self.base_url}/api-v2/projects/{project_id}", json=data
        )

    def get_project(self, project_id):
        return self.session.get(
            f"{self.base_url}/api-v2/projects/{project_id}"
        )

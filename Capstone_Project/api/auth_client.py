from api.base_client import BaseAPIClient
from config.config_reader import ConfigReader


class AuthClient:
    """Handle authentication and authenticated API requests."""

    def __init__(self):
        self.client = BaseAPIClient()
        config = ConfigReader()

        self.login_endpoint = config.get(
            "authentication",
            "login_endpoint"
        )
        self.me_endpoint = config.get(
            "authentication",
            "me_endpoint"
        )

        self.access_token = None

    def login(self, username, password):
        """Authenticate a user and store the access token in memory."""
        response = self.client.post(
            self.login_endpoint,
            payload={
                "username": username,
                "password": password
            }
        )

        if response.status_code == 200:
            self.access_token = response.json().get("accessToken")

        return response

    def get_auth_headers(self):
        """Return Bearer authentication headers."""
        if not self.access_token:
            raise RuntimeError(
                "Access token is not available. Login first."
            )

        return {
            "Authorization": f"Bearer {self.access_token}"
        }

    def get_current_user(self):
        """Get the currently authenticated user's details."""
        return self.client.get(
            self.me_endpoint,
            headers=self.get_auth_headers()
        )

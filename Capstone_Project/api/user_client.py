from api.base_client import BaseAPIClient


class UserClient:
    """Provide reusable methods for User Management API operations."""

    def __init__(self):
        self.client = BaseAPIClient()

    def get_users(self, params=None):
        """Get the list of users."""
        return self.client.get(
            "/users",
            params=params
        )

    def get_user(self, user_id):
        """Get a specific user by ID."""
        return self.client.get(
            f"/users/{user_id}"
        )

    def create_user(self, payload):
        """Create a simulated user."""
        return self.client.post(
            "/users/add",
            payload=payload
        )

    def update_user(self, user_id, payload):
        """Update a user."""
        return self.client.put(
            f"/users/{user_id}",
            payload=payload
        )

    def patch_user(self, user_id, payload):
        """Partially update a user."""
        return self.client.patch(
            f"/users/{user_id}",
            payload=payload
        )

    def delete_user(self, user_id):
        """Delete a user."""
        return self.client.delete(
            f"/users/{user_id}"
        )

class APIAssertions:
    """Reusable assertions for API response validation."""

    @staticmethod
    def assert_status_code(response, expected_status):
        actual_status = response.status_code

        assert actual_status == expected_status, (
            f"Expected status {expected_status}, "
            f"but received {actual_status}"
        )

    @staticmethod
    def assert_json_field_exists(response, field):
        data = response.json()

        assert field in data, (
            f"Expected JSON field '{field}' was not found"
        )

    @staticmethod
    def assert_json_field_equals(response, field, expected_value):
        data = response.json()
        actual_value = data.get(field)

        assert actual_value == expected_value, (
            f"Expected '{field}' to be '{expected_value}', "
            f"but received '{actual_value}'"
        )

    @staticmethod
    def assert_json_field_true(response, field):
        data = response.json()
        actual_value = data.get(field)

        assert actual_value is True, (
            f"Expected '{field}' to be True, "
            f"but received '{actual_value}'"
        )

    @staticmethod
    def assert_list_not_empty(response, field):
        data = response.json()
        values = data.get(field, [])

        assert values, (
            f"Expected '{field}' to contain at least one item"
        )

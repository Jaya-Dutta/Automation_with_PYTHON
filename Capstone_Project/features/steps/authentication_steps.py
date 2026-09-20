import os

from behave import given, when, then

from api.auth_client import AuthClient
from utilities.data_reader import DataReader
from utilities.assertions import APIAssertions


@given("valid authentication credentials are available")
def step_valid_credentials(context):
    data = DataReader.read_json("auth_data.json")
    valid_user = data["valid_user"]

    context.username = os.getenv(valid_user["username_env"])
    context.password = os.getenv(valid_user["password_env"])

    assert context.username, "DUMMYJSON_USERNAME is not configured"
    assert context.password, "DUMMYJSON_PASSWORD is not configured"

    context.auth_client = AuthClient()


@given("invalid authentication credentials are available")
def step_invalid_credentials(context):
    data = DataReader.read_json("auth_data.json")
    invalid_user = data["invalid_user"]

    context.username = invalid_user["username"]
    context.password = invalid_user["password"]

    context.auth_client = AuthClient()


@when("I send a login request")
def step_send_login_request(context):
    context.response = context.auth_client.login(
        context.username,
        context.password
    )


@then("the login response status should be 200")
def step_login_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then("an access token should be returned")
def step_access_token_should_be_returned(context):
    assert context.auth_client.access_token, (
        "Access token was not returned"
    )


@then("the login response should indicate authentication failure")
def step_login_should_fail(context):
    assert context.response.status_code in (400, 401), (
        f"Expected authentication failure but received "
        f"{context.response.status_code}"
    )


@given("the user is successfully authenticated")
def step_user_is_authenticated(context):
    data = DataReader.read_json("auth_data.json")
    valid_user = data["valid_user"]

    username = os.getenv(valid_user["username_env"])
    password = os.getenv(valid_user["password_env"])

    assert username, "DUMMYJSON_USERNAME is not configured"
    assert password, "DUMMYJSON_PASSWORD is not configured"

    context.auth_client = AuthClient()
    context.login_response = context.auth_client.login(
        username,
        password
    )

    APIAssertions.assert_status_code(
        context.login_response,
        200
    )


@when("I request the current authenticated user")
def step_request_current_user(context):
    context.response = context.auth_client.get_current_user()


@then("the authenticated user response status should be 200")
def step_authenticated_user_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then('the authenticated username should be "emilys"')
def step_authenticated_username_should_be_emilys(context):
    APIAssertions.assert_json_field_equals(
        context.response,
        "username",
        "emilys"
    )

from behave import when, then

from api.user_client import UserClient
from utilities.data_reader import DataReader
from utilities.assertions import APIAssertions


@when("I request the list of users")
def step_request_users(context):
    context.user_client = UserClient()
    context.response = context.user_client.get_users()


@then("the users response status should be 200")
def step_users_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then("the users list should not be empty")
def step_users_list_should_not_be_empty(context):
    APIAssertions.assert_list_not_empty(
        context.response,
        "users"
    )


@when("I request user with ID 1")
def step_request_user_by_id(context):
    context.user_client = UserClient()
    context.response = context.user_client.get_user(1)


@then("the user response status should be 200")
def step_user_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then("the returned user ID should be 1")
def step_returned_user_id_should_be_1(context):
    APIAssertions.assert_json_field_equals(
        context.response,
        "id",
        1
    )


@when("I create a user using the create user payload")
def step_create_user(context):
    data = DataReader.read_json("user_payloads.json")
    payload = data["create_user"]

    context.user_client = UserClient()
    context.response = context.user_client.create_user(payload)


@then("the create user response status should be 201")
def step_create_user_status_should_be_201(context):
    APIAssertions.assert_status_code(
        context.response,
        201
    )


@then("the created user should contain an ID")
def step_created_user_should_contain_id(context):
    APIAssertions.assert_json_field_exists(
        context.response,
        "id"
    )


@when("I update user with ID 1 using the update user payload")
def step_update_user(context):
    data = DataReader.read_json("user_payloads.json")
    payload = data["update_user"]

    context.user_client = UserClient()
    context.response = context.user_client.update_user(1, payload)


@then("the update user response status should be 200")
def step_update_user_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then("the updated user ID should be 1")
def step_updated_user_id_should_be_1(context):
    APIAssertions.assert_json_field_equals(
        context.response,
        "id",
        1
    )


@when("I patch user with ID 1 using the patch user payload")
def step_patch_user(context):
    data = DataReader.read_json("user_payloads.json")
    payload = data["patch_user"]

    context.user_client = UserClient()
    context.response = context.user_client.patch_user(1, payload)


@then("the patch user response status should be 200")
def step_patch_user_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then("the patched user ID should be 1")
def step_patched_user_id_should_be_1(context):
    APIAssertions.assert_json_field_equals(
        context.response,
        "id",
        1
    )


@when("I delete user with ID 1")
def step_delete_user(context):
    context.user_client = UserClient()
    context.response = context.user_client.delete_user(1)


@then("the delete user response status should be 200")
def step_delete_user_status_should_be_200(context):
    APIAssertions.assert_status_code(
        context.response,
        200
    )


@then("the deleted user should be marked as deleted")
def step_deleted_user_should_be_marked_deleted(context):
    APIAssertions.assert_json_field_true(
        context.response,
        "isDeleted"
    )

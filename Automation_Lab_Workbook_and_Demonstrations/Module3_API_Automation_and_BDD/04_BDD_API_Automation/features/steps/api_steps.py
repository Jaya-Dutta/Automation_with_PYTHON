import requests
from behave import given, when, then


@given("the API endpoint is available")
def step_api_available(context):
    context.base_url = "https://jsonplaceholder.typicode.com"


@when("I send a GET request for post 1")
def step_send_get_request(context):
    context.response = requests.get(
        f"{context.base_url}/posts/1",
        timeout=10
    )


@then("the response status code should be 200")
def step_verify_status_code(context):
    assert context.response.status_code == 200


@then("the response should contain post data")
def step_verify_post_data(context):
    data = context.response.json()

    assert "id" in data
    assert "title" in data
    assert "body" in data

    print("Response:", data)
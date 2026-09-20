import requests


# Test data for multiple API scenarios.
test_data = [
    {"post_id": 1, "expected_status": 200},
    {"post_id": 2, "expected_status": 200},
    {"post_id": 3, "expected_status": 200}
]


# Given: API endpoint is available.
def given_api_endpoint():
    return "https://jsonplaceholder.typicode.com/posts"


# When: Send API requests using different test data.
def when_send_requests(base_url):
    results = []

    for data in test_data:
        response = requests.get(
            f"{base_url}/{data['post_id']}",
            timeout=10
        )

        results.append((data, response))

    return results


# Then: Validate each response.
def then_validate_responses(results):
    for data, response in results:
        assert response.status_code == data["expected_status"]

        body = response.json()
        assert body["id"] == data["post_id"]

        print(
            f"Post ID: {data['post_id']} | "
            f"Status: {response.status_code} | PASS"
        )


# Execute data-driven API automation.
base_url = given_api_endpoint()
results = when_send_requests(base_url)
then_validate_responses(results)

print("\nPASS: Assignment 2 - Data-driven API automation completed.")
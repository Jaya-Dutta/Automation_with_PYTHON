import json
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

# GET
response = requests.get(f"{base_url}/1", timeout=10)
print("GET:", response.status_code, response.json())
assert response.status_code == 200

# POST
with open(
    "01_API_Automation_with_Requests/test_data/api_data.json",
    encoding="utf-8"
) as file:
    test_data = json.load(file)

post_payload = test_data["post_payload"]

response = requests.post(base_url, json=post_payload, timeout=10)
print("POST:", response.status_code, response.json())
assert response.status_code == 201

# PUT replaces the complete resource.
put_payload = {
    "title": "Updated Title",
    "body": "Updated complete resource",
    "userId": 1
}

response = requests.put(
    f"{base_url}/1",
    json=put_payload,
    timeout=10
)

print("PUT:", response.status_code, response.json())
assert response.status_code == 200

# PATCH updates only selected fields.
patch_payload = {
    "title": "Partially Updated Title"
}

response = requests.patch(
    f"{base_url}/1",
    json=patch_payload,
    timeout=10
)

print("PATCH:", response.status_code, response.json())
assert response.status_code == 200

# DELETE removes the resource.
response = requests.delete(
    f"{base_url}/1",
    timeout=10
)

print("DELETE:", response.status_code)
assert response.status_code == 200

print("\nPASS: End-to-end CRUD API flow completed.")
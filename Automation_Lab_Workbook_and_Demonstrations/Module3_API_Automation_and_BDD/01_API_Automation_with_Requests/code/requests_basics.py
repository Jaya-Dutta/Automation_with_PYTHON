import requests


# REST APIs commonly use HTTP methods such as GET, POST, PUT and DELETE.
# SOAP is XML-based and usually follows a stricter messaging structure.

url = "https://jsonplaceholder.typicode.com/posts/1"

# Send a GET request and receive the Response object.
response = requests.get(url, timeout=10)

print("===== API RESPONSE =====")

# HTTP status code: 200 means the request was successful.
print("Status Code:", response.status_code)

# Response headers contain metadata sent by the server.
print("\nContent-Type:", response.headers.get("Content-Type"))

# response.text gives the response body as a string.
print("\nResponse Text:")
print(response.text)

# response.content gives the raw response body as bytes.
print("\nResponse Content Type:", type(response.content))

# Convert JSON response into a Python dictionary.
data = response.json()

print("\nJSON Response:")
print(data)

# Basic validation.
assert response.status_code == 200
assert "id" in data
assert data["id"] == 1

print("\nPASS: GET request and response validation successful.")

# POST REQUEST
post_url = "https://jsonplaceholder.typicode.com/posts"

# Data that we want to send to the API.
payload = {
    "title": "API Automation",
    "body": "Learning POST request with Python Requests",
    "userId": 1
}

# Request headers tell the server what type of data we are sending.
headers = {
    "Content-Type": "application/json"
}

# Send POST request with JSON payload and headers.
post_response = requests.post(
    post_url,
    json=payload,
    headers=headers,
    timeout=10
)

print("\n\n===== POST API RESPONSE =====")

print("Status Code:", post_response.status_code)

print("Content-Type:", post_response.headers.get("Content-Type"))

print("\nResponse JSON:")
print(post_response.json())

# Validate successful POST response.
assert post_response.status_code == 201

post_data = post_response.json()

assert post_data["title"] == payload["title"]
assert post_data["body"] == payload["body"]
assert post_data["userId"] == payload["userId"]

print("\nPASS: POST request and response validation successful.")
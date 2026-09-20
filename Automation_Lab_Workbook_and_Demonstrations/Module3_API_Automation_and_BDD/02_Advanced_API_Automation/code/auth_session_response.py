import os
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10

COMMON_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Use environment variables for real credentials.
API_TOKEN = os.getenv("API_TOKEN", "demo-token")

session = requests.Session()
session.headers.update(COMMON_HEADERS)

# Authentication header pattern; demo API does not require a real token.
session.headers.update({
    "Authorization": f"Bearer {API_TOKEN}"
})

# Session reuses headers, cookies and connection settings.
response = session.get(
    f"{BASE_URL}/posts/1",
    timeout=TIMEOUT
)

print("Status Code:", response.status_code)
print("Session Headers:", dict(session.headers))
print("Response:", response.json())

assert response.status_code == 200

# Send a cookie with a request.
response = session.get(
    f"{BASE_URL}/cookies",
    cookies={"session_id": "demo123"},
    timeout=TIMEOUT
)

print("\nCookie Request Status:", response.status_code)

# Store and inspect session cookies.
session.cookies.set("user", "jaya")

print("Session Cookies:", session.cookies.get_dict())

response = session.get(
    f"{BASE_URL}/posts/1",
    timeout=TIMEOUT
)

print("Session Request Status:", response.status_code)

assert response.status_code == 200

session.close()

print("\nPASS: Global configuration, session, authentication pattern and cookies handled.")
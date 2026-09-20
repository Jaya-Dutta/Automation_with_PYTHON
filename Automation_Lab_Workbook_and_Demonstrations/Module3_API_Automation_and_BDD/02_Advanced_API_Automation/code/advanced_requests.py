import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url, timeout=10)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Text:", response.text[:100])
print("Content Type:", type(response.content))

response.raise_for_status()

print("JSON:", response.json())
print("PASS: Successful response handled correctly.")

# Handle an HTTP error response.
error_response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/9999",
    timeout=10
)

print("\nError Status Code:", error_response.status_code)

if error_response.status_code >= 400:
    print("Error response received.")

try:
    error_response.raise_for_status()
except requests.exceptions.HTTPError as error:
    print("Handled HTTPError:", error)

# Handle connection/timeout-related Requests exceptions.
try:
    requests.get("https://invalid.example.invalid", timeout=2)
except requests.exceptions.RequestException as error:
    print("Handled RequestException:", type(error).__name__)

# Stream response content in chunks.
stream_response = requests.get(url, stream=True, timeout=10)

total_bytes = 0

for chunk in stream_response.iter_content(chunk_size=1024):
    if chunk:
        total_bytes += len(chunk)

stream_response.close()

print("\nStreamed Bytes:", total_bytes)
print("PASS: Advanced response handling completed.")
# 02 - Advanced API Automation

This submodule covers advanced API automation techniques using Python and the Requests library.

## Objectives

* Handle successful and error API responses
* Use `raise_for_status()`
* Handle Requests exceptions
* Work with response text and binary content
* Stream response data in chunks
* Configure common headers and timeouts
* Use environment variables for authentication values
* Use `requests.Session()`
* Manage session headers and cookies

## Files

### `code/advanced_requests.py`

Covers:

* Response status handling
* Response headers
* Response text
* Binary response content
* JSON response
* `raise_for_status()`
* HTTP error handling
* Connection error handling
* `RequestException`
* Streaming with `stream=True`
* `iter_content()`

### `code/auth_session_response.py`

Covers:

* Global API configuration
* Base URL and timeout
* Common request headers
* Authentication header pattern
* Environment variables
* `requests.Session()`
* Session-level headers
* Cookies
* Session cookie storage
* Reusable session configuration

## Run

From the Module 3 root directory:

```powershell
python .\02_Advanced_API_Automation\code\advanced_requests.py
python .\02_Advanced_API_Automation\code\auth_session_response.py
```

## Result

The advanced API automation examples executed successfully.

* Successful response handling: Passed
* HTTP error handling: Passed
* Exception handling: Passed
* Streaming response: Passed
* Session configuration: Passed
* Authentication pattern: Implemented
* Cookie handling: Passed

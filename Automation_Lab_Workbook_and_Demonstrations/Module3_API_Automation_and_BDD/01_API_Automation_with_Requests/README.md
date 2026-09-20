# 01 - API Automation with Requests

This submodule covers API automation using Python and the Requests library.

## Objectives

- Understand REST and SOAP APIs
- Use Python HTTP libraries
- Install and use the Requests library
- Send GET and POST requests
- Work with JSON payloads and responses
- Validate status codes and headers
- Read response text, content and JSON
- Perform PUT, PATCH and DELETE operations
- Understand PUT vs PATCH
- Handle API payloads using reusable external test data
- Build an end-to-end API automation flow

## Files

### `code/requests_basics.py`

Covers:

- GET request
- JSON response handling
- Response object
- Status code
- Response headers
- `response.text`
- `response.content`
- POST request
- JSON payload
- Request headers
- Response validation

### `code/api_crud.py`

Covers:

- GET
- POST
- PUT
- PATCH
- DELETE
- Payload handling
- Response validation
- End-to-end CRUD flow
- External JSON test data

### `test_data/api_data.json`

Contains reusable API payload data used by the automation code.

## Run

From the Module 3 root directory:

```powershell
python .\01_API_Automation_with_Requests\code\requests_basics.py
python .\01_API_Automation_with_Requests\code\api_crud.py
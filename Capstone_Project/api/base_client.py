import requests

from config.config_reader import ConfigReader
from utilities.exceptions import APIFrameworkError
from utilities.logger import get_logger


class BaseAPIClient:
    """Reusable HTTP client for REST API requests."""

    def __init__(self):
        config = ConfigReader()

        self.base_url = config.get("api", "base_url")
        self.timeout = config.get("api", "timeout")
        self.logger = get_logger()

        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get(self, endpoint, headers=None, params=None):
        return self._request(
            method="GET",
            endpoint=endpoint,
            headers=headers,
            params=params
        )

    def post(self, endpoint, payload=None, headers=None):
        return self._request(
            method="POST",
            endpoint=endpoint,
            payload=payload,
            headers=headers
        )

    def put(self, endpoint, payload=None, headers=None):
        return self._request(
            method="PUT",
            endpoint=endpoint,
            payload=payload,
            headers=headers
        )

    def patch(self, endpoint, payload=None, headers=None):
        return self._request(
            method="PATCH",
            endpoint=endpoint,
            payload=payload,
            headers=headers
        )

    def delete(self, endpoint, headers=None):
        return self._request(
            method="DELETE",
            endpoint=endpoint,
            headers=headers
        )

    def _request(
        self,
        method,
        endpoint,
        payload=None,
        headers=None,
        params=None
    ):
        url = f"{self.base_url}{endpoint}"

        request_headers = self.headers.copy()

        if headers:
            request_headers.update(headers)

        self.logger.info(
            "Sending %s request to %s",
            method,
            endpoint
        )

        try:
            response = requests.request(
                method=method,
                url=url,
                json=payload,
                headers=request_headers,
                params=params,
                timeout=self.timeout
            )

            self.logger.info(
                "Received response status: %s for %s %s",
                response.status_code,
                method,
                endpoint
            )

            return response

        except requests.exceptions.Timeout as error:
            self.logger.error(
                "API request timed out: %s %s",
                method,
                endpoint
            )
            raise APIFrameworkError(
                f"API request timed out: {method} {url}"
            ) from error

        except requests.exceptions.ConnectionError as error:
            self.logger.error(
                "Unable to connect to API: %s %s",
                method,
                endpoint
            )
            raise APIFrameworkError(
                f"Unable to connect to API: {method} {url}"
            ) from error

        except requests.exceptions.RequestException as error:
            self.logger.error(
                "Unexpected API request error: %s %s",
                method,
                endpoint
            )
            raise APIFrameworkError(
                f"Unexpected API request error: {method} {url}"
            ) from error
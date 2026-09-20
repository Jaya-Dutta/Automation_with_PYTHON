Feature: API Automation with BDD

  Scenario: Verify a successful GET API response
    Given the API endpoint is available
    When I send a GET request for post 1
    Then the response status code should be 200
    And the response should contain post data
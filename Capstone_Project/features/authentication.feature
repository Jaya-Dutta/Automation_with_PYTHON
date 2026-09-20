Feature: User Authentication
  As an API automation tester
  I want to validate user authentication
  So that protected API operations can use a valid access token

  Scenario: Successful user login
    Given valid authentication credentials are available
    When I send a login request
    Then the login response status should be 200
    And an access token should be returned

  Scenario: Invalid user login
    Given invalid authentication credentials are available
    When I send a login request
    Then the login response should indicate authentication failure

  Scenario: Get authenticated user details
    Given the user is successfully authenticated
    When I request the current authenticated user
    Then the authenticated user response status should be 200
    And the authenticated username should be "emilys"

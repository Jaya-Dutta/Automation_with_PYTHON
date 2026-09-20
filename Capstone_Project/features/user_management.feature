Feature: User Management API
  As an API automation tester
  I want to validate User Management API operations
  So that user-related REST endpoints are tested through reusable clients

  Scenario: Get all users
    When I request the list of users
    Then the users response status should be 200
    And the users list should not be empty

  Scenario: Get a user by ID
    When I request user with ID 1
    Then the user response status should be 200
    And the returned user ID should be 1

  Scenario: Create a new user
    When I create a user using the create user payload
    Then the create user response status should be 201
    And the created user should contain an ID

  Scenario: Update an existing user
    When I update user with ID 1 using the update user payload
    Then the update user response status should be 200
    And the updated user ID should be 1

  Scenario: Partially update an existing user
    When I patch user with ID 1 using the patch user payload
    Then the patch user response status should be 200
    And the patched user ID should be 1

  Scenario: Delete an existing user
    When I delete user with ID 1
    Then the delete user response status should be 200
    And the deleted user should be marked as deleted

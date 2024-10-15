Feature: Register and Login
    As an admin
    I need to persist data from player
    So that we need to implement a connection with mongo

    Scenario: Register a player
        Given a player with name "sergio" and password "password"
        When sent a "register" POST request
        Then the player should access successfully
        And the response should contain a token

    Scenario: Login a player
        Given a player with name "sergio" and password "password"
        When sent a "login" POST request
        Then the player should access successfully
        And the response should contain a token

    Scenario: Shoud no login
        Given a player with name "sergio" and password "wrongpassword"
        When sent a "login" POST request with wrong password
        Then the player should not access successfully 

    Scenario: Delete a player
        Given a player with name "sergio" exists in the database
        When sent a "delete" DELETE request for "sergio"
        Then the player should be deleted successfully

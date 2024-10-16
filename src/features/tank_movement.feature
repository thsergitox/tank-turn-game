Feature: Tank Movement
  As a player
  I want to move my tank during the movement turn
  So that I can position it strategically

  Scenario: Move tank during movement turn
    Given it is the movement turn
    When I press the right arrow key
    Then my tank should move to the right

  Scenario: Cannot move tank during shooting turn
    Given it is the shooting turn
    When I press the right arrow key
    Then my tank should not move

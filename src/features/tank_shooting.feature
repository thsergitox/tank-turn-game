Feature: Tank Shooting
  As a player
  I want to shoot with my tank during the shooting turn
  So that I can attack my opponent

  Scenario: Shoot during shooting turn
    Given it is the shooting turn
    When I press the spacebar
    Then my tank should fire a bullet

  Scenario: Cannot shoot during movement turn
    Given it is the movement turn
    When I press the spacebar
    Then my tank should not fire a bullet

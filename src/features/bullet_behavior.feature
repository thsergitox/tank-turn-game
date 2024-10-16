Feature: Bullet Behavior
  As a player
  I want the bullets to behave realistically
  So that the game is challenging and fair

  Scenario: Bullet trajectory
    Given a tank has fired a bullet
    When the bullet is in flight
    Then it should follow a parabolic path

  Scenario: Bullet collision with tank
    Given a bullet is in flight
    When it collides with an enemy tank
    Then it should deal damage to the tank

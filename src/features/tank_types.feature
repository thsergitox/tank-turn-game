Feature: Tank Types
  As a player
  I want to choose different types of tanks
  So that I can use different strategies

  Scenario Outline: Tank characteristics
    Given I have selected a <tank_type> tank
    When I check its stats
    Then it should have <health> health
    And it should have <damage> damage
    And it should have <movement> movement range

    Examples:
      | tank_type | health | damage | movement |
      | Light     | 60     | 20     | 200      |
      | Standard  | 100    | 30     | 150      |
      | Heavy     | 150    | 50     | 100      |

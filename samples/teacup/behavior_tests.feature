# Created by houghton at 9/22/17
Feature: Extreme Conditions Test
  Extreme conditions tests check for realistic model behavior

  Scenario: Supernova
    Given the model teacup.mdl
    When Room Temperature is set to 100000
    Then Heat Loss to Room is immediately less than zero
# Created by houghton at 9/26/17
Feature: Extreme Conditions Tests
  # Enter feature description here

  Scenario: Hare Oblivion
    Given the model "Lotka_Volterra.mdl"
    When Prey is set to 0
    Then Prey Births is immediately 0
    And Prey Deaths is immediately 0
    When the model is run
    Then Predators becomes 0 at time 12
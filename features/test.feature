Feature: Selenium tests
  Skeleton for BackEnd services tests defined with Gherkin

  Scenario Outline: Example test
    When A <method> request is sent to <url>
    Then Response code is <code>
    And Response message is <message>

    Examples:
      | method | url                         | code | message      |
      | GET    | http://localhost:5000/hello | 200  | Hello world! |
Feature: DuckDuckGo
  As a Web surfer,
  I want to search for websites using plain-language phrases,
  So that I can learn more about the world around me.


  Scenario Outline: Basic DuckDuckGo Web Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "<phrase>"
    Then the search result query is "<phrase>"
    And the search result links pertain to "<phrase>"
    And the search result title contains "<phrase>"

    Examples:
      | phrase     |
      | panda      |
      | python     |
      | polar bear |
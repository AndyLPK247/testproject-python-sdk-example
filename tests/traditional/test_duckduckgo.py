"""
This module contains traditional pytest test cases.
They test searches on the DuckDuckGo website.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


# ------------------------------------------------------------
# Tests
# ------------------------------------------------------------

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  
  # Given the DuckDuckGo home page is displayed
  search_page.load()

  # When the user searches for the phrase
  search_page.search(phrase)

  # Then the search result query is the phrase
  assert phrase == result_page.search_input_value()
  
  # And the search result links pertain to the phrase
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0

  # And the search result title contains the phrase
  assert phrase in result_page.title()
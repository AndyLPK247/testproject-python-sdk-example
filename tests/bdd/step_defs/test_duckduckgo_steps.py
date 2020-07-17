"""
This module contains step definitions for BDD-style tests using pytest-bdd.
They test searches on the DuckDuckGo website.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys


# ------------------------------------------------------------
# Scenarios
# ------------------------------------------------------------

scenarios('../features/duckduckgo.feature')


# ------------------------------------------------------------
# Given Steps
# ------------------------------------------------------------

@given('the DuckDuckGo home page is displayed')
def load_duckduckgo(search_page):
  search_page.load()


# ------------------------------------------------------------
# When Steps
# ------------------------------------------------------------

@when(parsers.parse('the user searches for "{phrase}"'))
@when('the user searches for "<phrase>"')
def search_phrase(search_page, phrase):
  search_page.search(phrase)


# ------------------------------------------------------------
# Then Steps
# ------------------------------------------------------------

@then(parsers.parse('the search result query is "{phrase}"'))
@then('the search result query is "<phrase>"')
def check_search_result_query(result_page, phrase):
  assert phrase == result_page.search_input_value()


@then(parsers.parse('the search result links pertain to "{phrase}"'))
@then('the search result links pertain to "<phrase>"')
def check_search_result_links(result_page, phrase):
  titles = result_page.result_link_titles()
  matches = [t for t in titles if phrase.lower() in t.lower()]
  assert len(matches) > 0


@then(parsers.parse('the search result title contains "{phrase}"'))
@then('the search result title contains "<phrase>"')
def check_search_result_title(result_page, phrase):
  assert phrase in result_page.title()

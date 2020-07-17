"""
This module contains shared fixtures.
"""

# ------------------------------------------------------------
# Imports
# ------------------------------------------------------------

import json
import pytest

from selenium.webdriver import ChromeOptions
from src.testproject.sdk.drivers import webdriver


# ------------------------------------------------------------
# Fixtures
# ------------------------------------------------------------

@pytest.fixture
def config(scope='session'):

  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0
  assert config['testproject_projectname'] != ""
  assert config['testproject_token'] != ""

  # Return config so it can be used
  return config


@pytest.fixture
def browser(config):

  # Initialize shared arguments
  kwargs = {
    'projectname': config['testproject_projectname'],
    'token': config['testproject_token']
  }

  # Initialize the TestProject WebDriver instance
  # Note that these objects use the same API as Selenium WebDriver
  # The only thing different is the initialization call
  # Therefore, any WebDriver-based project can easily be retrofitted to use TestProject!

  if config['browser'] == 'Firefox':
    b = webdriver.Firefox(**kwargs)
  elif config['browser'] == 'Chrome':
    b = webdriver.Chrome(**kwargs)
  elif config['browser'] == 'Headless Chrome':
    opts = ChromeOptions()
    opts.add_argument('headless')
    b = webdriver.Chrome(chrome_options=opts, **kwargs)
  else:
    raise Exception(f'Browser "{config["browser"]}" is not supported')

  # Make its calls wait for elements to appear
  b.implicitly_wait(config['implicit_wait'])

  # Return the WebDriver instance for the setup
  yield b

  # Quit the WebDriver instance for the cleanup
  b.quit()
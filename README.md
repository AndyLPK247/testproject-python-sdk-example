# testproject-python-sdk-example
This repository contains example Web UI tests that use the
[TestProject Python SDK](https://github.com/testproject-io/python-sdk).


## What is Test Project?
[TestProject](https://testproject.io/) is a free end-to-end test automation platform
for Web, mobile, and API tests.
It provides:

* An in-browser recorder for building tests visually
* SDKs in Java, C#, and Python for coded automation solutions
* Add-ons that are automation building blocks developed and shared by the community
* Test dashboards and analytics hosted in the cloud

Check out TestProject's [documentation](https://docs.testproject.io/) for more information.


## TestProject Setup

Make sure your machine has the latest version of [Python](https://www.python.org/downloads/) installed,
as well as any browsers you wish to test (Chrome, Firefox, etc.). 

To set up TestProject for running the tests in this repository:

1. [Sign up](https://app.testproject.io/signup/) for a free TestProject account.
2. [Download](https://app.testproject.io/#/download) and install the TestProject agent for your operating system, or pull a container from [Docker Hub](https://hub.docker.com/r/testproject/agent).
3. Run the agent and [register it](https://docs.testproject.io/getting-started/installation-and-setup#register-the-agent) with your account.
4. Install this project's Python dependencies using `pip install requirements.txt`.
5. Set your developer token as the `testproject_token` field in the `config.json` file.


## Test Design

This repository contains a Web UI test using [pytest](https://pytest.org)
that does a basic search using [DuckDuckGo](https://duckduckgo.com/).
This test case is implemented in two ways:

1. Using a traditional pytest function under `tests/traditional`
2. Using a Gherkin feature file with [pytest-bdd](https://github.com/pytest-dev/pytest-bdd) under `tests/bdd`

Both implementations use the [TestProject Python SDK](https://github.com/testproject-io/python-sdk)
for browser automation.

Here's a brief overview of the test design:

* `config.json` contains input values such as browser type, project name, and developer token.
* `tests/conftest.py` contains pytest fixtures and hooks to set up tests and the TestProject WebDriver
* the `pages` package contains DuckDuckGo page objects that call the TestProject WebDriver
* the test cases call page objects rather than calling the TestProject WebDriver directly


## Running Tests

To run tests, execute `python -m pytest` at the command line.
You can provide path arguments to filter the tests to execute.
For example, `pytest -m pytest tests/traditional`
will execute only the traditional-style tests and not the BDD-style tests.
Once tests complete, their results should appear in the TestProject Reports dashboard online.


## Resources

* TestProject
  * [Home page](https://testproject.io/)
  * [Documentation](https://docs.testproject.io/)
  * [Python SDK GitHub repository](https://github.com/testproject-io/python-sdk)
* [Python.org](https://www.python.org/)
* [Automation Panda blog](https://automationpanda.com)

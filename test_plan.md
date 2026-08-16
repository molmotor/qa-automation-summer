# Scope
Testing the login page functionality on the-internet.herokuapp.com, plus API testing against the reqres.in REST API (GET and POST user endpoints).

# In Scope / Out of Scope
Will test: login form validation (valid/invalid username and password combinations), success/error messaging, session behavior (logout, browser back button), API GET requests for user data, API POST requests for creating a user record.
Won't test: performance/load testing, other unrelated pages on the-internet.herokuapp.com, other reqres.in endpoints beyond GET/POST users.

# Approach
- Manual testing: test cases written and executed by hand against the login page, documented in a test case table; bug reports written for defects found during manual testing.
- Automated UI testing: Selenium WebDriver with Page Object Model (POM), run via pytest, covering valid and invalid login scenarios.
- Automated API testing: Python `requests` library, run via pytest, covering GET (fetch user) and POST (create user) requests against reqres.in, checking status codes and response body content.

# Tools
Python, pytest, Selenium, Postman, requests, git/GitHub

# Pass/fail criteria
Pass: actual result matches expected result — e.g. correct error message on invalid credentials, correct success message on valid credentials, correct HTTP status code and response body on API calls.
Fail: actual result does not match expected result — e.g. wrong/missing error message, incorrect status code, unexpected response data.
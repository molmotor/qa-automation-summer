# QA Automation Portfolio — Login & API Testing

A summer project where I learned QA and test automation from scratch, using a real public demo site as the target. Covers manual testing, browser automation with Selenium, and API testing — the three main things a junior QA automation role usually asks for.

![Tests](https://github.com/molmotor/qa-automation-summer/actions/workflows/tests.yml/badge.svg)

## What's tested

Target app: the login page on [the-internet.herokuapp.com](https://the-internet.herokuapp.com/login), plus the [reqres.in](https://reqres.in) REST API.

- **15 manual test cases** covering valid/invalid login, empty fields, whitespace handling, case sensitivity, SQL-injection and XSS-style input, long input, and session/navigation behavior (logout, browser back button)
- **2 bug reports**, including a real finding around cached page content still being viewable via the browser back button after logout
- **Automated UI tests** (Selenium + pytest, using Page Object Model) covering valid and invalid login
- **Automated API tests** (Python `requests` + pytest) covering GET and POST requests, checking status codes and response data
- **4 unit tests** for a small calculator module (used early on to learn pytest basics)

Full scope and pass/fail criteria are in [`test_plan.md`](./test_plan.md).

## Tech stack

Python, pytest, Selenium, Postman, requests, git/GitHub

## Project structure

```
.
├── README.md
├── api_tests/
│   └── test_api.py           # API tests (requests + pytest)
├── manual_testing/
│   ├── bug_report_01.md
│   ├── bug_report_02.md
│   └── test_cases_login.md   # 15 manual test cases
├── requirements.txt
├── test_plan.md
├── ui_tests/
│   ├── pages/
│   │   └── login_page.py     # Page Object Model class
│   └── test_login_pom.py     # Selenium UI tests
└── unit_tests/
    ├── calculator.py
    └── test_calculator.py
```

## How to run

```bash
git clone <this-repo-url>
cd qa-automation-summer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

Note: the API tests expect a `REQRES_API_KEY` environment variable (free key from [app.reqres.in](https://app.reqres.in)):
```bash
export REQRES_API_KEY="your_key_here"
```

## What I learned

Most of this was learning Python itself while also learning QA concepts at the same time. A few specific things that stuck with me:

- The difference between a test *failing* and the thing it's testing *failing* — a test that expects an error and gets one is a passing test, not a broken one. Took a while to actually get that straight.
- Debugging real Selenium issues — my first login-check script always said "success" no matter what, because I was checking for the wrong thing (an element that exists either way, instead of checking its actual class/text). Caught that myself by re-inspecting the page.
- Refactoring a working script into Page Object Model once it made sense why it's worth the extra structure.
- Manual testing found a real (if minor) bug on its own: after logging out, hitting the browser's back button showed the old logged-in page again. Turned out to be just cached content, not an active session, but it's the kind of thing you only catch by actually poking at an app instead of only writing automated checks.

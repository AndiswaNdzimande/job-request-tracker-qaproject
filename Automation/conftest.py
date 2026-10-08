
"""
conftest.py - shared setup for the Job Request Tracker tests
=============================================================

WHAT THIS FILE IS
    pytest loads a file named exactly "conftest.py" automatically, before it runs
    the tests in this folder. It holds the SETUP code so the test file can contain
    only the CHECKS. Think of a kitchen: the test file is the recipe (what to
    check) and conftest.py is the preparation (open the app, put the tools in reach).

THE TOOLS
    pytest            The test runner: finds the tests, runs them, reports
                      PASS / FAIL / XFAIL.
    Playwright        The robot: controls a real browser (Chromium) to open the
                      page, click, type and read what is on screen.
    pytest-playwright The plugin that connects the two. It provides the `page`
                      fixture: a brand-new browser tab for every test.

FOLDER LAYOUT (conftest.py must sit next to pytest.ini, NOT inside tests/)
    Automation/
        conftest.py            <- this file
        pytest.ini             <- pytest settings
        requirements.txt       <- packages to install
        app/job-tracker-demo.html   <- the application under test
        tests/test_job_tracker.py   <- the automated checks

HOW TO RUN (from the Automation folder)
    pip install -r requirements.txt
    python -m playwright install chromium     (one-time browser download)
    python -m pytest -v                       known bugs shown as XFAIL
    python -m pytest --runxfail               shows the real failure messages

WHERE THE APP IS FOUND
    find_app() checks these places in order and uses the first file that exists:
    1. the JOB_TRACKER_PATH environment variable   2. Automation/app/
    3. the folder above Automation                 4. the Downloads folder
    If it finds nothing, the run stops with a message saying what to do.

WHAT IS IN THIS FILE
    find_app()           Returns the full path of job-tracker-demo.html.
    money_to_int(text)   Turns page text such as "R100 300" into the number
                         100300 and "R-5 000" into -5000. Whole rands only: cents
                         such as "R1 500,5" would be misread, so avoid them.
    JobTrackerPage       A "page object": one class that knows HOW to use the page,
                         so tests read like plain English and a page change is
                         fixed in one place. Its methods, in three groups:

        READING (look at the page, change nothing)
            total_budget()                 The number in the "Total budget" box.
            job_rows()                     The real job rows of the table; the
                                           "No jobs match your filters." message
                                           row is not a job and is excluded.
            job_row_count()                How many jobs the table lists
                                           (10 on a fresh page).
            budgets_in_table()             The Budget column as a list of numbers.
            count_status_in_table(status)  How many rows have the status
                                           "Pending", "In progress" or "Done".

        USING (do what a user does)
            filter_by_status(label)        Pick an option in the "All statuses"
                                           drop-down.
            open_new_request_form()        Click "+ New request" and wait until
                                           the form is open.
            fill_form(client, title, due, budget, status="Pending")
                                           Type into every form field without
                                           saving. `due` is written YYYY-MM-DD,
                                           e.g. "2026-12-01".
            click_save()                   Click "Save request" once.

        WAITING
            wait_until_save_settles()      The app fakes a slow save of about
                                           0.8 seconds ("Saving..."). This waits
                                           until the form has closed (job saved)
                                           or a real error message is shown (job
                                           rejected). It is faster and safer than
                                           a fixed sleep because it re-checks until
                                           the page is ready.

    tracker (fixture)    Opens a fresh copy of the app for each test and returns a
                         JobTrackerPage. A test asks for it by naming it as a
                         parameter: def test_x(tracker). Each test therefore starts
                         with only the original 10 jobs, like pressing F5 in manual
                         testing, and tests cannot affect each other.
"""
import os
import re
from pathlib import Path

import pytest
from playwright.sync_api import Page, expect

HERE = Path(__file__).resolve().parent
APP_NAME = "job-tracker-demo.html"
CANDIDATES = [
    os.environ.get("JOB_TRACKER_PATH"),
    HERE / "app" / APP_NAME,
    HERE.parent / APP_NAME,
    Path.home() / "Downloads" / APP_NAME,
]


# Find the app file, or stop the run with a clear message.
def find_app() -> Path:
    for candidate in CANDIDATES:
        if candidate and Path(candidate).is_file():
            return Path(candidate)
    pytest.fail(
        f"Could not find {APP_NAME}. Copy it into Automation/app/ or set the "
        "JOB_TRACKER_PATH environment variable to its full path.",
        pytrace=False,
    )


# Convert money text such as "R100 300" into a number (100300).
def money_to_int(text: str) -> int:
    return int(re.sub(r"[^\d-]", "", text))


class JobTrackerPage:
    # Wrap the Playwright browser tab so the tests can use it.
    def __init__(self, page: Page):
        self.page = page

    # Return the number shown in the "Total budget" box.
    def total_budget(self) -> int:
        text = self.page.locator("#totalBudget").inner_text()
        return money_to_int(text)

    # Return the table rows that are real jobs (not the "No jobs match" message).
    def job_rows(self):
        return self.page.locator("#rows tr").filter(has_not_text="No jobs match your filters.")

    # Return how many jobs the table currently lists.
    def job_row_count(self) -> int:
        return self.job_rows().count()

    # Return the budget of every listed job as a list of numbers.
    def budgets_in_table(self) -> list[int]:
        texts = self.job_rows().locator("td:nth-child(6)").all_inner_texts()
        return [money_to_int(t) for t in texts]

    # Return how many listed jobs have the given status.
    def count_status_in_table(self, status: str) -> int:
        return self.page.locator("#rows .pill", has_text=re.compile(rf"^{status}$")).count()

    # Choose an option in the "All statuses" drop-down.
    def filter_by_status(self, label: str):
        self.page.locator("#statusFilter").select_option(label=label)

    # Click "+ New request" and wait until the form is visible.
    def open_new_request_form(self):
        self.page.get_by_role("button", name="+ New request").click()
        expect(self.page.get_by_role("heading", name="New job request")).to_be_visible()

    # Type into every field of the New request form without saving.
    def fill_form(self, client, title, due, budget, status="Pending"):
        self.page.get_by_label("Client name").fill(client)
        self.page.get_by_label("Job title").fill(title)
        self.page.get_by_label("Due date").fill(due)
        self.page.get_by_label("Budget (R)").fill(str(budget))
        self.page.get_by_label("Status").select_option(label=status)

    # Click the "Save request" button once.
    def click_save(self):
        self.page.get_by_role("button", name="Save request").click()

    # Wait until the form has closed (saved) or a real error is shown (rejected).
    def wait_until_save_settles(self):
        self.page.wait_for_function(
            """() => {
                const dialog = document.getElementById('dlg');
                const message = document.getElementById('err').textContent;
                return !dialog.open || (message !== '' && message !== 'Saving...');
            }"""
        )


# Open a fresh copy of the app for each test and return the page helper.
@pytest.fixture
def tracker(page: Page) -> JobTrackerPage:
    page.goto(find_app().as_uri())
    expect(page.get_by_role("heading", name="Job Request Tracker")).to_be_visible()
    return JobTrackerPage(page)
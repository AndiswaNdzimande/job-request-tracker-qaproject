import os
from pathlib import Path

from playwright.sync_api import Page, expect


# Path to the supplied Job Request Tracker application.
# The confidential HTML file is NOT stored in this repository.
#
# Before running the tests, set JOB_TRACKER_PATH to the location
# of the supplied Job_traker.html file on your computer.
APP_PATH = Path(
    os.environ.get(
        "JOB_TRACKER_PATH",
        str(Path.home() / "Downloads" / "Job_traker.html")
    )
)


# ============================================================
# SETUP CHECK
# Description:
# Verify that Playwright can open the Job Request Tracker
# application and that the main page heading is visible.
#
# This is a smoke/setup check and is NOT counted as one of
# the three main automated challenge tests.
# ============================================================
def test_job_tracker_opens(page: Page):
    page.goto(APP_PATH.as_uri())

    expect(
        page.get_by_role("heading", name="Job Request Tracker")
    ).to_be_visible()


# ============================================================
# AT-001 - CREATE A VALID JOB REQUEST
# Description:
# Verify that a user can create a new job request when all
# required fields contain valid information.
#
# Expected result:
# The request should be saved and the new client and job
# should appear in the jobs table.
# ============================================================
def test_create_valid_job_request(page: Page):
    # Arrange - open the application.
    page.goto(APP_PATH.as_uri())

    # Act - open the New Job Request form.
    page.get_by_role("button", name="+ New request").click()

    # Fill in valid request information.
    page.get_by_role("textbox", name="Client name").fill(
        "Automation Test Client"
    )

    page.get_by_role(
        "textbox",
        name="Job title",
        exact=True
    ).fill(
        "Automated Test Job"
    )

    page.get_by_role(
        "textbox",
        name="Due date"
    ).fill(
        "2026-10-20"
    )

    page.get_by_role(
        "spinbutton",
        name="Budget (R)"
    ).fill(
        "5000"
    )

    # Pending is already the default status.

    # Save the request.
    page.get_by_role(
        "button",
        name="Save request"
    ).click()

    # Assert - verify that the new request appears.
    expect(
        page.get_by_text("Automation Test Client")
    ).to_be_visible()

    expect(
        page.get_by_text("Automated Test Job")
    ).to_be_visible()


# ============================================================
# AT-002 - REQUIRED CLIENT NAME VALIDATION
# Description:
# Verify that the application rejects a new job request when
# the required Client Name field is left empty.
#
# Expected result:
# The request should NOT be submitted.
# The New Job Request form should remain open.
# The message "Client name is required." should be displayed.
#
# Known defect:
# BUG-002 - The application currently displays
# "Client name is requred." instead of
# "Client name is required."
#
# Therefore, this automated test is expected to FAIL while
# BUG-002 remains unresolved.
# ============================================================
def test_client_name_is_required(page: Page):
    # Arrange - open the application.
    page.goto(APP_PATH.as_uri())

    # Act - open the New Job Request form.
    page.get_by_role(
        "button",
        name="+ New request"
    ).click()

    # Intentionally leave Client Name empty.

    # Complete the other required fields.
    page.get_by_role(
        "textbox",
        name="Job title",
        exact=True
    ).fill(
        "Automated Validation Test"
    )

    page.get_by_role(
        "textbox",
        name="Due date"
    ).fill(
        "2026-10-20"
    )

    page.get_by_role(
        "spinbutton",
        name="Budget (R)"
    ).fill(
        "5000"
    )

    # Attempt to save the incomplete request.
    page.get_by_role(
        "button",
        name="Save request"
    ).click()

    # Assert 1:
    # The form should remain open because submission was rejected.
    expect(
        page.get_by_role(
            "heading",
            name="New job request"
        )
    ).to_be_visible()

    # Assert 2:
    # Verify the correctly spelled validation message.
    #
    # This currently fails because BUG-002 causes the application
    # to display "Client name is requred."
    expect(
        page.get_by_text("Client name is required.")
    ).to_be_visible()


# ============================================================
# AT-003 - TOTAL BUDGET CALCULATION
# Description:
# Verify that the Total Budget displayed by the application
# equals the sum of the budgets for all jobs in the table.
#
# The test reads each budget directly from the table and
# calculates the expected total automatically.
#
# Expected result:
# Displayed Total Budget = Sum of all individual job budgets.
#
# Known defect:
# BUG-001 - The 10 jobs add up to R100,300, but the application
# displays R87,800.
#
# Therefore, this automated test is expected to FAIL while
# BUG-001 remains unresolved.
# ============================================================
def test_total_budget_matches_sum_of_jobs(page: Page):
    # Arrange - open the application.
    page.goto(APP_PATH.as_uri())

    # Locate all job rows in the table.
    rows = page.locator("tbody tr")

    calculated_total = 0

    # Act - read and add the Budget value from every job row.
    for index in range(rows.count()):
        row = rows.nth(index)

        # The Budget column is the sixth column (index 5).
        budget_text = row.locator("td").nth(5).inner_text()

        # Convert values such as "R18 000" into the integer 18000.
        budget_number = int(
            budget_text
            .replace("R", "")
            .replace(" ", "")
            .replace("\u00a0", "")
        )

        calculated_total += budget_number

    # Read the Total Budget displayed by the application.
    summary_text = page.locator("body").inner_text()

    # Find the content immediately after "Total budget".
    total_section = summary_text.split("Total budget", 1)[1]

    # The first line after "Total budget" contains the displayed amount.
    total_budget_text = total_section.strip().splitlines()[0]

    # Convert a value such as "R87 800" into the integer 87800.
    displayed_total = int(
        total_budget_text
        .replace("R", "")
        .replace(" ", "")
        .replace("\u00a0", "")
    )

    # Assert - compare the application's displayed total with
    # the total calculated from the individual job budgets.
    assert displayed_total == calculated_total, (
        f"Displayed Total Budget is R{displayed_total:,}, "
        f"but the jobs add up to R{calculated_total:,}."
    )
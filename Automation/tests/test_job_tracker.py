import pytest


# ============================================================
# AUTOMATED REGRESSION CHECKS - JOB REQUEST TRACKER
# Description:
# Three automated checks, chosen from the bugs found during
# manual testing.
#
#   AT-001  BUG-001  High    Total budget must equal the sum of the jobs.
#   AT-002  BUG-003  High    A negative budget must be rejected.
#   AT-003  BUG-009  Medium  The "Done" status filter must show the Done jobs.
#
# How each test is built (Arrange - Act - Assert):
#   Arrange - prepare what is needed and work out the CORRECT
#             answer ourselves.
#   Act     - do what a user would do on the page.
#   Assert  - compare what the page shows with the correct answer.
#
# The `tracker` helper (defined in conftest.py):
# Every test receives `tracker`, a freshly opened copy of the
# app containing only the original 10 jobs.
#
#   tracker.budgets_in_table()
#       The Budget column as a list of numbers.
#   tracker.total_budget()
#       The number in the "Total budget" box ("R87 800" -> 87800).
#   tracker.job_row_count()
#       How many jobs the table lists (10 on a fresh page).
#   tracker.open_new_request_form()
#       Click "+ New request" and wait for the form.
#   tracker.fill_form(client, title, due, budget, status="Pending")
#       Type into every form field without saving.
#       `due` is written as YYYY-MM-DD.
#   tracker.click_save()
#       Click "Save request" once.
#   tracker.wait_until_save_settles()
#       Wait for the app's fake 0.8 second save: until the form
#       closes (saved) or shows a real error (rejected).
#   tracker.count_status_in_table(status)
#       How many rows have the given status
#       ("Pending", "In progress" or "Done").
#   tracker.filter_by_status(label)
#       Pick an option in the "All statuses" drop-down.
#
# Why every test is marked xfail:
# Each test describes the CORRECT behaviour, and the application
# currently has the bug, so the test is expected to fail.
#
#   raises=AssertionError
#       Only a failed CHECK counts as the known bug. Any other
#       problem (file not found, timeout, wrong locator) still
#       shows as a real error and is not hidden.
#   strict=True
#       When a developer fixes the bug, the test passes and pytest
#       reports XPASS(strict) as a failure. That is the reminder
#       to remove the xfail marker.
#
# How to run (from the Automation folder; setup is explained
# in conftest.py):
#   python -m pytest -v
#       Known bugs are listed as XFAIL with their BUG ID.
#   python -m pytest --runxfail
#       Shows the real failure message of each check.
# ============================================================


# ============================================================
# AT-001 - TOTAL BUDGET CALCULATION
# Description:
# Verify that the Total Budget box displayed by the application
# equals the sum of the budgets listed in the table.
#
# Expected result:
# Displayed Total Budget = Sum of all individual job budgets.
#
# Known defect:
# BUG-001 - The Total Budget leaves out the last job in the
# list, so the displayed total is lower than the real sum.
#
# Therefore, this automated test is expected to FAIL while
# BUG-001 remains unresolved.
# ============================================================
@pytest.mark.xfail(
    raises=AssertionError, strict=True,
    reason="BUG-001: Total budget leaves out the last job in the list",
)
def test_total_budget_equals_sum_of_jobs(tracker):
    # Arrange - read every budget from the table and work out
    # the correct total ourselves.
    budgets = tracker.budgets_in_table()
    assert len(budgets) > 0, "The table should list jobs"
    expected_total = sum(budgets)

    # Act - read the Total Budget displayed by the application.
    displayed_total = tracker.total_budget()

    # Assert - the displayed total must equal the calculated total.
    assert displayed_total == expected_total, (
        f"Total budget shows R{displayed_total:,}, but the {len(budgets)} jobs "
        f"add up to R{expected_total:,} (difference R{expected_total - displayed_total:,})"
    )


# ============================================================
# AT-002 - NEGATIVE BUDGET VALIDATION
# Description:
# Verify that the application rejects a new job request when
# the Budget field contains a negative number.
#
# Expected result:
# The request should NOT be saved.
# The number of jobs in the table should stay the same.
#
# Known defect:
# BUG-003 - A negative budget is accepted and saved, so a new
# row appears in the table.
#
# Therefore, this automated test is expected to FAIL while
# BUG-003 remains unresolved.
# ============================================================
@pytest.mark.xfail(
    raises=AssertionError, strict=True,
    reason="BUG-003: a negative budget is accepted and saved",
)
def test_negative_budget_is_rejected(tracker):
    # Arrange - record how many jobs the table lists before
    # anything is added.
    jobs_before = tracker.job_row_count()

    # Act - open the New Job Request form, enter a negative
    # budget, and attempt to save.
    tracker.open_new_request_form()
    tracker.fill_form("Negative Co", "Negative Job", "2026-12-01", -5000)
    tracker.click_save()
    tracker.wait_until_save_settles()

    # Assert - the number of jobs must not have changed.
    jobs_after = tracker.job_row_count()
    assert jobs_after == jobs_before, (
        f"A job with a budget of -5000 was saved: the table went from "
        f"{jobs_before} to {jobs_after} jobs"
    )


# ============================================================
# AT-003 - DONE STATUS FILTER
# Description:
# Verify that choosing "Done" in the status filter lists every
# job that has the status Done.
#
# Expected result:
# The number of rows shown after filtering equals the number of
# Done jobs in the unfiltered table.
#
# Known defect:
# BUG-009 - The "Done" status filter shows no jobs.
#
# Therefore, this automated test is expected to FAIL while
# BUG-009 remains unresolved.
# ============================================================
@pytest.mark.xfail(
    raises=AssertionError, strict=True,
    reason="BUG-009: the 'Done' status filter shows no jobs",
)
def test_done_filter_shows_done_jobs(tracker):
    # Arrange - count the Done jobs in the unfiltered table.
    expected = tracker.count_status_in_table("Done")
    assert expected > 0, "The test data should contain at least one Done job"

    # Act - choose "Done" in the status drop-down.
    tracker.filter_by_status("Done")

    # Assert - the table must now list exactly the Done jobs.
    actual = tracker.job_row_count()
    assert actual == expected, (
        f"The Done filter shows {actual} jobs, but {expected} jobs have the status Done"
    )
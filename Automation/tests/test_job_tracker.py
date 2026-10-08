
"""
Automated regression checks for the Job Request Tracker
========================================================

THE THREE CHECKS (chosen from the bugs found in manual testing)
    AT-001  BUG-001  High    Total budget must equal the sum of the jobs.
    AT-002  BUG-003  High    A negative budget must be rejected.
    AT-003  BUG-009  Medium  The "Done" status filter must show the Done jobs.

HOW EACH TEST IS BUILT: ARRANGE - ACT - ASSERT
    Arrange  Prepare what is needed and work out the CORRECT answer ourselves.
    Act      Do what a user would do on the page.
    Assert   Compare what the page shows with the correct answer.

THE `tracker` HELPER (defined in conftest.py)
    Every test receives `tracker`: a freshly opened copy of the app (only the
    original 10 jobs). The methods used here are:
        tracker.budgets_in_table()        The Budget column as a list of numbers,
                                          e.g. [4500, 18000, ...].
        tracker.total_budget()            The number in the "Total budget" box
                                          ("R87 800" becomes 87800).
        tracker.job_row_count()           How many jobs the table lists
                                          (10 on a fresh page).
        tracker.open_new_request_form()   Click "+ New request" and wait for the form.
        tracker.fill_form(client, title, due, budget, status="Pending")
                                          Type into every form field without
                                          saving; `due` is YYYY-MM-DD.
        tracker.click_save()              Click "Save request" once.
        tracker.wait_until_save_settles() Wait for the app's fake 0.8 second save:
                                          until the form closes (saved) or shows a
                                          real error (rejected).
        tracker.count_status_in_table(s)  How many rows have status s
                                          ("Pending", "In progress" or "Done").
        tracker.filter_by_status(label)   Pick an option in the "All statuses"
                                          drop-down.

WHY EVERY TEST IS MARKED xfail
    Each test describes the CORRECT behaviour, and the application currently has
    the bug, so the test is expected to fail.
        raises=AssertionError  Only a failed CHECK counts as the known bug. Any
                               other problem (file not found, timeout, wrong
                               locator) still shows as a real error and is not
                               hidden.
        strict=True            When a developer fixes the bug, the test passes and
                               pytest reports XPASS(strict) as a failure. That is
                               the reminder to remove the xfail marker.

HOW TO RUN (from the Automation folder; setup is explained in conftest.py)
    python -m pytest -v          Known bugs are listed as XFAIL with their BUG ID.
    python -m pytest --runxfail  Shows the real failure message of each check.
"""
import pytest


# AT-001: the Total budget box must equal the sum of the budgets in the table.
@pytest.mark.xfail(
    raises=AssertionError, strict=True,
    reason="BUG-001: Total budget leaves out the last job in the list",
)
def test_total_budget_equals_sum_of_jobs(tracker):
    budgets = tracker.budgets_in_table()
    assert len(budgets) > 0, "The table should list jobs"
    expected_total = sum(budgets)

    displayed_total = tracker.total_budget()

    assert displayed_total == expected_total, (
        f"Total budget shows R{displayed_total:,}, but the {len(budgets)} jobs "
        f"add up to R{expected_total:,} (difference R{expected_total - displayed_total:,})"
    )


# AT-002: a job with a negative budget must not be added to the table.
@pytest.mark.xfail(
    raises=AssertionError, strict=True,
    reason="BUG-003: a negative budget is accepted and saved",
)
def test_negative_budget_is_rejected(tracker):
    jobs_before = tracker.job_row_count()

    tracker.open_new_request_form()
    tracker.fill_form("Negative Co", "Negative Job", "2026-12-01", -5000)
    tracker.click_save()
    tracker.wait_until_save_settles()

    jobs_after = tracker.job_row_count()
    assert jobs_after == jobs_before, (
        f"A job with a budget of -5000 was saved: the table went from "
        f"{jobs_before} to {jobs_after} jobs"
    )


# AT-003: choosing "Done" in the status filter must list every Done job.
@pytest.mark.xfail(
    raises=AssertionError, strict=True,
    reason="BUG-009: the 'Done' status filter shows no jobs",
)
def test_done_filter_shows_done_jobs(tracker):
    expected = tracker.count_status_in_table("Done")
    assert expected > 0, "The test data should contain at least one Done job"

    tracker.filter_by_status("Done")

    actual = tracker.job_row_count()
    assert actual == expected, (
        f"The Done filter shows {actual} jobs, but {expected} jobs have the status Done"
    )
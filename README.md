# Job Request Tracker - QA Challenge

> **Start here:** the test plan, test cases and bug log are combined in [Docs/QA-Submission.md](Docs/QA-Submission.md). The separate files in the Docs folder contain the same content plus the test summary report.

## Project Overview

This repository contains my Quality Assurance testing work for the **Job Request Tracker QA Challenge**.

The objective of this project is to evaluate the supplied Job Request Tracker application before release by identifying functional, validation, calculation, input-handling, usability and responsive-design issues that could affect users or data accuracy.

The project includes both **manual QA testing** and **automated browser testing**, and concludes with a final **Test Summary Report** containing a risk assessment, release recommendation and retesting guidance.

| At a glance | |
|---|---|
| Manual test cases | **42** (✅ 12 PASS, ⚠️ 10 PASS with known issue, ❌ 20 FAIL) |
| Documented defects | **16** (🔴 4 High, 🟠 8 Medium, 🟡 4 Low) |
| Observations for the product owner | 2 (OBS-01, OBS-02) |
| Automated checks | **3** (AT-001 to AT-003), each reproducing a logged defect |
| Release recommendation | 🔴 **Not ready for release** until the High-severity defects are fixed and retested |

> [!IMPORTANT]
> The supplied application file (`job-tracker-demo.html`) is **not included in this repository**. To run the automated tests you need your own authorised copy; see [Automation Setup and Execution](#automation-setup-and-execution).

Testing covers:

- Creating new job requests
- Required-field validation
- Budget validation (empty, negative, zero, decimal, very large)
- Special characters, HTML-like text and very long text
- Total Budget calculations
- Job status handling and every status filter option
- Overdue-job behaviour, including completed jobs and unusual dates
- Search functionality (casing, partial text, no result)
- Clear Filters functionality
- Job-result counts
- Duplicate submission and Cancel while saving
- Desktop usability
- Mobile/responsive behaviour
- Automated regression testing

---

# Testing Approach

Testing was performed using a **risk-based approach**, with higher-risk functionality tested before lower-impact usability issues.

The following testing techniques were used:

- Functional Testing
- Positive Testing
- Negative Testing
- Boundary Testing
- Exploratory Testing
- Responsive Testing
- Automated Browser Testing
- Regression Testing

## Control-by-control checklist

Every control on the page was listed and the same checklist was applied to each one:

| Check | Example |
|---|---|
| Empty and spaces only | Client name left empty, or three spaces |
| Boundary values | Budget of `0`, `-5000`, `1500.50`, `999999999999`; due dates in the past, today, and year `20206` |
| Special characters | `<b>Test</b>`, `O'Brien & Sons "Ltd"` |
| Very long text | 150 characters in Client name |
| Repeating the action quickly | Double-click **Save request** |
| Interrupting the action | Click **Cancel** while the request is saving |
| Every option of every drop-down | Pending, In progress **and Done** |
| Calculated values | Work out the expected figure by hand before reading the screen |

Manual testing provided broad coverage of the application. Automation was then used for selected high-value, repeatable checks rather than attempting to automate the entire manual test suite.

---

# Test Environment

## Manual Testing Environment

- **Operating System:** Windows
- **Browser:** Google Chrome Version 154.0.8037.93 (Official Build) (64-bit)
- **Application:** Job Request Tracker QA test build (`job-tracker-demo.html`)
- **Desktop Testing:** Google Chrome desktop browser
- **Mobile Testing:** Chrome DevTools Device Toolbar
- **Mobile Device:** iPhone 16
- **Mobile Viewport:** 393 × 852
- **Application Type:** Local HTML application
- **Test dates:** first session on or before 6 October 2026; second session on 8 October 2026

## Automation Environment

- **Language:** Python 3.14.2
- **Test Framework:** pytest 9.1.1
- **Browser Automation:** Playwright 1.63.0
- **pytest Playwright Plugin:** pytest-playwright 0.9.0
- **Automated Browser:** Chromium
- **Virtual Environment:** Python `venv`

---

# Manual Testing

## Manual Testing Summary

A total of **42 manual test cases** were executed.

### New Request Form

- Creating a request with valid information
- Client Name, Job Title, Due Date and Budget required validation
- Client Name with spaces only, HTML tags, special characters and 150 characters
- Job Title with HTML tags
- Negative, zero, decimal and very large budgets
- Due dates in the past, today, and with a 5-digit year
- Saving with each status (Pending, In progress, Done)
- Double-clicking **Save request**
- Cancelling before saving and while saving

### Data and Business Rules

- Total Budget calculation (original data and after adding jobs)
- Overdue-job calculation
- Treatment of completed jobs with past due dates
- A Done job with a future due date

### Search and Filtering

- Search by Client Name and by Job Title
- Search using different letter casing
- Partial text and no-match searches
- Every status filter option (Pending, In progress, Done)
- Search and status filter used together
- Clear Filters after a status filter and after a search
- Filtered job-result count

### Responsive Testing

The application was tested using Chrome DevTools with an **iPhone 16 viewport of 393 × 852**, covering the dashboard, summary boxes, search and filter controls, job table, horizontal page behaviour and access to the New Request form.

---

# Defects Identified

Testing identified **16 documented defects**. Full reproduction steps, expected and actual results (with numbers), severity reasons and evidence are in [`Docs/bug-report.md`](Docs/bug-report.md).

| Bug ID | Description | Severity | Automated |
|---|---|---|---|
| BUG-001 | Total Budget does not equal the sum of the job budgets (the newest job is left out) | 🔴 High | AT-001 |
| BUG-002 | Client name validation message contains a spelling error ("requred") | 🟡 Low | Manual |
| BUG-003 | New request form accepts a negative budget | 🔴 High | AT-002 |
| BUG-004 | Completed (Done) jobs are counted and shown as overdue | 🟠 Medium | Manual |
| BUG-005 | "Showing N jobs" line does not change when a search or filter is used | 🟠 Medium | Manual |
| BUG-006 | Search is case-sensitive (Client name and Job title) | 🟠 Medium | Manual |
| BUG-007 | Clear filters does not clear the Search box | 🟠 Medium | Manual |
| BUG-008 | Page does not fit a phone-sized screen | 🟠 Medium | Manual |
| BUG-009 | "Done" status filter always shows no jobs | 🟠 Medium | AT-003 |
| BUG-010 | Clicking Save twice creates duplicate jobs | 🔴 High | Manual |
| BUG-011 | Cancel clicked while saving still adds the job | 🟠 Medium | Manual |
| BUG-012 | HTML tags typed in Client name and Job title are interpreted instead of shown as text | 🔴 High | Manual |
| BUG-013 | A budget of 0 is accepted | 🟡 Low | Manual |
| BUG-014 | Decimal budgets are shown with one decimal place (`R1 500,5`) | 🟡 Low | Manual |
| BUG-015 | Client name has no length limit and a very long name stretches the layout | 🟡 Low | Manual |
| BUG-016 | A due date with a 5-digit year (e.g. 20206) is treated as overdue | 🟠 Medium | Manual |

## High-severity defects

### BUG-001 - Incorrect Total Budget 🔴

The 10 displayed jobs add up to **R100 300**, but the Total budget box shows **R87 800**, which is **R12 500 lower**. R12 500 is exactly the budget of the last job in the list. When a job is added, the **newest job** is the one left out (adding R1 000 shows R100 300 instead of R101 300), which points to an off-by-one error in the total calculation. Reproduced by automated test **AT-001**.

### BUG-003 - Negative Budget Accepted 🔴

A budget of `-5000` is saved and shown as `R-5 000`. Invalid financial data is stored as a real job. Reproduced by automated test **AT-002**.

### BUG-010 - Clicking Save Twice Creates Duplicate Jobs 🔴

One double-click on **Save request** creates two identical jobs (12 rows instead of 11, Open jobs 10 instead of 9). The application has no Delete button, so the duplicate cannot be removed.

### BUG-012 - HTML Typed in Text Fields Is Interpreted 🔴

`<b>Test</b>` in Client name is shown as bold **Test**, and `<i>Test</i>` in Job title as *Test*. This is a recognised security weakness (cross-site scripting).

## Observations (not counted as defects)

| ID | Observation |
|---|---|
| OBS-01 | New requests can be saved with a past or unrealistic due date (question for the product owner) |
| OBS-02 | The application has no way to edit or delete a job (suggestion; makes BUG-010 and BUG-011 worse) |

> [!NOTE]
> **The Overdue figure depends on today's date.** BUG-004 showed Overdue = 5 (expected 3) in the first session and Overdue = 6 (expected 4) on 8 October 2026. The behaviour is the same; the numbers move with the date, so expected results are written as a rule: *due date before today AND status not Done*.

---

# Automated Testing

## Automation Objective

A focused automated regression suite was created using Python, pytest, Playwright and Chromium.

The objective was not to automate every manual test case. Three checks were chosen because they cover the **two most serious defects (High)** and **one broken feature (Medium)**, and because their results do not depend on today's date.

## The three automated checks

| ID | Test function | Defect | Severity | What it checks |
|---|---|---|---|---|
| AT-001 | `test_total_budget_equals_sum_of_jobs` | BUG-001 | 🔴 High | The Total budget box equals the sum of the budgets in the table |
| AT-002 | `test_negative_budget_is_rejected` | BUG-003 | 🔴 High | A job with a budget of `-5000` is not added to the table |
| AT-003 | `test_done_filter_shows_done_jobs` | BUG-009 | 🟠 Medium | Choosing **Done** in the status filter lists every Done job |

Each test follows **Arrange - Act - Assert**: it prepares the data and works out the correct answer itself (nothing is hard-coded), does what a user would do, and compares the page with the correct answer.

## Why the tests are marked `xfail`

Each test describes the **correct** behaviour, and the application currently has the bug, so each test is marked:

```python
@pytest.mark.xfail(raises=AssertionError, strict=True, reason="BUG-001: ...")
```

- `raises=AssertionError` - only a failed **check** counts as the known bug. A missing file, a timeout or a wrong locator still shows as a real error and is not hidden.
- `strict=True` - when a developer fixes the bug, the test passes and pytest reports **XPASS(strict)** as a failure. That is the reminder to remove the `xfail` marker so the test becomes a normal regression test.

## Results

| Command | Result |
|---|---|
| `python -m pytest -v` | 🟣 **3 xfailed** - each listed with its bug ID |
| `python -m pytest --runxfail` | ❌ 3 failed - the real failure messages (below) |

| Test | Real failure message |
|---|---|
| AT-001 | `Total budget shows R87,800, but the 10 jobs add up to R100,300 (difference R12,500)` |
| AT-002 | `A job with a budget of -5000 was saved: the table went from 10 to 11 jobs` |
| AT-003 | `The Done filter shows 0 jobs, but 2 jobs have the status Done` |

The three failures represent known application defects, not problems in the automation framework.

## Automated Test Evidence

| Run | Evidence |
|---|---|
| `python -m pytest -v` (three XFAIL results with their bug IDs) | `Evidence/AT-run-1-expected-failures.png` |
| `python -m pytest --runxfail` (the real failure messages) | `Evidence/AT-run-2-failure-messages.png` |

## Automation files

| File | Purpose |
|---|---|
| `Automation/conftest.py` | Shared setup: finds the app, the `JobTrackerPage` page object (how to read and use the page) and the `tracker` fixture that opens a fresh copy of the app for each test |
| `Automation/tests/test_job_tracker.py` | The three automated checks |
| `Automation/pytest.ini` | pytest settings |
| `Automation/requirements.txt` | Packages to install |

The top of each Python file contains a docstring that explains how it works.

---

# Automation Setup and Execution

> [!IMPORTANT]
> Run every command **from the `Automation` folder**. If you run pytest from the repository root, `pytest.ini` is ignored and the bug IDs are not shown.

## Application file requirement

The original `job-tracker-demo.html` file supplied for the QA challenge is **not included in this repository**. It is treated as confidential challenge material and remains outside the repository (`Automation/app/` is listed in `.gitignore`).

The tests look for the file in this order and use the first one found:

1. The path in the `JOB_TRACKER_PATH` environment variable
2. `Automation/app/job-tracker-demo.html`  ← **recommended**
3. The folder above `Automation`
4. The `Downloads` folder

If the file is not found, the run stops with a message saying what to do.

## Windows (PowerShell)

```powershell
cd Automation
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
mkdir app
copy "$env:USERPROFILE\Downloads\job-tracker-demo.html" app\
python -m pytest -v
```

If PowerShell blocks the activation, run `Set-ExecutionPolicy -Scope Process Bypass` and activate again.

To use a file stored elsewhere:

```powershell
$env:JOB_TRACKER_PATH = "C:\path\to\job-tracker-demo.html"
```

## macOS / Linux

```bash
cd Automation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium
mkdir -p app && cp ~/Downloads/job-tracker-demo.html app/
python -m pytest -v
```

To use a file stored elsewhere:

```bash
export JOB_TRACKER_PATH=/path/to/job-tracker-demo.html
```

## Expected output

```text
tests/test_job_tracker.py::test_total_budget_equals_sum_of_jobs[chromium] XFAIL (BUG-001: Total budget leaves out the last job in the list)
tests/test_job_tracker.py::test_negative_budget_is_rejected[chromium] XFAIL (BUG-003: a negative budget is accepted and saved)
tests/test_job_tracker.py::test_done_filter_shows_done_jobs[chromium] XFAIL (BUG-009: the 'Done' status filter shows no jobs)
============ 3 xfailed ============
```

## Other useful commands

```powershell
python -m pytest --runxfail                # show the real failure message of each test
python -m pytest --runxfail --tb=line      # the same, one line per failure
python -m pytest --headed --slowmo 800     # watch the browser while the tests run
python -m pytest tests\test_job_tracker.py::test_done_filter_shows_done_jobs -v   # one test
```

(On macOS/Linux use `/` instead of `\` in the last path.)

## Troubleshooting

| Problem | Fix |
|---|---|
| `Could not find job-tracker-demo.html` | Copy the file into `Automation/app/` or set `JOB_TRACKER_PATH` |
| `ModuleNotFoundError: No module named 'conftest'` | The file must be named exactly `conftest.py` (lowercase) and sit in `Automation/`, **not** inside `tests/` |
| `Executable doesn't exist ... chromium` | Run `python -m playwright install chromium` |
| `pytest is not recognized` | Use `python -m pytest` and make sure the virtual environment is active |
| Bug IDs are not shown in the output | Run from the `Automation` folder so that `pytest.ini` is used |

---

# Assumptions

Where the supplied requirements did not explicitly define expected behaviour, reasonable QA assumptions were documented rather than presented as confirmed requirements.

1. Displayed summary values should accurately reflect the job data displayed by the application.
2. Invalid financial values (negative amounts) should not be accepted as valid job budgets.
3. A valid job budget is assumed to be greater than zero (to be confirmed).
4. Jobs with a status of `Done` should not be counted as overdue.
5. User-facing search should normally be case-insensitive.
6. Text typed by a user should be displayed exactly as typed (no HTML interpretation).
7. A new request should not be saved twice by a double-click.
8. The absence of Edit and Delete features is an observation (OBS-02), not a defect.
9. The Overdue figure depends on today's date; expected values in the documents are for 8 October 2026.

Findings based on assumptions may require confirmation from the product owner before being treated as confirmed defects.

---

# Project Structure

```text
job-request-tracker-qaproject/
|
|-- Docs/
|   |-- test-plan.md
|   |-- test-cases.md
|   |-- bug-report.md
|   `-- test-summary-report.md
|
|-- Evidence/
|   |-- AT-run-1-expected-failures.png
|   |-- AT-run-2-failure-messages.png
|   |-- BUG-001-before.png
|   |-- BUG-001-after.png
|   |-- BUG-002-client-name-validation.png
|   |-- BUG-003-negative-budget.png
|   |-- BUG-004-completed-jobs-overdue.png
|   |-- BUG-005-search-result-count.png
|   |-- BUG-006-case-sensitive-search.png
|   |-- BUG-007-clear-filters.png
|   |-- BUG-008-mobile-left-view.png
|   |-- BUG-008-mobile-right-view.png
|   |-- BUG-008-mobile-view-new-request-view.png
|   |-- BUG-009-done-filter.png
|   |-- BUG-010-duplicate-job.png
|   |-- BUG-011-cancel-still-saves.png
|   |-- BUG-012-html-rendered.png
|   |-- BUG-013-zero-budget.png
|   |-- BUG-014-decimal-budget.png
|   |-- BUG-015-long-name.png
|   |-- BUG-016-five-digit-year.png
|   
|
|-- Automation/
|   |-- conftest.py
|   |-- pytest.ini
|   |-- requirements.txt
|   |-- app/                      (your local copy of the app - NOT committed)
|   `-- tests/
|       `-- test_job_tracker.py
|
|-- .gitignore
`-- README.md
```

Add these lines to `.gitignore` so that local and confidential files are not committed:

```text
.venv/
.pytest_cache/
__pycache__/
playwright-report/
test-results/
Automation/app/
*.html
```

The supplied challenge HTML and PDF materials are also excluded.

---

# QA Documentation

The repository contains four primary QA documents together with supporting test evidence.

| Document | Contents |
|---|---|
| [`Docs/test-plan.md`](Docs/test-plan.md) | Objectives, scope, test approach (control-by-control checklist, test data approach, automation approach), priorities, environment, entry and exit criteria, assumptions |
| [`Docs/test-cases.md`](Docs/test-cases.md) | The **42 manual test cases** (ID, priority, type, test data, steps, expected and actual results, result, related defect) plus a results overview and the automated coverage table |
| [`Docs/bug-report.md`](Docs/bug-report.md) | The **16 defects** and 2 observations, each with numbered steps, expected and actual results, severity reason and evidence |
| [`Docs/test-summary-report.md`](Docs/test-summary-report.md) | Executive summary, defect and automation results, traceability, risks, limitations, release recommendation, retesting guidance and final conclusion |

---

# Test Traceability Summary

| Area | Manual Testing | Defect | Automated Coverage | Evidence |
|---|---|---|---|---|
| Total Budget calculation | Covered | BUG-001 | AT-001 | Manual + AT-run screenshots |
| Negative Budget | Covered | BUG-003 | AT-002 | Manual + AT-run screenshots |
| Status filter (Done option) | Covered | BUG-009 | AT-003 | Manual + AT-run screenshots |
| Client Name validation message | Covered | BUG-002 | Not automated | Manual evidence |
| Overdue completed jobs | Covered | BUG-004 | Not automated | Manual evidence |
| Result count | Covered | BUG-005 | Not automated | Manual evidence |
| Case-sensitive search | Covered | BUG-006 | Not automated | Manual evidence |
| Clear Filters | Covered | BUG-007 | Not automated | Manual evidence |
| Mobile responsiveness | Covered | BUG-008 | Not automated | Manual evidence |
| Double-click Save | Covered | BUG-010 | Not automated | Manual evidence |
| Cancel while saving | Covered | BUG-011 | Not automated | Manual evidence |
| HTML in text fields | Covered | BUG-012 | Not automated | Manual evidence |
| Zero / decimal budget | Covered | BUG-013, BUG-014 | Not automated | Manual evidence |
| Long text | Covered | BUG-015 | Not automated | Manual evidence |
| Due date with a 5-digit year | Covered | BUG-016 | Not automated | Manual evidence |

The automated suite intentionally focuses on selected high-value regression scenarios rather than duplicating the complete manual test suite.

---

# Current Project Status

## ✅ Completed

- Test planning
- Manual functional, positive, negative, boundary and exploratory testing
- Control-by-control checklist applied to every control
- Desktop and mobile/responsive testing
- **42 documented manual test cases**
- **16 documented defects** and 2 observations
- Manual screenshot evidence
- Python automation environment (pytest, Playwright, Chromium)
- AT-001, AT-002 and AT-003 automated checks with `xfail` tracking
- Automated execution evidence
- Manual and automated QA documentation
- Test-to-defect traceability
- Final QA Test Summary Report with risk assessment, release recommendation and retesting recommendations

## 🔜 Possible next steps

- Automate BUG-010 (double-click Save) and BUG-012 (HTML in text fields)
- Control the clock so that the date-dependent overdue defects (BUG-004, BUG-016) can be automated
- Retest everything once the defects are fixed

## Final Status

The planned QA work for this challenge is **complete**. The repository contains the manual testing documentation, defect reports, supporting evidence, automated regression tests, final Test Summary Report, and release recommendation.

---

# Repository Note

The original Job Request Tracker HTML file supplied for the QA challenge is **not included in this repository**. It is treated as confidential test material and is kept outside the repository.

The repository contains only the QA work created for the challenge:

- Test Plan
- 42 manual test cases
- 16 documented defect reports and 2 observations
- Manual and automated test evidence
- Python/Playwright automated test code
- Automation dependencies
- Final QA Test Summary Report
- Project README

The supplied challenge PDFs and HTML application are excluded through `.gitignore`. This keeps confidential challenge material separate from the QA deliverables while still allowing an authorised tester with a local copy of `job-tracker-demo.html` to execute the automated tests.

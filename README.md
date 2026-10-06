# Job Request Tracker - QA Challenge

## Project Overview

This repository contains my Quality Assurance testing work for the **Job Request Tracker QA Challenge**.

The objective of this project is to evaluate the supplied Job Request Tracker application before release by identifying functional, validation, calculation, usability, and responsive-design issues that could affect users.

The project includes both **manual QA testing** and **automated browser testing**, and concludes with a final **Test Summary Report** containing a risk assessment and release recommendation.

Manual testing was used to explore the application, validate expected behaviour, identify defects, test edge cases, and capture supporting evidence.

A focused automated regression suite was then implemented using **Python, pytest, and Playwright** to verify selected high-value application behaviours and reproduce important defects identified during manual testing.

Testing covers:

- Creating new job requests
- Required-field validation
- Budget validation
- Total Budget calculations
- Job status handling
- Overdue-job behaviour
- Search functionality
- Status filtering
- Clear Filters functionality
- Job-result counts
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

Manual testing provided broad coverage of the application.

Automation was then used for selected high-value and repeatable checks rather than attempting to automate the entire manual test suite.

---

# Test Environment

## Manual Testing Environment

- **Operating System:** Windows
- **Browser:** Google Chrome
- **Application:** Job Request Tracker QA test build
- **Desktop Testing:** Google Chrome desktop browser
- **Mobile Testing:** Chrome DevTools Device Toolbar
- **Mobile Device:** iPhone 16
- **Mobile Viewport:** 393 × 852
- **Application Type:** Local HTML application

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

A total of **17 manual test cases** were executed.

### New Request Form

Testing included:

- Creating a request with valid information
- Client Name required validation
- Job Title required validation
- Due Date required validation
- Budget required validation
- Negative budget handling
- Zero budget boundary testing
- Cancelling a new request
- Creating a request with an `In progress` status

### Data and Business Rules

Testing included:

- Total Budget calculation
- Overdue-job calculation
- Treatment of completed jobs with past due dates

### Search and Filtering

Testing included:

- Search by Client Name
- Search by Job Title
- Search using different letter casing
- Status filtering
- Clear Filters functionality
- Filtered job-result count

### Responsive Testing

The application was tested using Chrome DevTools with an **iPhone 16 viewport of 393 × 852**.

The mobile test included:

- Dashboard visibility
- Summary information
- Search and filter controls
- Job table usability
- Horizontal page behaviour
- Access to the New Request form

---

# Defects Identified

Manual testing identified **8 documented defects**.

## BUG-001 - Incorrect Total Budget

**Severity: High**

The 10 displayed jobs have the following budgets:

- R4,500
- R18,000
- R9,600
- R3,200
- R2,800
- R7,500
- R5,200
- R22,000
- R15,000
- R12,500

The correct combined total is:

**R100,300**

The application displays:

**R87,800**

The displayed Total Budget is therefore **R12,500 lower** than the sum of the displayed job budgets.

This defect was also reproduced by automated test **AT-003**.

---

## BUG-002 - Client Name Validation Message Contains a Spelling Error

**Severity: Low**

Client Name validation correctly prevents submission when the field is empty.

However, the application displays:

`Client name is requred.`

instead of:

`Client name is required.`

The validation functionality works, but the user-facing message contains a spelling error.

This defect was also reproduced by automated test **AT-002**.

---

## BUG-003 - Negative Budget Values Are Accepted

**Severity: High**

The New Request form accepts negative budget values.

For example:

`-5000`

can be saved successfully and is displayed as:

`R-5 000`

Invalid financial data should not be accepted as a valid job budget.

---

## BUG-004 - Completed Jobs Are Counted and Displayed as Overdue

**Severity: Medium**

Based on the documented QA assumption that a completed job should no longer be considered overdue, the application includes completed jobs with past due dates in the Overdue count.

The application displays:

**5 overdue jobs**

while only:

**3 jobs**

are both overdue and unfinished.

This finding depends on the expected business rule and should be confirmed with the product owner.

---

## BUG-005 - Job Result Count Does Not Update When Filters Are Applied

**Severity: Medium**

Search and Status filtering correctly reduce the jobs displayed in the table.

However, the result counter continues to display:

`Showing 10 jobs`

even when fewer jobs are visible.

For example, searching for:

`Kestrel Motors`

displays two matching jobs while the counter continues to show 10 jobs.

---

## BUG-006 - Search Is Case-Sensitive

**Severity: Medium**

Searching for:

`Kestrel Motors`

returns the expected matching jobs.

Searching for:

`kestrel motors`

returns:

`No jobs match your filters.`

This finding is based on the QA assumption that a user-facing search should normally behave in a case-insensitive manner.

---

## BUG-007 - Clear Filters Does Not Clear the Search Field

**Severity: Medium**

Clicking **Clear filters** resets the Status filter to:

`All statuses`

but does not clear the Search field.

The existing search term remains active and the table therefore remains filtered.

---

## BUG-008 - Poor Mobile Responsiveness

**Severity: Medium**

When tested using an iPhone 16 viewport of **393 × 852**, the application remains wider than the available screen.

The user must horizontally drag across the page to access information and controls including:

- Total Budget
- New Request
- Status filter
- Clear Filters
- Due Date
- Status
- Budget

The functionality remains accessible, but the layout provides a poor mobile user experience.

---

## Defect Summary

| Bug ID | Description | Severity | Automation |
|---|---|---|---|
| BUG-001 | Total Budget does not equal the sum of displayed job budgets | High | Reproduced by AT-003 |
| BUG-002 | Client Name validation message contains a spelling error | Low | Reproduced by AT-002 |
| BUG-003 | Negative budget values are accepted | High | Manual |
| BUG-004 | Completed jobs are counted and displayed as overdue | Medium | Manual |
| BUG-005 | Job result count does not update after filtering | Medium | Manual |
| BUG-006 | Search is case-sensitive | Medium | Manual |
| BUG-007 | Clear Filters does not clear Search | Medium | Manual |
| BUG-008 | Poor responsiveness on phone-sized screens | Medium | Manual |

---

# Automated Testing

## Automation Objective

A focused automated regression suite was created using:

- Python
- pytest
- Playwright
- Chromium

The objective was not to automate every manual test case.

Instead, automation focuses on a small number of important, repeatable behaviours that provide meaningful regression coverage.

The automated tests are located in:

`Automation/tests/test_job_tracker.py`

---

## Automation Setup Check

Before executing the primary automated tests, a smoke test verifies that Playwright can successfully open the Job Request Tracker.

### Test

`test_job_tracker_opens`

### Expected Result

The application opens and the **Job Request Tracker** heading is visible.

### Current Result

**PASS**

---

## AT-001 - Create a Valid Job Request

### Purpose

Verify that a user can successfully create a new job request when all required fields contain valid information.

### Automated Steps

The test:

1. Opens the application.
2. Clicks **+ New request**.
3. Enters a valid Client Name.
4. Enters a valid Job Title.
5. Enters a Due Date.
6. Enters a valid Budget.
7. Leaves the default status as `Pending`.
8. Clicks **Save request**.
9. Verifies that the new Client Name appears.
10. Verifies that the new Job Title appears.

### Expected Result

The request should be saved and displayed in the jobs table.

### Current Result

**PASS**

### Evidence

`Evidence/AT-001-create-valid-job-pass.png`

---

## AT-002 - Required Client Name Validation

### Purpose

Verify that the application rejects a new job request when the required Client Name field is empty.

### Automated Steps

The test:

1. Opens the application.
2. Opens the New Request form.
3. Leaves Client Name empty.
4. Completes the other required fields.
5. Attempts to save the request.
6. Verifies that the form remains open.
7. Verifies that the correct validation message is displayed.

### Expected Result

The application should display:

`Client name is required.`

### Actual Result

The application displays:

`Client name is requred.`

### Current Result

**FAIL - Known defect BUG-002**

The application correctly prevents the incomplete request from being submitted, but the validation message contains a spelling error.

The automated test intentionally continues to assert the correct expected behaviour instead of accepting the defective text.

### Evidence

`Evidence/AT-002-client-validation-fail.png`

---

## AT-003 - Total Budget Calculation

### Purpose

Verify that the Total Budget displayed by the application equals the sum of the individual job budgets displayed in the table.

### Automated Approach

The test does not hard-code **R100,300** as the expected result.

Instead, Playwright reads the Budget value from every displayed job row.

Python then converts the displayed budget values into numbers and calculates the total independently.

The automated calculation produces:

**R100,300**

The application displays:

**R87,800**

### Expected Result

The displayed Total Budget should equal the calculated sum of all job budgets.

### Actual Result

**Displayed Total Budget:** R87,800

**Calculated Total Budget:** R100,300

**Difference:** R12,500

### Current Result

**FAIL - Known defect BUG-001**

This automated test independently reproduces the Total Budget defect identified during manual testing.

### Evidence

`Evidence/AT-003-total-budget-fail.png`

---

## Automated Test Results

| Test | Purpose | Result | Related Defect |
|---|---|---|---|
| Setup Check | Verify application opens | PASS | None |
| AT-001 | Create valid job request | PASS | None |
| AT-002 | Required Client Name validation | FAIL | BUG-002 |
| AT-003 | Total Budget calculation | FAIL | BUG-001 |

The current complete automated test suite therefore contains **4 checks**:

- **2 Passed**
- **2 Failed**

The two failing tests represent known application defects rather than failures in the automation framework.

The tests intentionally continue to assert the correct expected behaviour so that they can become passing regression tests once the application defects are fixed.

---

## Automated Test Evidence

Evidence from the Playwright automated test execution is stored in the `Evidence/` directory.

| Automated Test | Result | Related Defect | Evidence |
|---|---|---|---|
| AT-001 - Create valid job request | PASS | None | `Evidence/AT-001-create-valid-job-pass.png` |
| AT-002 - Client Name validation | FAIL | BUG-002 | `Evidence/AT-002-client-validation-fail.png` |
| AT-003 - Total Budget calculation | FAIL | BUG-001 | `Evidence/AT-003-total-budget-fail.png` |

AT-002 and AT-003 intentionally assert the expected correct behaviour of the application. Their failures reproduce defects identified during manual testing rather than failures in the automation framework.

- **AT-002 / BUG-002:** The application prevents submission when the Client Name is empty, but displays `Client name is requred.` instead of `Client name is required.`
- **AT-003 / BUG-001:** The application displays a Total Budget of `R87,800`, while the automated test calculates `R100,300` from the individual job budgets.

---

# Automation Setup and Execution

## Important Application File Requirement

The original:

`Job_traker.html`

file supplied for the QA challenge is **not included in this repository**.

It is treated as confidential challenge material and remains outside the GitHub repository.

The automated tests require the tester to have an authorised local copy of this file.

By default, the automation looks for:

`Job_traker.html`

inside the current user's Downloads folder.

For example:

```text
C:\Users\<username>\Downloads\Job_traker.html
```

A different location can be supplied using the `JOB_TRACKER_PATH` environment variable.

Example using PowerShell:

```powershell
$env:JOB_TRACKER_PATH="C:\path\to\Job_traker.html"
```

---

## 1. Navigate to the Automation Directory

From the repository root:

```powershell
cd Automation
```

---

## 2. Create a Python Virtual Environment

```powershell
python -m venv .venv
```

---

## 3. Activate the Virtual Environment

Using PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation for the current session, the execution policy can be adjusted for that process according to the user's local security policy.

---

## 4. Install Dependencies

```powershell
python -m pip install -r requirements.txt
```

---

## 5. Install Chromium

```powershell
python -m playwright install chromium
```

---

## 6. Run the Complete Automated Test Suite

```powershell
python -m pytest tests\test_job_tracker.py -v
```

---

## Run Individual Tests

### Setup Check

```powershell
python -m pytest tests\test_job_tracker.py::test_job_tracker_opens -v
```

### AT-001

```powershell
python -m pytest tests\test_job_tracker.py::test_create_valid_job_request -v
```

### AT-002

```powershell
python -m pytest tests\test_job_tracker.py::test_client_name_is_required -v
```

### AT-003

```powershell
python -m pytest tests\test_job_tracker.py::test_total_budget_matches_sum_of_jobs -v
```

---

# Assumptions

Where the supplied requirements did not explicitly define expected behaviour, reasonable QA assumptions were documented rather than presented as confirmed requirements.

The main assumptions used during testing were:

1. Displayed summary values should accurately reflect the job data displayed by the application.
2. Invalid financial values should not be accepted as valid job budgets.
3. A valid job budget is assumed to be greater than zero.
4. Jobs with a status of `Done` should not continue to be counted as overdue.
5. User-facing search functionality should normally be case-insensitive.

Findings based on assumptions may require confirmation from the product owner before being treated as confirmed defects.

---

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
|   |-- AT-001-create-valid-job-pass.png
|   |-- AT-002-client-validation-fail.png
|   |-- AT-003-total-budget-fail.png
|   |-- BUG-001-after.png
|   |-- BUG-001-before.png
|   |-- BUG-002-client-name-validation.png
|   |-- BUG-003-negative-budget.png
|   |-- BUG-004-completed-jobs-overdue.png
|   |-- BUG-005-search-result-count.png
|   |-- BUG-006-case-sensitive-search.png
|   |-- BUG-007-clear-filters.png
|   |-- BUG-008-mobile-left-view.png
|   |-- BUG-008-mobile-right-view.png
|   |-- BUG-008-mobile-view-new-request-view.png
|   `-- Job-title-is-required.png
|
|-- Automation/
|   |-- tests/
|   |   `-- test_job_tracker.py
|   `-- requirements.txt
|
|-- .gitignore
`-- README.md
```

The following local/generated files are intentionally excluded from Git:

```text
.venv/
.pytest_cache/
__pycache__/
playwright-report/
test-results/
```

The supplied challenge HTML and PDF materials are also excluded.

---

# QA Documentation

The repository contains four primary QA documents together with supporting test evidence.

## Test Plan

`Docs/test-plan.md`

Defines the overall QA strategy and contains:

- Testing objectives
- Scope
- Test approach
- Test priorities
- Test environment
- Entry criteria
- Exit criteria
- Assumptions
- Limitations

---

## Test Cases

`Docs/test-cases.md`

Contains the **17 documented manual test cases**, including:

- Test ID
- Priority
- Test type
- Test data
- Test steps
- Expected result
- Actual result
- Test result
- Related defect references

---

## Bug Report

`Docs/bug-report.md`

Contains the **8 documented defects**, including:

- Bug ID
- Severity
- Environment
- Steps to reproduce
- Expected result
- Actual result
- Severity reasoning
- Supporting evidence

---

## Test Summary Report

`Docs/test-summary-report.md`

Provides the final consolidated QA assessment for the project.

The report contains:

- Executive summary
- Testing objectives
- Test scope
- Test approach
- Test environment
- Manual test execution summary
- Defect summary
- High-, Medium-, and Low-severity findings
- Automated testing summary
- Automated test results
- Manual and automated evidence references
- Test traceability
- QA assumptions
- Testing limitations
- Risk assessment
- Release recommendation
- Retesting recommendations
- Final QA conclusion

The Test Summary Report brings together the results of the complete manual and automated testing process and provides the final release assessment for the Job Request Tracker.

---

## Evidence

The `Evidence` directory contains screenshots captured during **manual and automated testing** to support the documented findings and test results.

Manual evidence is provided for findings including:

- Incorrect Total Budget
- Client Name validation spelling
- Negative budget acceptance
- Completed jobs included as overdue
- Incorrect filtered result count
- Case-sensitive search
- Clear Filters behaviour
- Mobile responsiveness

Automated execution evidence is provided for:

- AT-001 - Successful valid job creation
- AT-002 - Client Name validation defect reproduction
- AT-003 - Total Budget defect reproduction

---

# Test Traceability Summary

The project maintains traceability between manual testing, identified defects, automated regression checks, and supporting evidence.

| Area | Manual Testing | Defect | Automated Coverage | Evidence |
|---|---|---|---|---|
| Valid job creation | Covered | None | AT-001 | AT-001 screenshot |
| Client Name validation | Covered | BUG-002 | AT-002 | Manual + AT-002 screenshots |
| Total Budget calculation | Covered | BUG-001 | AT-003 | Manual + AT-003 screenshots |
| Negative Budget | Covered | BUG-003 | Not automated | Manual evidence |
| Overdue completed jobs | Covered | BUG-004 | Not automated | Manual evidence |
| Result count | Covered | BUG-005 | Not automated | Manual evidence |
| Case-sensitive search | Covered | BUG-006 | Not automated | Manual evidence |
| Clear Filters | Covered | BUG-007 | Not automated | Manual evidence |
| Mobile responsiveness | Covered | BUG-008 | Not automated | Manual evidence |

The automated suite intentionally focuses on selected high-value regression scenarios rather than duplicating the complete manual test suite.

---

---

# Current Project Status

## Completed

- Test planning
- Manual functional testing
- Positive testing
- Negative testing
- Boundary testing
- Exploratory testing
- Desktop testing
- Mobile/responsive testing
- **17 documented manual test cases**
- **8 documented defects**
- Manual screenshot evidence
- Python automation environment
- pytest setup
- Playwright setup
- Chromium installation
- Automated application smoke test
- AT-001 valid request automation
- AT-002 validation automation
- AT-003 Total Budget automation
- Automated execution evidence
- Automation dependency management
- Automation execution documentation
- Manual and automated QA documentation
- Test-to-defect traceability
- Final QA Test Summary Report
- Risk assessment
- Release recommendation
- Retesting recommendations
- Final repository audit

## Final Status

The planned QA work for this challenge is **complete**.

The repository contains the manual testing documentation, defect reports, supporting evidence, automated regression tests, automation dependencies, final Test Summary Report, and overall release assessment.

---

# Repository Note

The original Job Request Tracker HTML file supplied for the QA challenge is **not included in this repository**.

The supplied application is treated as confidential test material and is kept outside the repository.

The repository contains only the QA work created for the challenge, including:

- Test Plan
- 17 manual test cases
- 8 documented defect reports
- Manual test evidence
- Automated test evidence
- Python/Playwright automated test code
- Automation dependencies
- Final QA Test Summary Report
- Project README and supporting QA documentation

The supplied challenge PDFs and HTML application are excluded through `.gitignore`.

This keeps confidential challenge material separate from the QA deliverables while still allowing authorised testers with a local copy of `Job_traker.html` to execute the automated test suite.

---

# Final Release Recommendation

**NOT READY FOR RELEASE**

The application should not be released until the High-severity financial defects have been corrected and successfully retested.

At minimum:

1. **BUG-001** should be fixed so that Total Budget accurately reflects the underlying job budgets.
2. **BUG-003** should be fixed so that invalid negative budget values cannot be saved.
3. The affected manual test cases should be rerun.
4. The complete automated regression suite should be rerun.
5. AT-002 and AT-003 should be reviewed after their corresponding defects are fixed.
6. Medium-severity findings should be reviewed against confirmed product requirements before release.

## Findings by Severity

### High Severity

- **BUG-001 - Incorrect Total Budget**
- **BUG-003 - Negative budget values are accepted**

These defects affect financial-data accuracy and integrity and must be addressed before release.

### Medium Severity

- BUG-004 - Completed jobs counted as overdue
- BUG-005 - Incorrect filtered result count
- BUG-006 - Case-sensitive search
- BUG-007 - Clear Filters does not clear Search
- BUG-008 - Poor mobile responsiveness

These should be reviewed and prioritised according to confirmed product requirements.

### Low Severity

- BUG-002 - Client Name validation spelling error

Although this does not prevent the validation functionality from working, the user-facing text should be corrected.

The complete final QA assessment is available in:

[`Docs/test-summary-report.md`](Docs/test-summary-report.md)

The complete testing lifecycle and final assessment are documented across `Docs/test-plan.md`, `Docs/test-cases.md`, `Docs/bug-report.md`, and `Docs/test-summary-report.md`. Together with the evidence and automated regression suite, these deliverables provide traceability from test planning and execution through defect identification, automation, risk assessment, and the final release recommendation.

---

# Overall QA Conclusion

The Job Request Tracker's core functionality is usable, including creating requests, required-field validation, searching, status filtering, and displaying job information.

Manual testing identified **8 documented defects** across financial calculations, validation, filtering, search behaviour, overdue-job handling, result counts, and responsive design.

The highest-priority findings relate to financial-data integrity:

- **BUG-001:** The Total Budget does not equal the sum of the displayed job budgets.
- **BUG-003:** Negative budget values can be saved.

A focused automated regression suite was subsequently implemented using **Python, pytest, and Playwright**.

**AT-001** confirms that a valid job request can be created successfully.

**AT-002** automatically reproduces the Client Name validation spelling defect documented as **BUG-002**.

**AT-003** independently reads and calculates the displayed job budgets and reproduces **BUG-001** by demonstrating that the jobs total **R100,300** while the application displays **R87,800**.

The automation currently contains four checks when the setup smoke test is included:

- **2 passing**
- **2 failing because of known application defects**

The combination of manual exploratory testing and targeted browser automation provides broad behavioural coverage together with repeatable regression checks for important application functionality.

Based on the testing performed, the application is **not ready for release**. The **high-severity financial defects must be addressed and retested before release**. The medium-severity filtering, search, overdue-status, and responsive-design issues should then be reviewed according to product priorities.

Once the identified defects are corrected, the affected manual tests and automated regression tests should be rerun to verify the fixes and check for regressions.

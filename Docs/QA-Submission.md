# Job Request Tracker - QA Submission

**Tester:** Andiswa Ndzimande

This single document contains Part 1: Test plan, Part 2: Test cases and Part 3: Bug log. Screenshots are in the Evidence folder. The automated tests are in the Automation folder.

---


# Job Request Tracker - Test Plan

**Tester:** Andiswa Ndzimande
**Application under test:** `job-tracker-demo.html` (QA test build)
**Test execution date:** 8 October 2026
**Last updated:** 8 October 2026

## 1. Objective

The objective of this testing is to evaluate the Job Request Tracker before release and identify functional, validation, calculation, usability, input-handling and responsive design issues that could affect users.

Testing focuses on the application's core functionality, particularly creating job requests, displaying accurate job information, searching and filtering jobs, summary calculations, form validation, and behaviour on desktop and mobile screen sizes.

## 2. Scope

### In Scope

- New job request creation and the New request form (Client name, Job title, Due date, Budget, Status, Cancel, Save request)
- Form validation (empty, spaces-only, negative, zero, decimal and very large values)
- Handling of special characters and HTML-like text typed into text fields (basic input handling, not penetration testing)
- Duplicate submission and interruption: double-clicking Save, and clicking Cancel while a request is saving
- Date handling: past dates, today's date, and unusual years
- Job list/table display, including every Status option (Pending, In progress, Done)
- Search (Client name and Job title, different letter casing, partial text, no match)
- Status filtering (every option), combined search and status filtering, Clear filters
- Summary information: Open jobs, Overdue, Total budget and the "Showing N jobs" line
- Overdue behaviour, including completed (Done) jobs
- Desktop usability and layout
- Mobile/responsive behaviour using the browser device toolbar (iPhone 16, 393 x 852)
- Positive, negative and boundary test scenarios
- Exploratory testing of the page
- Automation of three important checks (AT-001 to AT-003, see section 3.4)

### Out of Scope

- Backend services and APIs, as none were provided for testing
- Database testing, as the supplied application does not provide access to a database
- Authentication and user account testing, as login functionality is not part of the supplied build
- Production deployment and hosting
- Performance or load testing
- Security penetration testing (only the basic input-handling checks listed above were performed)
- Dedicated accessibility testing
- Browsers other than the browsers required by the challenge

## 3. Test Approach

Testing uses a risk-based approach. Core functionality and data accuracy are tested first, followed by supporting functionality, usability and responsive behaviour.

### 3.1 Control-by-control checklist

To avoid testing only the "obvious" behaviour of each feature, every control on the page was listed and the same checklist was applied to each one.

**Control inventory**

| Area | Control | Type |
|---|---|---|
| Main page | + New request | Button |
| Main page | Search client or job title | Text box |
| Main page | Status filter (All statuses, Pending, In progress, Done) | Drop-down |
| Main page | Clear filters | Button |
| Main page (outputs) | Open jobs, Overdue, Total budget, "Showing N jobs" | Calculated values - checked against an independent calculation |
| New request form | Client name, Job title | Text boxes |
| New request form | Due date | Date picker |
| New request form | Budget (R) | Number box |
| New request form | Status | Drop-down |
| New request form | Cancel, Save request | Buttons |

**Checklist applied to each input:** empty; spaces only; boundary values (zero, negative, smallest, very large); special characters and HTML-like text; very long text; repeating the action quickly (double-click); interrupting the action (Cancel while saving, refresh); **every option** of every drop-down; and for every calculated value, an independent hand calculation.

### 3.2 Techniques

1. **Functional Testing** - verify features such as creating requests, searching and filtering work as expected.
2. **Positive Testing** - test the application using valid user input.
3. **Negative Testing** - test invalid or missing input to verify that the application handles errors correctly.
4. **Boundary Testing** - test boundary values such as zero, negative, decimal, very large budgets, and due dates of yesterday, today and unusual years.
5. **Exploratory Testing** - explore the application beyond predefined test cases to identify unexpected behaviour.
6. **Responsive Testing** - test the application on desktop and phone-sized screens.
7. **Automated Testing** - automate three important checks (two High-severity defects and one Medium) using Python, pytest and Playwright (see 3.4).

### 3.3 Test data approach

- Calculations are tested with **distinctive non-zero amounts** (for example R1 000 or R1 234). A budget of R0 can hide a calculation error because adding zero changes nothing.
- Expected results are calculated by hand from the table **before** reading the value on screen.
- The Overdue figure depends on the current date, so expected values are written as a rule ("due date before today AND status not Done") and the test date is recorded.
- Each test starts from a freshly reloaded page (F5), because jobs added during testing exist only until the page is reloaded.

### 3.4 Automation approach

Automation covers a small number of important, repeatable checks instead of trying to automate every manual test.

| Item | Choice |
|---|---|
| Language | Python 3.14.2 |
| Test runner | pytest 9.1.1 |
| Browser automation | Playwright 1.63.0 with pytest-playwright 0.9.0 |
| Browser | Chromium |
| Structure | `conftest.py` holds a page object (`JobTrackerPage`) and a `tracker` fixture that opens a fresh copy of the app for every test; the tests use the Arrange - Act - Assert pattern |

**The three automated checks**

| ID | Defect | Severity | What the test checks | Why it was chosen |
|---|---|---|---|---|
| AT-001 | BUG-001 | 🔴 High | Total budget equals the sum of the budgets in the table | Wrong money figure on the first screen; the expected value is calculated by the test, not hard-coded |
| AT-002 | BUG-003 | 🔴 High | A job with a budget of -5000 is not added to the table | Invalid financial data is stored; a clear pass/fail check |
| AT-003 | BUG-009 | 🟠 Medium | Choosing **Done** in the status filter lists every Done job | A whole filter option is broken; the expected count is read from the page |

**Selection criteria:** high business impact; the result does not depend on today's date or on random data; a test that runs in a few seconds; each test reproduces a logged defect.

**Not automated (and why):** BUG-004 and BUG-016 depend on today's date and would need a controlled clock; BUG-010 (double-click) and BUG-011 (Cancel while saving) depend on timing; BUG-012 needs a security-focused approach; BUG-008 is a visual layout problem.

**Known-bug strategy:** each test describes the correct behaviour and is marked `xfail(raises=AssertionError, strict=True)` with the bug ID.
- `raises=AssertionError` means only a failed check counts as the known bug; a missing file, timeout or wrong locator still shows as a real error.
- `strict=True` means that when a developer fixes the bug, the test passes and pytest reports XPASS(strict) as a failure, which is the reminder to remove the `xfail` marker.

**Running:** from the `Automation` folder, `python -m pytest -v` lists the three known bugs as XFAIL; `python -m pytest --runxfail` shows the real failure messages.

## 4. Test Priorities

### 🔴 P1 - Critical

Failures could give incorrect business information, create wrong or duplicate records, or prevent users from completing their main tasks.

- Creating a new job request, including a double-click on Save
- Required field validation
- Budget input and calculation (Total budget, negative, zero, decimal, large values)
- Open job count
- Overdue job count, including Done jobs
- Correct storage and display of submitted job information (including special characters)

### 🟠 P2 - High

These features support users in finding and managing job requests.

- Search functionality (casing, partial text, no result)
- Status filtering - **every option**
- Clearing filters
- "Showing N jobs" line
- Job table display and Status display
- Due date behaviour (past, today, unusual years)
- Cancel behaviour
- Mobile usability

### 🟡 P3 - Medium

These areas have lower business impact but still affect the overall user experience.

- Text and spelling
- Visual consistency
- Layout and alignment (including very long text)
- Error message clarity
- General usability

## 5. Test Environment

- **Operating System:** Windows
- **Browser:** Google Chrome Version 154.0.8037.93 (Official Build) (64-bit)
- **Application:** Job Request Tracker QA test build (`job-tracker-demo.html`)
- **Desktop Testing:** Chrome desktop browser
- **Mobile Testing:** Chrome DevTools device toolbar (iPhone 16, 393 x 852)
- **Test Type:** Local HTML application
- **Test date:** 8 October 2026 (the first testing session took place on or before 6 October 2026)

## 6. Entry Criteria

Testing can begin when:

- The supplied Job Request Tracker HTML file can be opened successfully.
- The application loads in the supported browser.
- The main page and New Request form are accessible.

## 7. Exit Criteria

Testing is considered complete when:

- Planned high-priority test scenarios have been executed.
- New Request form test cases have been completed.
- Every control on the page has been tested with the checklist in section 3.1.
- Identified bugs have been documented with numbered reproduction steps, expected and actual results (with numbers), severity and severity reason, environment, test date and evidence.
- Desktop and mobile testing has been completed.
- Three important checks (two High-severity, one Medium) have been automated, run from the `Automation` folder, and their results recorded with screenshots.
- Test documentation and automation instructions have been reviewed for clarity.

## 8. Assumptions and Limitations

- Testing is based on the supplied Job Request Tracker test build.
- Displayed summary values should accurately reflect the job data shown by the application.
- Invalid financial values (negative amounts) should not be accepted as valid job budgets.
- A valid job budget is assumed to be greater than zero (to be confirmed).
- Completed (`Done`) jobs should not be counted as overdue.
- User-facing search should be case-insensitive.
- Typed text should be displayed exactly as typed (no HTML interpretation).
- The absence of Edit and Delete features is recorded as an observation (OBS-02), not a defect, because the brief does not require them.
- Whether a new request may have a past due date is an open question for the product owner (OBS-01).
- Testing is time-boxed according to the challenge instructions, so higher-risk functionality is prioritised.
- Testing is limited to functionality available in the supplied build.
- No backend, database or production environment was provided for testing.
- The Overdue figure changes with the date; results were recorded on 8 October 2026.


---


# Job Request Tracker - Test Cases

**Tester:** Andiswa Ndzimande
**Application:** `job-tracker-demo.html` (QA test build)
**Last updated:** 8 October 2026

## Standard Preparation and Result Key

> [!IMPORTANT]
> **Before every test case:** open `job-tracker-demo.html` in Google Chrome (double-click the file) and press **F5** so that only the original 10 jobs are shown. The starting figures on 8 October 2026 are: **Open jobs 8**, **Overdue 6**, **Total budget R87 800**, and the grey line above the table reads **Showing 10 jobs**.

**How to use the form:** click the black **+ New request** button (top-right). The form has five fields: **Client name** (text), **Job title** (text), **Due date** (date picker - click the small calendar icon and pick a date, or type the date), **Budget (R)** (number) and **Status** (drop-down: Pending, In progress, Done). The buttons at the bottom are **Cancel** and **Save request**. After clicking Save the form shows `Saving...` for about one second and then closes.

**The Overdue figure depends on today's date.** Expected results are written as a rule (for example "past due and not Done"); numbers are those for 8 October 2026.

**Result key:**

- ✅ **PASS** - actual result matches the expected result.
- ⚠️ **PASS with known issue** - the feature under test behaves correctly; the only difference is a problem already logged under another bug (for example the wrong "Showing" line, BUG-005).
- ❌ **FAIL** - actual result differs from the expected result; the bug is listed.
- ❌ **FAIL based on documented assumption** - fails against an assumption that needs product-owner confirmation.

## Results Overview

| Test case | Title | Result | Related bug |
|---|---|---|---|
| TC-001 | Create a new request with valid information | ⚠️ PASS with known issue | BUG-001 |
| TC-002 | Verify Total Budget calculation | ❌ FAIL | BUG-001 |
| TC-003 | Submit a new request without a Client Name | ⚠️ PASS with known issue | BUG-002 |
| TC-004 | Submit a new request without a Job Title | ✅ PASS | - |
| TC-005 | Submit a new request without a Due Date | ✅ PASS | - |
| TC-006 | Submit a new request without a Budget | ✅ PASS | - |
| TC-007 | Submit a new request with a negative Budget | ❌ FAIL | BUG-003 |
| TC-008 | Submit a new request with a zero Budget | ❌ FAIL based on documented assumption | BUG-013 |
| TC-009 | Cancel creation of a new request | ✅ PASS | - |
| TC-010 | Create a request with In progress status | ✅ PASS | - |
| TC-011 | Verify completed past-due jobs are not treated as overdue | ❌ FAIL | BUG-004 (see also TC-028) |
| TC-012 | Search for jobs by Client Name | ❌ FAIL | BUG-005 |
| TC-013 | Search using different letter casing | ❌ FAIL | BUG-006 |
| TC-014 | Filter jobs by Pending status | ⚠️ PASS with known issue | BUG-005 |
| TC-015 | Clear all active filters | ❌ FAIL | BUG-007 |
| TC-016 | Search for a job by Job Title | ⚠️ PASS with known issue | BUG-005 |
| TC-017 | Verify application usability on a phone-sized screen | ❌ FAIL | BUG-008 |
| TC-018 | Client Name containing only spaces | ⚠️ PASS with known issue | BUG-002 |
| TC-019 | Client Name containing an HTML tag | ❌ FAIL | BUG-012 |
| TC-020 | Client Name containing an apostrophe, ampersand and quotation marks | ✅ PASS | - |
| TC-021 | Client Name of 150 characters | ❌ FAIL | BUG-015 |
| TC-022 | Double-click the Save request button | ❌ FAIL | BUG-010 |
| TC-023 | Job Title containing an HTML tag | ❌ FAIL | BUG-012 |
| TC-024 | Search for a new job using its exact capitalisation | ✅ PASS | - |
| TC-025 | Search for a new job using lowercase letters | ❌ FAIL | BUG-006 |
| TC-026 | Due date in the past with status Pending | ✅ PASS | - |
| TC-027 | Due date is today (boundary) | ✅ PASS | - |
| TC-028 | Due date in the past with status Done | ❌ FAIL | BUG-004 |
| TC-029 | Due date with a 5-digit year | ❌ FAIL | BUG-016 |
| TC-030 | Budget with decimals | ❌ FAIL | BUG-014 |
| TC-031 | Very large budget | ⚠️ PASS with known issue | BUG-001 |
| TC-032 | Total budget after adding a job | ❌ FAIL | BUG-001 |
| TC-033 | Save one job with each status | ✅ PASS | - |
| TC-034 | Done job with a future due date | ✅ PASS | - |
| TC-035 | Filter jobs by In progress status | ⚠️ PASS with known issue | BUG-005 |
| TC-036 | Filter jobs by Done status | ❌ FAIL | BUG-009 |
| TC-037 | Search with no matching job | ⚠️ PASS with known issue | BUG-005 |
| TC-038 | Search for part of a client name | ⚠️ PASS with known issue | BUG-005 |
| TC-039 | Search and status filter used together | ⚠️ PASS with known issue | BUG-005 |
| TC-040 | Clear filters after using only the status filter | ✅ PASS | - |
| TC-041 | Clear filters after a search with no results | ❌ FAIL | BUG-007 |
| TC-042 | Cancel clicked while the request is saving | ❌ FAIL | BUG-011 |

**Totals: 42 test cases executed - ✅ 12 PASS, ⚠️ 10 PASS with known issue, ❌ 20 FAIL.**

## New Request Form

These test cases verify the functionality, validation and behaviour of the New Request form using positive, negative and boundary testing.

### TC-001 - Create a new request with valid information

**Priority:** P1 - Critical

**Test Data:**

- Client Name: Test Client
- Job Title: Website Design
- Due Date: 20 October 2026
- Budget: 5000
- Status: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Enter `Test Client` in Client Name.
4. Enter `Website Design` in Job Title.
5. Select `20 October 2026` as the Due Date.
6. Enter `5000` as the Budget.
7. Select `Pending`.
8. Click **Save request**.

**Expected Result:**

The request should be saved successfully, the form should close, and the new job should appear in the job table with the entered information. The relevant summary information should update correctly.


**Actual Result:**

The request was successfully saved and displayed in the job table with the correct job title, due date, status and budget.

The Open Jobs count increased from 8 to 9 and the number of displayed jobs increased from 10 to 11.

The Total Budget displayed R100,300 after the request was added. Subsequent testing in TC-002 confirmed that the application's Total Budget calculation is inaccurate and is tracked separately under BUG-001.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-001

### TC-002 - Verify Total Budget calculation

**Priority:** P1 - Critical

**Test Data:**

Budgets of the 10 initial jobs displayed in the application.

**Steps:**

1. Open the Job Request Tracker.
2. Record the budget of each displayed job.
3. Calculate the sum of all 10 job budgets.
4. Compare the calculated total with the Total Budget displayed by the application.

**Expected Result:**

The Total Budget should equal the sum of all displayed job budgets.

Expected total: R100,300.

**Actual Result:**

The application displays R87,800.

The displayed total is R12,500 lower than the correct total.

**Result:** ❌ FAIL

**Related Bug:** BUG-001

### TC-003 - Submit a new request without a Client Name

**Priority:** P1 - Critical

**Test Type:** Negative Testing

**Test Data:**

- Client Name: [blank]
- Job Title: Website Design
- Due Date: 20 October 2026
- Budget: 5000
- Status: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Leave the Client Name field empty.
4. Enter `Website Design` as the Job Title.
5. Select `20 October 2026` as the Due Date.
6. Enter `5000` as the Budget.
7. Select `Pending`.
8. Click **Save request**.

**Expected Result:**

The request should not be saved.

The New Request form should remain open and display a clear validation message explaining that Client Name is required.

No new job should be added to the job table.

**Actual Result:**

The request was not saved. The New Request form remained open and a validation message was displayed below the Status field.

The user was able to return to the Client Name field and correct the missing information.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-002

**Note:** Required-field validation functions correctly, but the displayed validation message contains a spelling error documented under BUG-002.

### TC-004 - Submit a new request without a Job Title

**Priority:** P1 - Critical

**Test Type:** Negative Testing

**Test Data:**

- Client Name: WTC
- Job Title: [blank]
- Due Date: 20 October 2026
- Budget: 5000
- Status: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Enter `WTC` as the Client Name.
4. Leave the Job Title field empty.
5. Select `20 October 2026` as the Due Date.
6. Enter `5000` as the Budget.
7. Select `Pending`.
8. Click **Save request**.

**Expected Result:**

The request should not be saved.

The form should remain open and display a clear validation message explaining that Job Title is required.

No new job should be added to the table.
**Actual Result:**

The request was not saved. The New Request form remained open and displayed the validation message:

`Job title is required.`

No new job was added to the table.

**Result:** ✅ PASS
### TC-005 - Submit a new request without a Due Date

**Priority:** P1 - Critical

**Test Type:** Negative Testing

**Test Data:**

- Client Name: WTC
- Job Title: Website Design
- Due Date: [blank]
- Budget: 5000
- Status: Pending

**Steps:**

1. Open the New Request form.
2. Enter `WTC` as the Client Name.
3. Enter `Website Design` as the Job Title.
4. Leave the Due Date field empty.
5. Enter `5000` as the Budget.
6. Select `Pending`.
7. Click **Save request**.

**Expected Result:**

The request should not be saved.

The form should remain open and display a clear validation message explaining that a Due Date is required.

No new job should be added to the table.

**Actual Result:**

The request was not saved. The New Request form remained open and displayed the validation message:

`Please choose a due date.`

No new job was added to the table.

**Result:** ✅ PASS
### TC-006 - Submit a new request without a Budget

**Priority:** P1 - Critical

**Test Type:** Negative Testing

**Test Data:**

- Client Name: WTC
- Job Title: Website Design
- Due Date: 20 October 2026
- Budget: [blank]
- Status: Pending

**Steps:**

1. Open the New Request form.
2. Enter `WTC` as the Client Name.
3. Enter `Website Design` as the Job Title.
4. Select `20 October 2026` as the Due Date.
5. Leave the Budget field empty.
6. Select `Pending`.
7. Click **Save request**.

**Expected Result:**

The request should not be saved.

The form should remain open and display a clear validation message explaining that a Budget is required.

No new job should be added to the table.

**Actual Result:**

The request was not saved. The New Request form remained open and displayed the validation message:

`Please enter a budget.`

No new job was added to the table.

**Result:** ✅ PASS

### TC-007 - Submit a new request with a negative Budget

**Priority:** P1 - Critical

**Test Type:** Negative / Boundary Testing

**Test Data:**

- Client Name: WTC
- Job Title: Website Design
- Due Date: 20 October 2026
- Budget: -5000
- Status: Pending

**Steps:**

1. Open the New Request form.
2. Enter `WTC` as the Client Name.
3. Enter `Website Design` as the Job Title.
4. Select `20 October 2026` as the Due Date.
5. Enter `-5000` as the Budget.
6. Select `Pending`.
7. Click **Save request**.

**Expected Result:**

The request should not be saved.

The application should display a validation message explaining that the Budget must be a valid positive amount.

No job with a negative budget should be added to the job table.

**Actual Result:**

The application accepted the negative budget of `-5000` and saved the request successfully.

The New Request form closed and a new WTC job appeared in the table with the budget displayed as `R-5 000`.

The number of displayed jobs increased from 10 to 11 and Open Jobs increased from 8 to 9.

No validation error was displayed.

**Result:** ❌ FAIL

**Related Bug:** BUG-003
### TC-008 - Submit a new request with a zero Budget

**Priority:** P1 - Critical

**Test Type:** Boundary Testing

**Assumption:**

A valid job budget should be greater than zero.

**Test Data:**

- Client Name: WTC
- Job Title: Free Campaign
- Due Date: 20 October 2026
- Budget: 0
- Status: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Enter `WTC` as the Client Name.
4. Enter `Free Campaign` as the Job Title.
5. Select `20 October 2026` as the Due Date.
6. Enter `0` as the Budget.
7. Select `Pending`.
8. Click **Save request**.

**Expected Result:**

Based on the documented assumption that job budgets must be greater than zero, the request should not be saved.

The application should display a validation message indicating that the budget must be greater than zero.
**Actual Result:**

The application accepted a budget value of `0` and saved the request successfully.

The new job appeared in the table with the budget displayed as `R0`.

No validation message was displayed.

**Result:** ❌ FAIL based on documented assumption

**Related Bug:** BUG-013

**Note:**

The supplied requirements do not specify whether zero-value budgets are permitted. 
This result is therefore based on the test assumption that a valid job budget must be greater than zero. 
Business clarification would be required before confirming this behaviour as a defect.

### TC-009 - Cancel creation of a new request

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Client Name: Cancel Test
- Job Title: Test Job
- Due Date: 20 October 2026
- Budget: 5000
- Status: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Confirm the current number of displayed jobs.
3. Click **+ New request**.
4. Enter `Cancel Test` as the Client Name.
5. Enter `Test Job` as the Job Title.
6. Select `20 October 2026` as the Due Date.
7. Enter `5000` as the Budget.
8. Select `Pending`.
9. Click **Cancel**.

**Expected Result:**

The New Request form should close.

The request should not be saved and the number of jobs should remain unchanged.

**Actual Result:**

The New Request form closed after clicking Cancel.

The number of displayed jobs remained at 10 and the `Cancel Test` request was not added to the job table.

**Result:** ✅ PASS
### TC-010 - Create a request with In progress status

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Client Name: WTC
- Job Title: Social Media Campaign
- Due Date: 25 October 2026
- Budget: 6000
- Status: In progress

**Steps:**

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Enter `WTC` as the Client Name.
4. Enter `Social Media Campaign` as the Job Title.
5. Select `25 October 2026` as the Due Date.
6. Enter `6000` as the Budget.
7. Select `In progress`.
8. Click **Save request**.
9. Locate the new request in the job table.

**Expected Result:**

The request should be saved successfully.

The new job should appear in the table with the status displayed as `In progress`.

**Actual Result:**

The request was successfully saved and appeared in the job table.

The selected status was correctly displayed as `In progress`.

**Result:** ✅ PASS
### TC-011 - Verify completed past-due jobs are not treated as overdue

**Priority:** P1 - Critical

**Test Type:** Functional / Business Rule Testing

**Assumption:**

A job with a status of `Done` should no longer be considered overdue, even when its due date has passed. Rule: **Overdue = due date before today AND status not Done.**

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5**.
2. Read the number in the **Overdue** box (middle summary box).
3. In the table, find every row whose **Due date** is earlier than today (8 October 2026): rows 1 (2026-10-02), 3 (2026-09-25), 4 (2026-10-06), 5 (2026-09-30), 7 (2026-09-28) and 10 (2026-10-01).
4. Write down the **Status** of each of those rows (rows 3 and 7 are **Done**).
5. Count the past-due rows that are **not** Done.
6. Look at the text colour of rows 3 and 7.

**Expected Result:**

Only past-due jobs that are not Done count as overdue: **Overdue = 4** (rows 1, 4, 5 and 10). The two Done rows are shown in normal black text.

**Actual Result:**

On 8 October 2026 the application displays **Overdue = 6**: six jobs are past due, including the two Done jobs, and the two Done rows are shown in red.

The original test (on or before 6 October 2026, when row 4 was not yet past due) showed Overdue = 5 against an expected 3. The behaviour is the same; the figures change with the date.

**Result:** ❌ FAIL

**Related Bug:** BUG-004 (see also TC-028)

### TC-012 - Search for jobs by Client Name

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Search term: Kestrel Motors

**Steps:**

1. Open the Job Request Tracker.
2. Locate the Search field.
3. Enter `Kestrel Motors`.
4. Observe the jobs displayed in the table.

**Expected Result:**

Only jobs belonging to `Kestrel Motors` should be displayed.

Two matching jobs should appear:

- Showroom poster - A1
- 4x4 bakkie spec sheet update

The displayed result count should indicate that 2 jobs are being shown.

**Actual Result:**

The search successfully filtered the table and displayed the two jobs belonging to `Kestrel Motors`.

However, the result counter above the table continued to display `Showing 10 jobs` even though only 2 jobs were visible.

**Result:** ❌ FAIL

**Related Bug:** BUG-005

### TC-013 - Search using different letter casing

**Priority:** P2 - High

**Test Type:** Usability / Functional Testing

**Test Data:**

- Search term: kestrel motors

**Steps:**

1. Open the Job Request Tracker.
2. Enter `kestrel motors` in lowercase in the Search field.
3. Observe the displayed results.

**Expected Result:**

The search should return the same two `Kestrel Motors` jobs regardless of letter casing.
**Actual Result:**

When `kestrel motors` was entered using lowercase letters, no matching jobs were returned.

The application displayed:

`No jobs match your filters.`

Searching for `Kestrel Motors` using the exact capitalization successfully returned two matching jobs.

**Result:** ❌ FAIL

**Related Bug:** BUG-006

**Note:** The same defect was reproduced on Job title (TC-025).

### TC-014 - Filter jobs by Pending status

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Status Filter: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Open the Status filter.
3. Select `Pending`.
4. Observe the jobs displayed in the table.
5. Observe the result count above the table.

**Expected Result:**

Only jobs with a status of `Pending` should be displayed.

Three jobs should be displayed.

The result counter should display:

`Showing 3 jobs`
**Actual Result:**

The Status filter correctly displayed only the three jobs with a `Pending` status:

- Ridgeway Mining
- Visit Karoo
- Mooirivier Chemicals

However, the result counter continued to display `Showing 10 jobs` instead of `Showing 3 jobs`.

The incorrect result counter is already tracked under BUG-005.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-005

### TC-015 - Clear all active filters

**Priority:** P2 - High

**Test Type:** Functional Testing

**Precondition:**

Both Search and Status filters are active.

**Test Data:**

- Search: Visit
- Status: Pending

**Steps:**

1. Open the Job Request Tracker.
2. Enter `Visit` in the Search field.
3. Select `Pending` from the Status filter.
4. Confirm that the table is filtered.
5. Click **Clear filters**.
6. Observe the Search field.
7. Observe the Status filter.
8. Observe the job table.

**Expected Result:**

Both filters should be reset.

The Search field should become empty.

The Status filter should return to `All statuses`.

All 10 jobs should be displayed again.

**Actual Result:**

Clicking `Clear filters` reset the Status filter to `All statuses`, but the Search field was not cleared.

The search term `Visit` remained in the Search field and the table remained filtered to the Visit Karoo job.

**Result:** ❌ FAIL

**Related Bug:** BUG-007

**Note:** A second example, with no search results, is TC-041.


### TC-016 - Search for a job by Job Title

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Search term: Annual report

**Steps:**

1. Open the Job Request Tracker.
2. Ensure no Status filter is active.
3. Enter `Annual report` in the Search field.
4. Observe the displayed jobs.

**Expected Result:**

The application should display the job whose title contains `Annual report`.

The `Ridgeway Mining - Annual report infographics` job should be displayed.

Other non-matching jobs should not be displayed.

**Actual Result:**

The search successfully returned the `Ridgeway Mining - Annual report infographics` job when `Annual report` was entered.

Only the matching job was displayed.

The result counter continued to display `Showing 10 jobs`, which is already tracked under BUG-005.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-005
### TC-017 - Verify application usability on a phone-sized screen

**Priority:** P2 - High

**Test Type:** Responsive / Usability Testing

**Environment:**

- Google Chrome Device Toolbar
- Device: iPhone 16
- Viewport: 393 × 852

**Steps:**

1. Open the Job Request Tracker in Google Chrome.
2. Open Chrome Developer Tools.
3. Enable the Device Toolbar.
4. Select `iPhone 16`.
5. Observe the dashboard, filters and job table.
6. Attempt to access content on the right side of the application.

**Expected Result:**

The application should adapt to the phone-sized viewport.

Important controls and information should remain usable without requiring the user to horizontally drag across the entire page.

**Actual Result:**

The application does not adapt correctly to the phone-sized viewport.

Only part of the dashboard and job table is visible at one time.

The user must horizontally drag the page to access content on the right, including:

- Total Budget
- New Request button
- Status filter
- Clear Filters button
- Due Date
- Status
- Budget

The content is accessible by horizontal dragging, but the mobile experience is difficult to use.

**Result:** ❌ FAIL

**Related Bug:** BUG-008

## Additional Control-by-Control Testing (8 October 2026)

These cases were added after listing every control on the page (Search box, Status drop-down, Clear filters, + New request, and the five form fields plus Cancel and Save) and applying the same checklist to each: empty, spaces only, boundary values, special characters, very long text, fast repeated clicks, interruption, and **every option** of every drop-down.

### TC-018 - Client Name containing only spaces

**Priority:** P1 - Critical

**Test Type:** Negative Testing

**Test Data:**

- Client Name: 3 spaces
- Job Title: Test Job
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Click in **Client name** and press the space bar three times (no letters).
4. Fill in the other fields: **Job title** `Test Job`, **Due date** `01 December 2026` (use the calendar icon), **Budget (R)** `1000`, **Status** `Pending`.
5. Click the black **Save request** button (bottom-right of the form).
6. Read the red message under the Status field and count the table rows.

**Expected Result:**

Spaces are not a real name, so the request is **not saved**, the form stays open, the table still has **10 rows** and the message reads `Client name is required.`

**Actual Result:**

The request was not saved, the form stayed open and the table still had 10 rows. The message read `Client name is requred.` (spelling error).

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-002

**Note:** The validation (spaces treated as empty) works correctly; only the message text is wrong.

### TC-019 - Client Name containing an HTML tag

**Priority:** P1 - Critical

**Test Type:** Negative / Input-handling Testing

**Test Data:**

- Client Name: <b>Test</b>
- Job Title: Test Job
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `<b>Test</b>`
   - **Job title:** `Test Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the **Client** cell of the new last row.

**Expected Result:**

The row shows the characters exactly as typed: `<b>Test</b>`, in normal text.

**Actual Result:**

The row shows only the word **Test**, in **bold**. The tags are not displayed because the page interpreted them as formatting.

**Result:** ❌ FAIL

**Related Bug:** BUG-012

### TC-020 - Client Name containing an apostrophe, ampersand and quotation marks

**Priority:** P2 - High

**Test Type:** Input-handling Testing

**Test Data:**

- Client Name: O'Brien & Sons "Ltd"
- Job Title: Test Job
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `O'Brien & Sons "Ltd"`
   - **Job title:** `Test Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the **Client** cell of the new last row.

**Expected Result:**

The row shows exactly `O'Brien & Sons "Ltd"`.

**Actual Result:**

The request saved and the row showed `O'Brien & Sons "Ltd"` exactly as typed, including the quotation marks.

**Result:** ✅ PASS

### TC-021 - Client Name of 150 characters

**Priority:** P3 - Medium

**Test Type:** Boundary Testing

**Test Data:**

- Client Name: the letter `a` repeated 150 times
- Job Title: Long Name Job
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. In **Client name** type the letter `a` 150 times (type ten, select and copy them, paste fifteen times).
4. Fill in the other fields: **Job title** `Long Name Job`, **Due date** `01 December 2026`, **Budget (R)** `1000`, **Status** `Pending`.
5. Click the black **Save request** button (bottom-right of the form).
6. Wait one second for the form to close.
7. Look at the whole page, including the right-hand columns.

**Expected Result:**

The field limits the length (for example to 100 characters) or the long name wraps so that the table keeps its normal width.

**Actual Result:**

All 150 characters were accepted and the layout stretched to fit the long name.

**Result:** ❌ FAIL

**Related Bug:** BUG-015

**Note:** No maximum length is defined in the brief; 100 characters is a suggested limit to confirm with the product owner.

### TC-022 - Double-click the Save request button

**Priority:** P1 - Critical

**Test Type:** Negative / Timing Testing

**Test Data:**

- Client Name: Dup Co
- Job Title: Dup Job
- Due Date: 01 December 2026
- Budget: 1234
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Dup Co`
   - **Job title:** `Dup Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1234`
   - **Status:** `Pending`
4. Double-click the **Save request** button (two quick clicks).
5. Wait one second for the form to close.
6. Count the new rows. Read **Open jobs**, **Showing** and **Total budget**.

**Expected Result:**

**One** job is added: 11 rows, **Open jobs = 9**, **Showing 11 jobs**.

**Actual Result:**

**Two identical** jobs were added: 12 rows, **Open jobs = 10**, **Showing 12 jobs**; Total budget rose by R1 234.

**Result:** ❌ FAIL

**Related Bug:** BUG-010

**Note:** The app has no Delete button (OBS-02), so the duplicate cannot be removed.

### TC-023 - Job Title containing an HTML tag

**Priority:** P1 - Critical

**Test Type:** Negative / Input-handling Testing

**Test Data:**

- Client Name: Test Co
- Job Title: <i>Test</i>
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Test Co`
   - **Job title:** `<i>Test</i>`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the **Job** cell of the new last row.

**Expected Result:**

The row shows `<i>Test</i>` exactly as typed, in normal text.

**Actual Result:**

The row shows the word *Test* in italics; the tags are not displayed.

**Result:** ❌ FAIL

**Related Bug:** BUG-012

### TC-024 - Search for a new job using its exact capitalisation

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Job created: Client `Test Co`, Job title `Test Job`
- Search term: Test Job

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Test Co`
   - **Job title:** `Test Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Click in the **Search client or job title** box and type `Test Job` (capital T and J).

**Expected Result:**

The new job is shown (1 row).

**Actual Result:**

The job was found and displayed.

**Result:** ✅ PASS

**Note:** The "Showing" line is covered by BUG-005.

### TC-025 - Search for a new job using lowercase letters

**Priority:** P2 - High

**Test Type:** Usability / Functional Testing

**Test Data:**

- Job created: Client `Test Co`, Job title `Test Job`
- Search term: test job

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Test Co`
   - **Job title:** `Test Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Click in the **Search client or job title** box and type `test job` (all lowercase).

**Expected Result:**

The same job is shown (1 row).

**Actual Result:**

No jobs were shown; the table displayed `No jobs match your filters.`

**Result:** ❌ FAIL

**Related Bug:** BUG-006

**Note:** Repeats TC-013 on the Job title field.

### TC-026 - Due date in the past with status Pending

**Priority:** P2 - High

**Test Type:** Boundary Testing

**Test Data:**

- Client Name: Past Co
- Job Title: Past Job
- Due Date: 01 January 2020
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Past Co`
   - **Job title:** `Past Job`
   - **Due date:** `01 January 2020` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the colour of the new row and read **Overdue** and **Open jobs**.

**Expected Result:**

The job is saved (no rule forbids past dates), the row is red, **Overdue changes from 6 to 7** and **Open jobs from 8 to 9** (a Pending job past its date is overdue).

**Actual Result:**

The job was saved, the row was red, Overdue changed from 6 to 7 and Open jobs from 8 to 9.

**Result:** ✅ PASS

**Note:** Whether a **new** request should be allowed to have a past date is an open question for the product owner (OBS-01).

### TC-027 - Due date is today (boundary)

**Priority:** P2 - High

**Test Type:** Boundary Testing

**Test Data:**

- Client Name: Today Co
- Job Title: Today Job
- Due Date: 08 October 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Today Co`
   - **Job title:** `Today Job`
   - **Due date:** `08 October 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the colour of the new row and read **Overdue** and **Open jobs**.

**Expected Result:**

A job due today is not late yet: the row is **black**, **Overdue stays 6** and **Open jobs changes from 8 to 9**.

**Actual Result:**

The row was black, Overdue stayed at 6 and Open jobs changed from 8 to 9.

**Result:** ✅ PASS

**Note:** Use today's date when repeating this test; the page compares due dates with the current date.

### TC-028 - Due date in the past with status Done

**Priority:** P1 - Critical

**Test Type:** Business Rule Testing

**Assumption:**

A job with status `Done` is not overdue, even when its due date has passed.

**Test Data:**

- Client Name: Done Check Co
- Job Title: Done Check Job
- Due Date: 01 January 2020
- Budget: 1234
- Status: Done

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Done Check Co`
   - **Job title:** `Done Check Job`
   - **Due date:** `01 January 2020` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1234`
   - **Status:** `Done`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the colour of the new row and read **Overdue** and **Open jobs**.

**Expected Result:**

A finished job is not overdue: the row is **black**, **Overdue stays 6**, **Open jobs stays 8**.

**Actual Result:**

The row was **red** and **Overdue changed from 6 to 7**. Open jobs correctly stayed at 8.

**Result:** ❌ FAIL

**Related Bug:** BUG-004

**Note:** Reproduces TC-011 on a job created by the tester.

### TC-029 - Due date with a 5-digit year

**Priority:** P2 - High

**Test Type:** Boundary / Negative Testing

**Test Data:**

- Client Name: Year Check Co
- Job Title: Year Check Job
- Due Date: year typed as 20206
- Budget: 1234
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in **Client name** `Year Check Co`, **Job title** `Year Check Job`, **Budget (R)** `1234`, **Status** `Pending`.
4. Click the year part of **Due date** and type `20206`.
5. Click the black **Save request** button (bottom-right of the form).
6. Wait one second for the form to close.
7. Look at the colour of the new row and read **Overdue** and **Open jobs**.

**Expected Result:**

The date is far in the future: the row is **black**, **Overdue stays 6**, **Open jobs 8 to 9** (or the form rejects the year).

**Actual Result:**

The row was **red**, **Overdue changed from 6 to 7**, Open jobs changed from 8 to 9.

**Result:** ❌ FAIL

**Related Bug:** BUG-016

### TC-030 - Budget with decimals

**Priority:** P2 - High

**Test Type:** Boundary Testing

**Test Data:**

- Client Name: Decimal Co
- Job Title: Decimal Job
- Due Date: 01 December 2026
- Budget: 1500.50
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Decimal Co`
   - **Job title:** `Decimal Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1500.50`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Read the budget of the new last row.

**Expected Result:**

The row shows `R1 500,50`.

**Actual Result:**

The row showed `R1 500,5`.

**Result:** ❌ FAIL

**Related Bug:** BUG-014

### TC-031 - Very large budget

**Priority:** P3 - Medium

**Test Type:** Boundary Testing

**Test Data:**

- Client Name: Big Co
- Job Title: Big Job
- Due Date: 01 December 2026
- Budget: 999999999999
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Big Co`
   - **Job title:** `Big Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `999999999999`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Read the budget of the new last row and look at the page layout. Then read **Total budget**.

**Expected Result:**

The job is saved, the budget is shown in full and the layout does not break. (The brief gives no maximum budget.)

**Actual Result:**

The row showed `R999 999 999 999` and the layout stayed intact. Total budget showed R100 300, which leaves out the new job.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-001

**Note:** No upper limit exists; confirm with the product owner whether one is needed.

### TC-032 - Total budget after adding a job

**Priority:** P1 - Critical

**Test Type:** Calculation Testing

**Test Data:**

- Client Name: Total Check Co
- Job Title: Total Check Job
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Total Check Co`
   - **Job title:** `Total Check Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Read the **Total budget** box. The 11 listed jobs add up to R101 300.

**Expected Result:**

Total budget shows **R101 300**.

**Actual Result:**

Total budget showed **R100 300** (R1 000 too low: the newest job was left out). With a second R1 000 job added, it showed R101 300 instead of R102 300.

**Result:** ❌ FAIL

**Related Bug:** BUG-001

**Note:** Use a non-zero, distinctive amount: with a budget of R0 the wrong total looks correct.

### TC-033 - Save one job with each status

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Three jobs with status Pending, In progress and Done
- Due date 01 December 2026, Budget 1000

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Add three jobs one after the other: click **+ New request**, fill in valid data, choose the status from the **Status** drop-down (inside the form), click **Save request**. Use the statuses `Pending`, `In progress` and `Done`.
3. Read the **Status** pill of each new row.

**Expected Result:**

Each new row shows the status that was chosen.

**Actual Result:**

Each row showed the chosen status (Pending, In progress, Done).

**Result:** ✅ PASS

### TC-034 - Done job with a future due date

**Priority:** P2 - High

**Test Type:** Business Rule Testing

**Test Data:**

- Client Name: Done Future Co
- Job Title: Done Future Job
- Due Date: 20 December 2026
- Budget: 1000
- Status: Done

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Done Future Co`
   - **Job title:** `Done Future Job`
   - **Due date:** `20 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Done`
4. Click the black **Save request** button (bottom-right of the form).
5. Wait one second for the form to close.
6. Look at the colour of the new row and read **Open jobs** and **Overdue**.

**Expected Result:**

The row is **black**, **Open jobs stays 8** (a Done job is not open) and **Overdue stays 6**.

**Actual Result:**

The row was black, Open jobs stayed at 8 and Overdue was unchanged.

**Result:** ✅ PASS

### TC-035 - Filter jobs by In progress status

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Status filter: In progress

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the **All statuses** drop-down and choose **In progress**.
3. Count the rows.

**Expected Result:**

5 rows are shown: Kestrel Motors (Showroom poster), Harbour Fleet Leasing, Nexa Tech, AutoFind and Jozi Events Bureau.

**Actual Result:**

5 In progress rows were shown. The "Showing" line still read 10 jobs.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-005

### TC-036 - Filter jobs by Done status

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Status filter: Done

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the **All statuses** drop-down and choose **Done**.
3. Count the rows.

**Expected Result:**

2 rows are shown: Brightline Fibre and Kestrel Motors (4x4 bakkie spec sheet update).

**Actual Result:**

0 rows were shown (`No jobs match your filters.`).

**Result:** ❌ FAIL

**Related Bug:** BUG-009

### TC-037 - Search with no matching job

**Priority:** P2 - High

**Test Type:** Negative Testing

**Test Data:**

- Search term: zzz

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click in the **Search client or job title** box and type `zzz`.
3. Count the job rows.

**Expected Result:**

No job rows are shown and the table says that no jobs match.

**Actual Result:**

No job rows were shown. The "Showing" line still read 10 jobs.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-005

### TC-038 - Search for part of a client name

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Search term: Kestrel

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click in the **Search client or job title** box and type `Kestrel`.
3. Count the rows.

**Expected Result:**

2 rows are shown (both Kestrel Motors jobs).

**Actual Result:**

2 rows were shown. The "Showing" line still read 10 jobs.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-005

### TC-039 - Search and status filter used together

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Search term: Visit
- Status filter: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Type `Visit` in the **Search** box.
3. Choose **Pending** from the **All statuses** drop-down.
4. Count the rows.

**Expected Result:**

1 row is shown (Visit Karoo).

**Actual Result:**

1 row was shown. The "Showing" line still read 10 jobs.

**Result:** ⚠️ PASS with known issue

**Related Bug:** BUG-005

### TC-040 - Clear filters after using only the status filter

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Status filter: In progress

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Choose **In progress** from the **All statuses** drop-down (5 rows).
3. Click the **Clear filters** button.

**Expected Result:**

The drop-down returns to **All statuses** and all **10 jobs** are shown.

**Actual Result:**

The drop-down returned to All statuses and the full list was shown.

**Result:** ✅ PASS

### TC-041 - Clear filters after a search with no results

**Priority:** P2 - High

**Test Type:** Functional Testing

**Test Data:**

- Search term: zzz

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Type `zzz` in the **Search** box (0 rows).
3. Click the **Clear filters** button.
4. Look at the search box and count the rows.

**Expected Result:**

The search box is **empty** and all **10 jobs** are shown.

**Actual Result:**

`zzz` stayed in the search box and the table stayed empty (0 rows).

**Result:** ❌ FAIL

**Related Bug:** BUG-007

**Note:** Second example of TC-015.

### TC-042 - Cancel clicked while the request is saving

**Priority:** P2 - High

**Test Type:** Negative / Timing Testing

**Test Data:**

- Client Name: Cancel Co
- Job Title: Cancel Job
- Due Date: 01 December 2026
- Budget: 1000
- Status: Pending

**Steps:**

1. Open `job-tracker-demo.html` in Google Chrome and press **F5** (starting figures on 8 October 2026: Open jobs 8, Overdue 6, Total budget R87 800, **Showing 10 jobs**).
2. Click the black **+ New request** button (top-right).
3. Fill in the form fields exactly as follows:
   - **Client name:** `Cancel Co`
   - **Job title:** `Cancel Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button (bottom-right of the form).
5. Immediately (within one second, while the red text `Saving...` is visible) click **Cancel**.
6. Wait two seconds, then count the rows.

**Expected Result:**

The request is cancelled: the table keeps **10 rows** and **Open jobs stays 8**.

**Actual Result:**

The form closed, but the `Cancel Co` job then appeared as row 11 and Open jobs changed to 9.

**Result:** ❌ FAIL

**Related Bug:** BUG-011

**Note:** Cancelling before clicking Save works correctly (TC-009).

## Automated Coverage

Three of the cases above are also automated with Python, pytest and Playwright (`Automation/tests/test_job_tracker.py`). Each automated test asserts the **correct** behaviour and is marked as an expected failure (`xfail`) with its bug ID, so it currently reports **XFAIL**.

| Automated test | Function | Manual test cases | Defect | Severity |
|---|---|---|---|---|
| AT-001 | `test_total_budget_equals_sum_of_jobs` | TC-001, TC-002, TC-032 | BUG-001 | 🔴 High |
| AT-002 | `test_negative_budget_is_rejected` | TC-007 | BUG-003 | 🔴 High |
| AT-003 | `test_done_filter_shows_done_jobs` | TC-036 | BUG-009 | 🟠 Medium |

Run them from the `Automation` folder with `python -m pytest -v` (known bugs shown as XFAIL) or `python -m pytest --runxfail` (real failure messages).


---


# Job Request Tracker - Bug Report

**Tester:** Andiswa Ndzimande
**Application:** `job-tracker-demo.html` (QA test build)
**Last updated:** 8 October 2026

> [!NOTE]
> **The Overdue figure depends on today's date**, because the app compares each due date with the current date. Expected results are therefore written as a rule (for example "past due and not Done"), and the numbers are those for **8 October 2026**.

## How to read this report

- Every set of steps starts from a clean page. If you have never seen the app, follow the first two steps exactly: open the file in Chrome and press **F5**.
- **Starting figures on 8 October 2026:** Open jobs **8**, Overdue **6**, Total budget **R87 800**, and the line above the table reads **Showing 10 jobs**.
- Where a bug depends on an assumption about the intended behaviour, the assumption is written in the bug.
- Severity scale: 🔴 **High** = wrong money data, duplicated data or a security risk; 🟠 **Medium** = a feature gives wrong information or does not work but the user can still carry on; 🟡 **Low** = cosmetic or depends on an unstated rule.
- **Automated** means the bug is also reproduced by a Playwright test in `Automation/tests/test_job_tracker.py` (see the README).

## Defect summary

| Bug ID | Title | Severity | Automated |
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
| BUG-014 | Decimal budgets are shown with one decimal place (R1 500,5) | 🟡 Low | Manual |
| BUG-015 | Client name has no length limit and a very long name stretches the layout | 🟡 Low | Manual |
| BUG-016 | A due date with a 5-digit year (e.g. 20206) is treated as overdue | 🟠 Medium | Manual |

**Total: 16 defects - 4 High, 8 Medium, 4 Low.** Two further items (OBS-01, OBS-02) are observations for the product owner and are not counted as defects.

---

## BUG-001 - Total Budget does not equal the sum of the job budgets (the newest job is left out)

**Severity:** 🔴 High

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

**Part A - original data**

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Look at the **Budget** column of the table. Write down the budget of each of the 10 rows from top to bottom: R4 500, R18 000, R9 600, R3 200, R2 800, R7 500, R5 200, R22 000, R15 000, R12 500.
4. Add the 10 numbers together with a calculator. The correct total is **R100 300**.
5. Look at the **Total budget** box (the third summary box at the top of the page) and compare it with your total.

**Part B - after adding a job**

1. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
2. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
3. Fill in the form fields exactly as follows:
   - **Client name:** `Total Check Co`
   - **Job title:** `Total Check Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
4. Click the black **Save request** button at the bottom-right of the form.
5. Wait one second. The table now lists 11 jobs. The correct total is R100 300 + R1 000 = **R101 300**.
6. Read the **Total budget** box again.

### Expected Result

Part A: Total budget shows **R100 300** (the sum of the 10 listed jobs).

Part B: Total budget shows **R101 300** (the sum of the 11 listed jobs).

### Actual Result

Part A: Total budget shows **R87 800**, which is **R12 500 too low**. R12 500 is exactly the budget of the last job in the table (Jozi Events Bureau, row 10).

Part B: Total budget shows **R100 300**, which is **R1 000 too low**. R1 000 is exactly the budget of the job just added (the new last row).

### Severity Reason

🔴 High - The Total budget box shows a wrong money figure on the first screen the user sees. The error changes every time a job is added, so it is never correct, and a user relying on it would under-report the value of the work in progress.

### Notes / Suspected Cause

In both parts the missing amount is exactly the budget of the **last job in the list**. This pattern suggests the calculation skips the final row (an off-by-one error in the total calculation). It was reproduced with five different new jobs (R0, R1 000, R1 500,50, R1 000 Done, R999 999 999 999): every time the newest job was missing from the total.

### Related Test Cases

TC-001, TC-002, TC-032. **Automated:** AT-001 (`test_total_budget_equals_sum_of_jobs`).

### Evidence

- `Evidence/BUG-001-before.png`
- `Evidence/BUG-001-after.png`
- `Evidence/AT-run-2-failure-messages.png (automated test AT-001 failure message)`

---

## BUG-002 - Client name validation message contains a spelling error ("requred")

**Severity:** 🟡 Low

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Leave **Client name** empty. (To repeat with spaces, type three spaces in Client name instead.)
5. Fill in the other fields as follows:
   - **Job title:** `Test Job`
   - **Due date:** `01 December 2026` (click the calendar icon and pick this date)
   - **Budget (R):** `1000`
   - **Status:** leave as `Pending`
6. Click the black **Save request** button at the bottom-right of the form.
7. Read the red message under the **Status** field.

### Expected Result

The form stays open, no job is added (the table still has 10 jobs) and the red message reads exactly: `Client name is required.`

### Actual Result

The form stays open and no job is added (correct), but the red message reads: `Client name is requred.` (the word "required" is missing the letter *i*). The same message appears when Client name contains only spaces.

### Severity Reason

🟡 Low - The validation itself works and the user can understand the message, but a spelling mistake in text every user sees reduces trust in the product.

### Related Test Cases

TC-003, TC-018.

### Evidence

- `Evidence/BUG-002-client-name-validation.png`

---

## BUG-003 - New request form accepts a negative budget

**Severity:** 🔴 High

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields exactly as follows:
   - **Client name:** `WTC`
   - **Job title:** `Website Design`
   - **Due date:** `20 October 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `-5000`
   - **Status:** `Pending`
5. Click the black **Save request** button at the bottom-right of the form.
6. Wait one second, then look at the last row of the table and at the **Showing** line.

### Expected Result

The request is **not saved**. The form stays open and shows a message that the budget must be a positive amount. The table still has **10 jobs** and the line reads **Showing 10 jobs**.

### Actual Result

The request **is saved**. The form closes and an 11th row appears with the budget `R-5 000`. The line reads **Showing 11 jobs** and **Open jobs** changes from 8 to 9. No error message is shown.

### Severity Reason

🔴 High - A negative budget is invalid money data. It is stored as a real job, shown in the table, and (together with BUG-001) makes the financial summary unreliable. The app has no delete button, so the user cannot remove the entry.

### Related Test Cases

TC-007. **Automated:** AT-002 (`test_negative_budget_is_rejected`).

### Evidence

- `Evidence/BUG-003-negative-budget.png`
- `Evidence/AT-run-2-failure-messages.png (automated test AT-002 failure message)`

---

## BUG-004 - Completed (Done) jobs are counted and shown as overdue

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Assumption

A job with the status `Done` is finished, so it should not count as overdue even if its due date has passed. Rule used for all expected results: **Overdue = jobs whose due date is before today AND whose status is not Done.** This should be confirmed with the product owner. The numbers below depend on today's date, so the test date is stated.

### Steps to Reproduce

**Part A - original data**

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Read the number in the **Overdue** summary box (middle box). On 8 October 2026 it shows **6**.
4. In the table, find the rows whose **Due date** is before 2026-10-08 and write down each row's **Status**: Kestrel Motors / Showroom poster (2026-10-02, In progress), Brightline Fibre (2026-09-25, **Done**), Harbour Fleet Leasing (2026-10-06, In progress), Visit Karoo (2026-09-30, Pending), Kestrel Motors / 4x4 bakkie spec sheet (2026-09-28, **Done**), Jozi Events Bureau (2026-10-01, In progress).
5. Count only the rows that are past due **and not Done**. The answer is 4.
6. Look at the colour of the two **Done** rows (Brightline Fibre and the 4x4 bakkie spec sheet).

**Part B - brand-new Done job**

1. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
2. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
3. Fill in the form fields exactly as follows:
   - **Client name:** `Done Check Co`
   - **Job title:** `Done Check Job`
   - **Due date:** `01 January 2020` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1234`
   - **Status:** `Done`
4. Click the black **Save request** button at the bottom-right of the form.
5. Wait one second. Read the **Overdue** box and look at the colour of the new last row.

### Expected Result

Part A: **Overdue = 4** and the two Done rows are shown in normal black text.

Part B: **Overdue stays 6** and the new Done row is black.

### Actual Result

Part A: **Overdue = 6**. The two Done jobs are counted and shown in red.

Part B: **Overdue changes from 6 to 7** and the new Done row is red. (**Open jobs** correctly stays at 8, so the app does know the job is finished; only the overdue check ignores the status.)

### Severity Reason

🟠 Medium - The Overdue box overstates the amount of late work (6 shown, 4 real), so a manager would chase finished jobs and could miss the real late ones. Users can still use the rest of the tracker, so the impact is Medium.

### Notes / Suspected Cause

Date dependence: the same bug appeared on earlier dates with different numbers. The original screenshot (taken on or before 6 October 2026, before Harbour Fleet Leasing's due date of 2026-10-06 counted as past) showed Overdue = 5 against a correct figure of 3. On 8 October 2026 it shows 6 against a correct figure of 4. The wrong behaviour is the same; the numbers move with the date, so always compare with the rule above.

### Related Test Cases

TC-011, TC-028.

### Evidence

- `Evidence/BUG-004-completed-jobs-overdue.png (original screenshot, Overdue 5)`

---

## BUG-005 - "Showing N jobs" line does not change when a search or filter is used

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click in the **Search client or job title** box (wide box under the summary boxes) and type `Kestrel Motors`.
4. Count the rows in the table, then read the grey line above the table (**Showing ... jobs**).
5. Delete the search text (select it and press Delete). Open the **All statuses** drop-down (right of the search box) and choose **Pending**. Count the rows and read the grey line again.
6. Choose **All statuses** again. Type `zzz` in the search box. Count the rows and read the grey line again.

### Expected Result

Search `Kestrel Motors`: 2 rows and the line reads **Showing 2 jobs**.

Status **Pending**: 3 rows and the line reads **Showing 3 jobs**.

Search `zzz`: 0 rows and the line reads **Showing 0 jobs**.

### Actual Result

The table filters correctly (2 rows, 3 rows and 0 rows), but the line always reads **Showing 10 jobs**, so it is wrong in all three cases.

### Severity Reason

🟠 Medium - The count is wrong whenever the user filters, which is the main way to use the list. The user sees "0 rows" next to "Showing 10 jobs", which is contradictory and could make them doubt the whole page.

### Related Test Cases

TC-012, TC-014, TC-016, TC-035, TC-037, TC-038.

### Evidence

- `Evidence/BUG-005-search-result-count.png`

---

## BUG-006 - Search is case-sensitive (Client name and Job title)

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Assumption

A user-facing search should find a job whatever capital letters the user types.

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click in the **Search client or job title** box and type `Kestrel Motors` (capital K and M). Count the rows.
4. Replace the text with `kestrel motors` (all lowercase). Count the rows and read the table message.
5. Replace the text with `Annual report` and count the rows. Then replace it with `annual report` (lowercase) and count the rows again.

### Expected Result

`Kestrel Motors` and `kestrel motors` both show the **same 2 rows**. `Annual report` and `annual report` both show the **same 1 row** (Ridgeway Mining).

### Actual Result

`Kestrel Motors` shows 2 rows but `kestrel motors` shows **0 rows** with the message `No jobs match your filters.` `Annual report` shows 1 row but `annual report` shows **0 rows**. The same happened with a job the tester created (`Test Job` found, `test job` not found).

### Severity Reason

🟠 Medium - Users do not type capital letters consistently, so existing jobs appear to be missing. They may create duplicates (see BUG-010) because they think the job does not exist.

### Related Test Cases

TC-013, TC-024, TC-025.

### Evidence

- `Evidence/BUG-006-case-sensitive-search.png`

---

## BUG-007 - Clear filters does not clear the Search box

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

**Example 1 - search and status together**

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Type `Visit` in the **Search client or job title** box.
4. Open the **All statuses** drop-down and choose **Pending**. One row (Visit Karoo) remains.
5. Click the **Clear filters** button (right of the drop-down).
6. Look at the search box, the drop-down and the number of rows.

**Example 2 - search only**

1. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
2. Type `zzz` in the search box. The table shows 0 rows.
3. Click **Clear filters**.
4. Look at the search box and the number of rows.

### Expected Result

Example 1 and 2: the search box becomes **empty**, the drop-down shows **All statuses**, and the table shows all **10 jobs**.

### Actual Result

Example 1: the drop-down returns to All statuses, but `Visit` stays in the search box and the table still shows **1 row**.

Example 2: `zzz` stays in the search box and the table still shows **0 rows**. Clicking Clear filters visibly does nothing.

### Severity Reason

🟠 Medium - A button called "Clear filters" leaves a filter active. In Example 2 the user sees an empty table, presses the button that should fix it, and nothing changes, so they may think the data was lost. The workaround is to delete the text by hand.

### Notes / Suspected Cause

Resetting the drop-down works; only the search box is ignored (see TC-040 for the drop-down on its own).

### Related Test Cases

TC-015, TC-040, TC-041.

### Evidence

- `Evidence/BUG-007-clear-filters.png`

---

## BUG-008 - Page does not fit a phone-sized screen

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F12** (or Ctrl+Shift+I) to open Chrome DevTools.
3. Click the **Toggle device toolbar** icon (small phone-and-tablet icon at the top-left of the DevTools panel), or press **Ctrl+Shift+M**.
4. In the device list at the top of the page choose **iPhone 16** (viewport 393 x 852). Press **F5** to reload.
5. Look at the page without scrolling, then drag the page sideways with the mouse to the right edge.

### Expected Result

All content fits across the **393 px** screen width: the **+ New request** button, all three summary boxes, the search box, the drop-down, the Clear filters button and all six table columns are visible without sideways dragging (the table may scroll inside its own box).

### Actual Result

Only the left part of the page is visible. The page is wider than the 393 px screen, so the user has to drag sideways to reach **Total budget**, **+ New request**, the **status drop-down**, **Clear filters**, and the **Due date**, **Status** and **Budget** columns.

### Severity Reason

🟠 Medium - The tracker works but is awkward on a phone: the main action button and the budget figures are off-screen. The functions remain reachable by dragging, so the impact is Medium.

### Notes / Suspected Cause

Suspected cause: in DevTools > Elements > Styles, the page wrapper (`.wrap`) has `min-width: 820px`, which forces the page to be wider than a phone.

### Related Test Cases

TC-017.

### Evidence

- `Evidence/BUG-008-mobile-left-view.png`
- `Evidence/BUG-008-mobile-right-view.png`
- `Evidence/BUG-008-mobile-view-new-request-view.png`

---

## BUG-009 - "Done" status filter always shows no jobs

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. In the table, count the jobs whose **Status** pill reads **Done**: Brightline Fibre and Kestrel Motors / 4x4 bakkie spec sheet update. That is **2** jobs.
4. Click the **All statuses** drop-down (right of the search box).
5. Choose **Done** from the list.
6. Count the rows in the table and read the grey **Showing** line.

### Expected Result

The table shows the **2 Done jobs** (Brightline Fibre and the 4x4 bakkie spec sheet update).

### Actual Result

The table shows **0 job rows** and the message `No jobs match your filters.` The grey line still reads **Showing 10 jobs** (see BUG-005). The other options work: **Pending** shows 3 rows and **In progress** shows 5 rows.

### Severity Reason

🟠 Medium - One of the three status filters is completely broken, so a user can never list finished work. The rest of the page still works, so the impact is Medium.

### Notes / Suspected Cause

Suspected cause: the **Done** option's internal value is `Completed`, but jobs are stored with the status `Done`, so nothing matches. (Visible in DevTools > Elements on the drop-down.)

### Related Test Cases

TC-036. **Automated:** AT-003 (`test_done_filter_shows_done_jobs`).

### Evidence

- `Evidence/BUG-009-done-filter.png`
- `Evidence/AT-run-2-failure-messages.png (automated test AT-003 failure message)`

---

## BUG-010 - Clicking Save twice creates duplicate jobs

**Severity:** 🔴 High

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields exactly as follows:
   - **Client name:** `Dup Co`
   - **Job title:** `Dup Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1234`
   - **Status:** `Pending`
5. Double-click the black **Save request** button (two quick clicks), or click it twice within one second.
6. Wait one second for the form to close. Count the new rows at the bottom of the table.
7. Read the **Open jobs** box, the **Total budget** box and the grey **Showing** line.

### Expected Result

**One** new job (`Dup Co`) is added. The table has **11 rows**, **Open jobs = 9**, and the line reads **Showing 11 jobs**.

### Actual Result

**Two identical** `Dup Co / Dup Job` jobs are added (rows 11 and 12). The table has **12 rows**, **Open jobs = 10**, and the line reads **Showing 12 jobs**. The Total budget rises by R1 234 (it shows R101 534 instead of R100 300 for a single save).

### Severity Reason

🔴 High - One accidental double-click creates a duplicate record that inflates Open jobs and adds the budget to the Total budget a second time. The app has no Delete or Edit button, so the user cannot remove the duplicate; the only way to get rid of it is to reload the page, which also discards every other request added since. The form shows "Saving..." for about one second and the Save button stays clickable, which invites the extra click.

### Notes / Suspected Cause

Suspected cause: the Save button is not disabled while the request is being saved.

### Related Test Cases

TC-022.

### Evidence

- `Evidence/BUG-010-duplicate-job.png`

---

## BUG-011 - Cancel clicked while saving still adds the job

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields exactly as follows:
   - **Client name:** `Cancel Co`
   - **Job title:** `Cancel Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
5. Click the black **Save request** button at the bottom-right of the form.
6. **Immediately** (within one second, while the red text `Saving...` is shown under the Status field) click the **Cancel** button.
7. Check that the form closes, then wait two seconds.
8. Count the rows in the table and read the **Open jobs** box.

### Expected Result

Because the user cancelled, **no job is added**. The table still has **10 rows**, **Open jobs = 8** and the line reads **Showing 10 jobs**.

### Actual Result

The form closes, but about one second later the `Cancel Co` job **appears** as row 11. The table has **11 rows** and **Open jobs = 9**.

### Severity Reason

🟠 Medium - The user explicitly cancelled, yet a record is created. There is no Delete button to remove it, and it changes Open jobs and the totals, so the user is left with data they did not want.

### Notes / Suspected Cause

Cancelling **before** clicking Save works correctly (TC-009). Only the one-second window after Save is affected.

### Related Test Cases

TC-042.

### Evidence

- `Evidence/BUG-011-cancel-still-saves.png`

---

## BUG-012 - HTML tags typed in Client name and Job title are interpreted instead of shown as text

**Severity:** 🔴 High

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields exactly as follows:
   - **Client name:** `<b>Test</b>`
   - **Job title:** `<i>Test</i>`
   - **Due date:** `01 December 2026` (click the calendar icon and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
5. Click the black **Save request** button at the bottom-right of the form.
6. Wait one second, then look closely at the **Client** and **Job** cells of the new last row.

### Expected Result

The row shows exactly the characters that were typed: `<b>Test</b>` in the Client cell and `<i>Test</i>` in the Job cell, in normal (not bold, not italic) text.

### Actual Result

The row shows only the word **Test** in both cells, the Client cell in **bold** and the Job cell in *italics*. The typed characters `<b>` and `</b>` / `<i>` and `</i>` are not displayed.

### Severity Reason

🔴 High - Whatever a user types is run as part of the page instead of shown as text. This is a recognised security weakness (cross-site scripting, XSS): a malicious entry could run code for anyone who opens the tracker. High because of the security risk.

### Notes / Suspected Cause

Characters that are normal in company names (`'`, `&` and quotes, e.g. `O'Brien & Sons "Ltd"`) display correctly (TC-020). The problem is specific to angle-bracket tags. Suspected cause: the table is built by inserting the typed text directly into the page without escaping it.

### Related Test Cases

TC-019, TC-020, TC-023.

### Evidence

- `Evidence/BUG-012-html-rendered.png`

---

## BUG-013 - A budget of 0 is accepted

**Severity:** 🟡 Low

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Assumption

A job budget should be greater than R0. The brief does not state this rule, so it must be confirmed with the product owner (a free job may be allowed).

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields exactly as follows:
   - **Client name:** `WTC`
   - **Job title:** `Free Campaign`
   - **Due date:** `20 October 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `0`
   - **Status:** `Pending`
5. Click the black **Save request** button at the bottom-right of the form.
6. Wait one second and read the budget in the new last row.

### Expected Result

The request is **not saved** and a message asks for a budget greater than 0. The table still has **10 rows**.

### Actual Result

The request **is saved**. An 11th row appears with the budget `R0`, and no message is shown.

### Severity Reason

🟡 Low - A zero-value job is probably a data-entry mistake and would not be caught. The impact is small and depends on a business rule that is not stated, so Low.

### Related Test Cases

TC-008.

### Evidence

- `Evidence/BUG-013-zero-budget.png`

---

## BUG-014 - Decimal budgets are shown with one decimal place (R1 500,5)

**Severity:** 🟡 Low

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields exactly as follows:
   - **Client name:** `Decimal Co`
   - **Job title:** `Decimal Job`
   - **Due date:** `01 December 2026` (click the small calendar icon inside the field and pick this date)
   - **Budget (R):** `1500.50`
   - **Status:** `Pending`
5. Click the black **Save request** button at the bottom-right of the form.
6. Wait one second and read the budget in the new last row.

### Expected Result

The row shows the amount with two decimal places: `R1 500,50`.

### Actual Result

The row shows `R1 500,5` (one decimal place).

### Severity Reason

🟡 Low - Money should show cents. `R1 500,5` looks like a typing mistake, but the stored amount is correct, so the impact is cosmetic.

### Related Test Cases

TC-030.

### Evidence

- `Evidence/BUG-014-decimal-budget.png`

---

## BUG-015 - Client name has no length limit and a very long name stretches the layout

**Severity:** 🟡 Low

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. In **Client name** type the letter `a` 150 times. (Tip: type ten a's, select them, copy them, then paste fifteen times.)
5. Fill in the other fields as follows:
   - **Job title:** `Long Name Job`
   - **Due date:** `01 December 2026` (click the calendar icon and pick this date)
   - **Budget (R):** `1000`
   - **Status:** `Pending`
6. Click the black **Save request** button at the bottom-right of the form.
7. Wait one second, then look at the whole page, including the right-hand columns.

### Expected Result

The field stops accepting text at a sensible limit (for example 100 characters), or the long name wraps inside its column so that the table keeps its normal width and all six columns stay visible.

### Actual Result

All **150 characters** are accepted and the table/page layout stretches to fit the long name.

### Severity Reason

🟡 Low - One long entry can push other columns out of view for everyone. The data is still saved and reachable by scrolling, so the impact is Low.

### Related Test Cases

TC-021.

### Evidence

- `Evidence/BUG-015-long-name.png`

---

## BUG-016 - A due date with a 5-digit year (e.g. 20206) is treated as overdue

**Severity:** 🟠 Medium

**Environment:**
- Windows
- Google Chrome (Version 154.0.8037.93)
- Desktop
- Local Job Request Tracker test build (`job-tracker-demo.html`)
- Tested on: 8 October 2026

### Steps to Reproduce

1. Open the file `job-tracker-demo.html` in Google Chrome (double-click the file, or drag it into a Chrome window). A page titled **Job Request Tracker** opens.
2. Press **F5** to reload the page so that only the original 10 jobs are listed. Check the starting figures (as at 8 October 2026): **Open jobs = 8**, **Overdue = 6**, **Total budget = R87 800**, and the line above the table reads **Showing 10 jobs**.
3. Click the black **+ New request** button at the top-right of the page. A form titled **New job request** opens.
4. Fill in the form fields as follows:
   - **Client name:** `Year Check Co`
   - **Job title:** `Year Check Job`
   - **Budget (R):** `1234`
   - **Status:** leave as `Pending`
5. Click the **year part** of the **Due date** field (the last number in the date) and type `20206` in place of the year, so the year part of the field reads 20206.
6. Click the black **Save request** button at the bottom-right of the form.
7. Wait one second. Look at the colour of the new last row and read the **Overdue** and **Open jobs** boxes.

### Expected Result

The date is far in the future, so the row is **black**, **Overdue stays 6** and **Open jobs changes from 8 to 9**. (Better still, the form rejects a year with more than four digits.)

### Actual Result

The row is shown in **red**, **Overdue changes from 6 to 7**, and Open jobs changes from 8 to 9.

### Severity Reason

🟠 Medium - A single extra digit typed by mistake produces a false overdue job and a wrong Overdue count, with no warning from the form. The date field gives no protection, so a Medium.

### Notes / Suspected Cause

Suspected cause: dates are compared as text, character by character, so `20206-...` is placed before `2026-...`.

### Related Test Cases

TC-029.

### Evidence

- `Evidence/BUG-016-five-digit-year.png`

---

# Observations (not counted as defects)

## OBS-01 - New requests can be saved with a past or unrealistic due date

**Severity:** Low (question for the product owner)

**Steps:** Open the app and press F5. Click **+ New request**, enter valid data with **Due date** `01 January 2020` (or a date in the year 1000), status `Pending`, and click **Save request**.

**Expected (assumption):** a warning, or the form only accepts today or a future date.

**Actual:** the request is saved with no warning. With `01 January 2020` the row turns red and **Overdue changes from 6 to 7** (correct for a Pending job). A job due **today** (08 October 2026) is saved and shown in black (correct: not yet late).

**Why it is only an observation:** back-capturing old jobs may be intended. Needs a decision from the product owner. The related 5-digit-year problem is logged as BUG-016.

**Related:** TC-026, TC-027.


## OBS-02 - The application has no way to edit or delete a job

**Severity:** n/a (suggestion)

**Observation:** after a job is added there is no Edit or Delete button, and the table rows cannot be selected. The data also disappears when the page is reloaded (F5).

**Why it matters:** mistakes and duplicates (BUG-010, BUG-011) and invalid entries (BUG-003, BUG-013) cannot be corrected, which raises the impact of those bugs.

**Why it is not a defect:** the brief does not say editing or deleting should exist. Suggested as an improvement for the product owner.

**Related:** TC-022, TC-042.


---


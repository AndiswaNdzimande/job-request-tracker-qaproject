
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

# Job Request Tracker - Test Cases

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

**Result:** PASS with known issue

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

**Result:** FAIL

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

**Result:** PASS with known issue

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

**Result:** PASS
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

**Result:** PASS
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

**Result:** PASS

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

**Result:** FAIL

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

**Result:** FAIL based on documented assumption

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

**Result:** PASS
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

**Result:** PASS
### TC-011 - Verify completed past-due jobs are not treated as overdue

**Priority:** P1 - Critical

**Test Type:** Functional / Business Rule Testing

**Assumption:**

A job with a status of `Done` should no longer be considered overdue, even when its due date has passed.

**Steps:**

1. Open the Job Request Tracker.
2. Observe the displayed Overdue count.
3. Identify jobs with due dates before the current date.
4. Check the status of each past-due job.
5. Compare the number of unfinished past-due jobs with the displayed Overdue count.
6. Observe whether completed past-due jobs are visually marked as overdue.

**Expected Result:**

Only jobs with a past due date that are not `Done` should be considered overdue.

Jobs with a status of `Done` should not contribute to the Overdue count or be visually marked as overdue.
**Actual Result:**

The application displays an Overdue count of 5.

Five jobs have due dates before the current date. However, two of these jobs have a status of `Done`.

The two completed jobs are also displayed in red as though they are overdue.

Based on the assumption that completed jobs should no longer be considered overdue, only 3 unfinished jobs should be counted as overdue.

**Result:** FAIL

**Related Bug:** BUG-004
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

**Result:** FAIL

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

**Result:** FAIL

**Related Bug:** BUG-006

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

**Result:** PASS with known issue

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

**Result:** FAIL

**Related Bug:** BUG-007


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

**Result:** PASS with known issue

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

**Result:** FAIL

**Related Bug:** BUG-008
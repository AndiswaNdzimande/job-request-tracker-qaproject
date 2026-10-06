# Job Request Tracker - Bug Report
## BUG-001 - Total Budget does not equal the sum of displayed job budgets

**Severity:** High

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Observe the 10 jobs displayed in the table.
3. Record the budget of each job.
4. Add the 10 displayed budget values.
5. Compare the calculated total with the Total Budget displayed by the application.

### Expected Result

The Total Budget should equal the sum of all displayed job budgets.

The 10 displayed jobs have a combined budget of R100,300.

### Actual Result

The application displays a Total Budget of R87,800.

The displayed amount is R12,500 lower than the sum of the displayed job budgets.

### Severity Reason

High - The application displays incorrect financial information, which could cause users to make decisions using inaccurate budget data.

### Evidence

Screenshot showing the 10 jobs and the displayed Total Budget of R87,800.
## BUG-002 - Client Name required validation message contains a spelling error

**Severity:** Low

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Leave Client Name empty.
4. Enter valid information into the remaining required fields.
5. Click **Save request**.

### Expected Result

The request should not be saved and the following validation message should be displayed:

`Client name is required.`

### Actual Result

The request is correctly prevented from being saved, but the validation message displays:

`Client name is requred.`

The word "required" is misspelled.

### Severity Reason

Low - The validation functionality works correctly and the user can understand the message, but the spelling error reduces the professionalism and quality of the user interface.

### Evidence

`Evidence/BUG-002-client-name-validation.png`

## BUG-003 - New Request form accepts negative budget values

**Severity:** High

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Click **+ New request**.
3. Enter `WTC` as the Client Name.
4. Enter `Website Design` as the Job Title.
5. Select `20 October 2026` as the Due Date.
6. Enter `-5000` as the Budget.
7. Select `Pending`.
8. Click **Save request**.

### Expected Result

The request should not be saved.

The application should display a validation message informing the user that the budget must be a valid non-negative or positive monetary amount.

### Actual Result

The application saves the request successfully.

The new job appears in the table with the budget displayed as:

`R-5 000`

No validation error is displayed.

### Severity Reason

High - Invalid financial data can be saved as a legitimate job budget. This can affect the accuracy of financial information and calculations within the tracker.

### Evidence

`Evidence/BUG-003-negative-budget.png`
## BUG-004 - Completed jobs are counted and displayed as overdue

**Severity:** Medium

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Assumption

A job with a status of `Done` should no longer be considered overdue, even if its due date has passed.

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Observe the Overdue summary.
3. Identify jobs with due dates before the current date.
4. Check the statuses of those jobs.
5. Observe the completed jobs with past due dates.

### Expected Result

Only jobs whose due dates have passed and whose status is not `Done` should be considered overdue.

Based on the current data, the expected Overdue count is 3.

Completed jobs should not be visually marked as overdue.

### Actual Result

The application displays an Overdue count of 5.

Two of the five jobs counted as overdue have a status of `Done`.

The completed jobs are also displayed in red.

### Severity Reason

Medium - The application gives a misleading representation of outstanding work, but users can still access and use the main job-tracking functionality.

### Evidence

`Evidence/BUG-004-completed-jobs-overdue.png`
## BUG-005 - Job result count does not update when filters are applied

**Severity:** Medium

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Confirm that 10 jobs are initially displayed.
3. Enter `Kestrel Motors` in the Search field.
4. Observe the filtered job table.
5. Observe the job count displayed above the table.

### Expected Result

The table should display the two jobs matching `Kestrel Motors`.

The result counter should update to:

`Showing 2 jobs`

### Actual Result

The table correctly displays only the two matching Kestrel Motors jobs.

However, the result counter continues to display:

`Showing 10 jobs`
The job table is filtered correctly, but the result counter continues to display `Showing 10 jobs`.

This occurs when filtering using both:

- The Search field
- The Status filter

For example, selecting `Pending` correctly displays 3 jobs, but the counter still displays `Showing 10 jobs`

### Severity Reason

Medium - Search filtering works, but the displayed result count is inaccurate and could mislead users about the number of matching records.

### Evidence

`Evidence/BUG-005-search-result-count.png`
## BUG-006 - Search is case-sensitive

**Severity:** Medium

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Assumption

A user-facing search should return matching client names or job titles regardless of letter casing.

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Enter `Kestrel Motors` in the Search field.
3. Observe that two matching jobs are displayed.
4. Replace the search term with `kestrel motors`.
5. Observe the search results.

### Expected Result

The search should be case-insensitive.

Searching for `kestrel motors` should return the same two jobs as searching for `Kestrel Motors`.

### Actual Result

Searching for `Kestrel Motors` returns two matching jobs.

Searching for `kestrel motors` returns no jobs and displays:

`No jobs match your filters.`

### Severity Reason

Medium - The search feature works only when users enter matching capitalization, which can prevent users from finding existing jobs even when they enter the correct client name.

### Evidence

`Evidence/BUG-006-case-sensitive-search.png`
## BUG-007 - Clear filters does not clear the Search field

**Severity:** Medium

**Environment:**
- Windows
- Google Chrome
- Desktop
- Local Job Request Tracker test build

### Steps to Reproduce

1. Open the Job Request Tracker.
2. Enter `Visit` in the Search field.
3. Select `Pending` from the Status filter.
4. Confirm that the table is filtered to the matching job.
5. Click `Clear filters`.
6. Observe the Search field and displayed jobs.

### Expected Result

Clicking `Clear filters` should reset all active filters.

The Search field should become empty, the Status filter should return to `All statuses`, and all jobs should be displayed.


### Actual Result

Clicking `Clear filters` resets the Status filter to `All statuses`, but it does not clear the active Search field.

The search term remains entered and the table remains filtered by that search term.

In this test, `Visit` remained in the Search field and only the Visit Karoo job remained visible.

### Severity Reason

Medium - The Clear filters control does not fully perform the action indicated by its label, requiring the user to manually remove the search term.

### Evidence

`Evidence/BUG-007-clear-filters.png`
## BUG-008 - Application does not adapt correctly to phone-sized screens

**Severity:** Medium

**Environment:**
- Windows
- Google Chrome
- Chrome Device Toolbar
- iPhone 16
- Viewport: 393 × 852

### Steps to Reproduce

1. Open the Job Request Tracker in Google Chrome.
2. Open Chrome Developer Tools.
3. Enable the Device Toolbar.
4. Select `iPhone 16`.
5. Observe the application.
6. Horizontally drag the page to access content outside the initial viewport.

### Expected Result

The application should provide a usable responsive layout on a phone-sized screen.

Important controls and information should fit or adapt appropriately for the smaller viewport.

### Actual Result

The page maintains a layout wider than the phone viewport.

Important information and controls are positioned outside the initial visible area. The user must horizontally drag across the page to access:

- Total Budget
- New Request
- Status filter
- Clear Filters
- Due Date
- Status
- Budget

### Severity Reason

Medium - The functionality remains accessible through horizontal dragging, but the layout provides a poor mobile user experience and makes important controls and information difficult to access.

### Evidence

- `Evidence/BUG-008-mobile-left-view.png`
- `Evidence/BUG-008-mobile-right-view.png`
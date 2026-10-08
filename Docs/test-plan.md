
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

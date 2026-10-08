
# Job Request Tracker - QA Test Summary Report

## 1. Document Information

**Project:** Job Request Tracker QA Challenge  
**Document:** QA Test Summary Report  
**Testing Type:** Manual and Automated QA Testing  
**Automation Tools:** Python, pytest and Playwright  
**Tester:** Andiswa Ndzimande  
**Test dates:** first session on or before 6 October 2026; second control-by-control session on 8 October 2026  
**Status:** ✅ Testing Completed

---

# 2. Executive Summary

Quality Assurance testing was performed on the supplied **Job Request Tracker** application to evaluate its functionality, validation, calculations, search and filtering behaviour, input handling, usability, and mobile responsiveness.

The testing process combined **manual testing** with a focused **automated regression suite**.

A total of **42 manual test cases** were executed (✅ 12 PASS, ⚠️ 10 PASS with known issue, ❌ 20 FAIL).

Testing identified **16 documented defects**:

- 4 High-severity defects
- 8 Medium-severity defects
- 4 Low-severity defects

Two further items were recorded as observations for the product owner (OBS-01 past due dates accepted, OBS-02 no edit or delete) and are not counted as defects.

The most significant findings relate to **financial-data integrity and data quality**: the application displays an incorrect Total Budget (the newest job is always left out), accepts negative budgets, creates duplicate jobs when Save is clicked twice, and displays HTML typed into text fields as page content (a security risk).

A second testing session applied a control-by-control checklist to every control on the page. It found eight further defects (BUG-009 to BUG-016), including a status filter option that never works ("Done"), and strengthened the earlier findings with additional examples.

Following manual testing, three important defects were automated using **Python, pytest and Playwright**: two High-severity defects (BUG-001 incorrect Total Budget and BUG-003 negative budget accepted) and one Medium-severity defect (BUG-009 the "Done" status filter shows no jobs). Each automated test asserts the **correct** behaviour and is marked as an expected failure (`xfail`) with its bug ID, so the suite runs cleanly while still tracking the defects. Current automation results:

- 3 expected failures (XFAIL), each reproducing a known application defect
- 0 unexpected failures or errors

Running the suite with `--runxfail` shows the real failure message of each test.

Based on the testing performed, the application should **not be considered release-ready until the High-severity defects have been addressed and successfully retested**.

---

# 3. Testing Objectives

The primary objectives of testing were to:

- Verify that core Job Request Tracker functionality works correctly.
- Validate the New Request form.
- Verify required-field validation.
- Test valid and invalid budget values.
- Verify Total Budget calculations.
- Verify overdue-job behaviour.
- Test search functionality.
- Test status filtering.
- Verify Clear Filters behaviour.
- Verify filtered job-result counts.
- Evaluate desktop usability.
- Evaluate mobile responsiveness.
- Identify defects that could affect users or data accuracy.
- Capture evidence supporting identified defects.
- Automate selected high-value regression scenarios.

---

# 4. Test Scope

## In Scope

The following areas were included in testing:

### New Job Requests

- Creating valid job requests
- Required Client Name validation
- Required Job Title validation
- Required Due Date validation
- Required Budget validation
- Negative budget values
- Zero-value, decimal and very large budget testing
- Special characters, HTML-like text and very long text in text fields
- Duplicate submission (double-click Save) and Cancel while saving
- Due date handling: past date, today, and a 5-digit year
- Cancelling a request
- Creating requests with different statuses

### Dashboard and Business Rules

- Open Jobs
- Overdue Jobs
- Total Budget
- Job table information
- Completed-job overdue behaviour
- "Showing N jobs" line

### Search and Filtering

- Search by Client Name
- Search by Job Title
- Search using different letter casing
- Status filtering (every option: Pending, In progress, Done)
- Search and status filter used together
- Clear Filters (after a status filter and after a search)
- Filtered result counts

### Responsive Behaviour

- Mobile dashboard layout
- Horizontal page behaviour
- Mobile access to controls
- Mobile New Request form

### Automation

- Total Budget equals the sum of the jobs (BUG-001)
- Negative budget is rejected (BUG-003)
- "Done" status filter lists the Done jobs (BUG-009)

---

# 5. Test Approach

A **risk-based testing approach** was used.

Higher-risk functionality, particularly functionality affecting financial information and core job creation, was given greater attention.

Testing techniques included:

- Functional Testing
- Positive Testing
- Negative Testing
- Boundary Testing
- Exploratory Testing
- Responsive Testing
- Automated Browser Testing
- Regression Testing

Manual testing was used for broad application coverage.

Automation was then introduced for selected scenarios that were important, repeatable, and suitable for regression testing.

---

# 6. Test Environment

## Manual Testing

**Operating System:** Windows  
**Browser:** Google Chrome  
**Application:** Job Request Tracker QA test build  
**Application Type:** Local HTML application  
**Mobile Testing Tool:** Chrome DevTools Device Toolbar  
**Mobile Device:** iPhone 16  
**Mobile Viewport:** 393 × 852

## Automated Testing

**Language:** Python 3.14.2  
**Framework:** pytest 9.1.1  
**Browser Automation:** Playwright 1.63.0  
**Plugin:** pytest-playwright 0.9.0  
**Browser:** Chromium  
**Environment:** Python virtual environment (`venv`)

---

# 7. Manual Test Execution Summary

A total of **42 manual test cases** were executed:

| Result | Count |
|---|---|
| ✅ PASS | 12 |
| ⚠️ PASS with known issue | 10 |
| ❌ FAIL | 20 |

("PASS with known issue" means the feature under test behaves correctly and the only difference from the expected result is a problem already logged under another bug, for example the wrong "Showing N jobs" line.)

The test cases covered:

- Core job-request creation
- Form validation (empty, spaces only, negative, zero, decimal, very large)
- Special characters, HTML-like text and very long text
- Calculation behaviour (Total budget after adding jobs)
- Overdue-job handling, including today's date and Done jobs
- Duplicate submission and Cancel while saving
- Search (casing, partial text, no match), every status filter option, Clear Filters
- Responsive design

Detailed test steps, expected results, actual results, and test outcomes are documented in:

`Docs/test-cases.md`

Supporting screenshots are stored in:

`Evidence/`

---

# 8. Defect Summary

Testing identified **16 documented defects** (4 High, 8 Medium, 4 Low).

| Bug ID | Defect | Severity | Automation |
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

Two observations are recorded separately: OBS-01 (new requests can be saved with a past or unrealistic due date) and OBS-02 (no way to edit or delete a job).

Detailed reproduction steps and evidence references are documented in:

`Docs/bug-report.md`

---

# 9. 🔴 High-Severity Findings

## BUG-001 - Incorrect Total Budget

The application displays **R87 800**, while the 10 original jobs add up to **R100 300**, a difference of **R12 500**. R12 500 is exactly the budget of the last job in the list. When a new job is added, the new job is the one left out (adding R1 000 shows R100 300 instead of R101 300). The error was reproduced with five different new jobs and by automated test **AT-001**.

### Risk

Users may make decisions using an incorrect representation of the total value of tracked work.

### Recommendation

The Total Budget calculation should be corrected (it appears to skip the final row) and regression tested before release.

---

## BUG-003 - Negative Budget Values Are Accepted

The application allows a negative budget such as `-5000` to be saved and displays it as `R-5 000`.

### Risk

Allowing invalid negative financial values can compromise the accuracy and integrity of the application's financial information.

### Recommendation

Budget validation should prevent negative values from being submitted (reproduced by automated test **AT-002**). The handling of a zero-value budget (BUG-013) should also be confirmed with the product owner.

---

## BUG-010 - Clicking Save Twice Creates Duplicate Jobs

Two quick clicks on **Save request** created two identical jobs (12 rows instead of 11, Open jobs 10 instead of 9). The Total budget also rose by the duplicate's budget.

### Risk

One accidental double-click creates a duplicate record that inflates the counts and totals. The application has no Delete button, so the user cannot remove the duplicate; reloading the page also discards every other new request.

### Recommendation

Disable the Save button as soon as it is clicked (or ignore repeat clicks) and show a clear saving state. Consider adding Edit and Delete features (OBS-02).

---

## BUG-012 - HTML Typed in Text Fields Is Interpreted as Page Content

`<b>Test</b>` in Client name and `<i>Test</i>` in Job title were displayed as **bold** and *italic* text instead of the characters typed.

### Risk

This is a recognised security weakness (cross-site scripting): a malicious entry could run code for anyone who opens the tracker.

### Recommendation

Display all user-typed text as plain text (escape it) before showing it in the table, and retest with special characters.

---

# 10. 🟠 Medium-Severity Findings

8 Medium-severity findings were documented:

- **BUG-004:** Completed (Done) jobs are counted and shown as overdue
- **BUG-005:** "Showing N jobs" line does not change when a search or filter is used
- **BUG-006:** Search is case-sensitive (Client name and Job title)
- **BUG-007:** Clear filters does not clear the Search box
- **BUG-008:** Page does not fit a phone-sized screen
- **BUG-009 (automated: AT-003):** "Done" status filter always shows no jobs
- **BUG-011:** Cancel clicked while saving still adds the job
- **BUG-016:** A due date with a 5-digit year (e.g. 20206) is treated as overdue

These issues do not necessarily prevent the core application from functioning, but they can cause incorrect information, confusing behaviour, or poor usability.

BUG-004 and BUG-006 are based on documented QA assumptions and should be confirmed against the intended product requirements. BUG-004 depends on today's date: the same defect showed Overdue = 5 (expected 3) in the first session and Overdue = 6 (expected 4) on 8 October 2026.

---

# 11. 🟡 Low-Severity Findings

4 Low-severity findings were documented:

- **BUG-002:** Client name validation message contains a spelling error ("requred")
- **BUG-013:** A budget of 0 is accepted
- **BUG-014:** Decimal budgets are shown with one decimal place (R1 500,5)
- **BUG-015:** Client name has no length limit and a very long name stretches the layout

BUG-002 is a user-facing spelling issue rather than a failure of the validation logic. BUG-013 depends on a business rule that the brief does not state (whether a zero budget is allowed) and must be confirmed with the product owner.

---

# 12. Automated Testing Summary

Three important checks were automated using:

- Python 3.14.2
- pytest 9.1.1
- Playwright 1.63.0 (with pytest-playwright 0.9.0)
- Chromium

The automated files are in the `Automation` folder:

| File | Purpose |
|---|---|
| `Automation/conftest.py` | Shared setup: finds the app, a page object (`JobTrackerPage`) and the `tracker` fixture that opens a fresh copy of the app for each test |
| `Automation/tests/test_job_tracker.py` | The three automated checks (AT-001 to AT-003) |
| `Automation/pytest.ini` | pytest settings |
| `Automation/requirements.txt` | Packages to install |

The three checks were chosen because they cover the two most serious defects (High) and one broken feature (Medium), and because their results do not depend on today's date. Automation was deliberately focused on these scenarios rather than duplicating all 42 manual test cases.

> [!NOTE]
> Each test describes the **correct** behaviour and is marked `xfail(raises=AssertionError, strict=True)` with its bug ID. `raises=AssertionError` means only a failed check counts as the known bug (a missing file or timeout still shows as a real error). `strict=True` means that when a defect is fixed, the test passes and pytest reports XPASS(strict) as a failure, which is the reminder to remove the `xfail` marker.

---

# 13. Automated Test Results

| Test | Description | Related Defect | Severity | Result (`python -m pytest -v`) |
|---|---|---|---|---|
| AT-001 | Total budget equals the sum of the jobs | BUG-001 | 🔴 High | 🟣 XFAIL |
| AT-002 | A negative budget is rejected | BUG-003 | 🔴 High | 🟣 XFAIL |
| AT-003 | The "Done" filter shows the Done jobs | BUG-009 | 🟠 Medium | 🟣 XFAIL |

## Automation Totals

**Total automated checks:** 3  
**Expected failures (XFAIL):** 3  
**Unexpected failures or errors:** 0

The three XFAIL results represent known application defects. They are **not automation framework failures**.

With `python -m pytest --runxfail` the same tests fail with these messages:

| Test | Failure message |
|---|---|
| AT-001 | Total budget shows R87,800, but the 10 jobs add up to R100,300 (difference R12,500) |
| AT-002 | A job with a budget of -5000 was saved: the table went from 10 to 11 jobs |
| AT-003 | The Done filter shows 0 jobs, but 2 jobs have the status Done |

---

# 14. Automation Findings

## AT-001 - Total Budget Equals the Sum of the Jobs

**Result:** 🟣 XFAIL (BUG-001)

The test reads the Budget value of every job in the table, adds them up itself, and compares the answer with the Total budget box. The expected value is **calculated by the test**, not hard-coded.

**Calculated:** R100,300  
**Displayed:** R87,800  
**Difference:** R12,500

This independently reproduces the financial calculation defect found during manual testing.

---

## AT-002 - A Negative Budget Is Rejected

**Result:** 🟣 XFAIL (BUG-003)

The test counts the jobs, opens the New request form, enters a budget of `-5000`, clicks Save, waits for the app to finish saving, and counts the jobs again. The correct behaviour is that no job is added.

**Jobs before:** 10  
**Jobs after:** 11

The application saved the invalid job.

---

## AT-003 - The "Done" Filter Shows the Done Jobs

**Result:** 🟣 XFAIL (BUG-009)

The test counts the jobs whose status is Done in the full list, chooses **Done** in the status filter, and counts the rows again.

**Done jobs in the list:** 2  
**Rows shown after filtering:** 0

The filter option never matches.

The tests should remain unchanged until the defects are fixed. When a defect is fixed, its test starts to pass, pytest reports XPASS(strict) as a failure, and the `xfail` marker should then be removed.

---

# 15. Automated Test Evidence

Automated test execution evidence is stored in the `Evidence/` directory.

| Run | Command (from the `Automation` folder) | Evidence |
|---|---|---|
| Run 1 | `python -m pytest -v` - three XFAIL results with their bug IDs | `Evidence/AT-run-1-expected-failures.png` |
| Run 2 | `python -m pytest --runxfail` - the real failure messages | `Evidence/AT-run-2-failure-messages.png` |

---

# 16. Manual Test Evidence

Manual testing evidence is stored in:

`Evidence/`

Evidence was captured for findings including:

- Incorrect Total Budget (original data and after adding a job)
- Client Name validation spelling
- Negative and zero budget acceptance
- Completed jobs included as overdue (original data and a new Done job)
- Incorrect filtered result count (including the empty search showing 10 jobs)
- Case-sensitive search (Client name and Job title)
- Clear Filters behaviour (after a status filter and after an empty search)
- Mobile responsiveness
- Done status filter showing no jobs
- Duplicate job after a double-click on Save
- Cancel while saving still adding the job
- HTML tags displayed as formatting
- Decimal budget display
- Very long client name
- Five-digit due year treated as overdue

Automated execution evidence:

- `Evidence/AT-run-1-expected-failures.png`
- `Evidence/AT-run-2-failure-messages.png`

The evidence supports the reproduction steps and actual results documented in the bug report.

---

# 17. Traceability

Testing maintains traceability between manual testing, identified defects, automated tests, and supporting evidence.

| Functional Area | Manual Coverage | Defect | Automation | Evidence |
|---|---|---|---|---|
| Client Name validation | Yes | BUG-002 | Not automated | Manual |
| Total Budget | Yes | BUG-001 | AT-001 | Manual + Automated |
| Negative budget | Yes | BUG-003 | AT-002 | Manual + Automated |
| Zero / decimal budget | Yes | BUG-013, BUG-014 | Not automated | Manual |
| Overdue and Done jobs | Yes | BUG-004 | Not automated | Manual |
| Result count | Yes | BUG-005 | Not automated | Manual |
| Search case sensitivity | Yes | BUG-006 | Not automated | Manual |
| Clear Filters | Yes | BUG-007 | Not automated | Manual |
| Mobile responsiveness | Yes | BUG-008 | Not automated | Manual |
| Status filter (Done option) | Yes | BUG-009 | AT-003 | Manual + Automated |
| Double-click Save | Yes | BUG-010 | Not automated | Manual |
| Cancel while saving | Yes | BUG-011 | Not automated | Manual |
| HTML in text fields | Yes | BUG-012 | Not automated | Manual |
| Long text | Yes | BUG-015 | Not automated | Manual |
| Due date years | Yes | BUG-016 | Not automated | Manual |

---

# 18. Assumptions

Where expected behaviour was not explicitly defined by the supplied requirements, QA assumptions were documented rather than treated as confirmed requirements.

Important assumptions included:

1. Displayed summary values should accurately represent the underlying displayed job data.
2. Negative financial values should not be accepted as valid budgets.
3. A valid job budget is assumed to be greater than zero.
4. Completed jobs should not normally continue to be counted as overdue.
5. User-facing search should normally be case-insensitive.
6. Text typed by a user should be displayed exactly as typed (no HTML interpretation).
7. A new request should not be saved twice by a double-click.
8. The absence of Edit and Delete features is an observation (OBS-02), not a defect, and whether past due dates are allowed for new requests (OBS-01) is a question for the product owner.
9. The Overdue figure depends on today's date; the expected values in this report are for 8 October 2026.

Findings that depend on product assumptions should be confirmed with the product owner.

---

# 19. Limitations

Testing was performed against the supplied local HTML QA build.

The following limitations apply:

- Testing was performed primarily in Google Chrome.
- Automated browser testing was performed using Chromium.
- Mobile testing used Chrome DevTools emulation rather than a physical iPhone.
- Cross-browser testing across Firefox, Safari, and Edge was not part of the completed scope.
- Performance testing was not performed.
- Security testing was limited to basic input-handling checks (special characters and HTML-like text); no penetration testing was performed.
- Accessibility testing was not performed as a dedicated test phase.
- Backend/API testing was not applicable to the supplied local HTML test build.
- Automation covers selected regression scenarios rather than the complete manual test suite. The automated suite covers three defects (BUG-001, BUG-003, BUG-009); the High-severity defects BUG-010 (duplicate save) and BUG-012 (HTML in text fields) are not yet automated.
- Results that depend on the current date (Overdue) were recorded on 8 October 2026.

These limitations should be considered when interpreting the final QA assessment.

---

# 20. Risk Assessment

The greatest current risks are **financial-data integrity** and **data quality**.

BUG-001 and BUG-003 can result in incorrect financial information being displayed or stored. BUG-010 can create duplicate records that inflate counts and totals, and the application provides no way to delete them. BUG-012 is a security risk because typed text is interpreted as page content.

Additional risks include:

- Incorrect operational information from overdue calculations (BUG-004, BUG-016).
- Confusing or broken search and filtering behaviour (BUG-005, BUG-006, BUG-007, BUG-009).
- Cancelling a request that is then saved anyway (BUG-011).
- Poor usability on mobile devices (BUG-008).
- Minor loss of professionalism from validation-message spelling, decimal formatting and layout issues (BUG-002, BUG-014, BUG-015).

---

# 21. Release Recommendation

> [!CAUTION]
> **Recommendation: NOT READY FOR RELEASE**


Based on the testing performed, the current application build should **not be considered release-ready without remediation of the High-severity defects**.

### 🔴 Must Fix

**BUG-001 - Incorrect Total Budget** (automated: AT-001)

Financial summary information must accurately reflect the underlying job data.

**BUG-003 - Negative Budget Values Are Accepted** (automated: AT-002)

Invalid negative financial values should not be accepted.

**BUG-010 - Clicking Save Twice Creates Duplicate Jobs**

One accidental double-click must not create duplicate records.

**BUG-012 - HTML Typed in Text Fields Is Interpreted as Page Content**

User-typed text must be displayed as text to remove the security risk.

### 🟠 Should Review / Fix

- **BUG-004:** Completed (Done) jobs are counted and shown as overdue
- **BUG-005:** "Showing N jobs" line does not change when a search or filter is used
- **BUG-006:** Search is case-sensitive (Client name and Job title)
- **BUG-007:** Clear filters does not clear the Search box
- **BUG-008:** Page does not fit a phone-sized screen
- **BUG-009:** "Done" status filter always shows no jobs
- **BUG-011:** Cancel clicked while saving still adds the job
- **BUG-016:** A due date with a 5-digit year (e.g. 20206) is treated as overdue

### 🟡 Lower Priority

- **BUG-002:** Client name validation message contains a spelling error ("requred")
- **BUG-013:** A budget of 0 is accepted
- **BUG-014:** Decimal budgets are shown with one decimal place (R1 500,5)
- **BUG-015:** Client name has no length limit and a very long name stretches the layout

Although the Low-severity defects do not affect the core workflow, BUG-002 and BUG-014 should still be corrected before a polished production release.

---

# 22. Retesting Recommendation

After defects are fixed, QA should perform:

1. Defect verification testing for every bug in the bug report.
2. Regression testing of affected functionality.
3. Full rerun of the automated test suite (`python -m pytest -v` from the `Automation` folder).
4. Retesting of Total Budget calculations with non-zero amounts, including after adding jobs.
5. Negative, zero, decimal and boundary testing of Budget validation.
6. Retesting of search (casing) and **every** status filter option.
7. Retesting of overdue calculations on the day of retest, including Done jobs and unusual year values.
8. Retesting of double-click Save and Cancel while saving.
9. Retesting of special characters and HTML-like text in Client name and Job title.
10. Responsive testing after mobile-layout changes.

AT-001, AT-002 and AT-003 should remain unchanged until the corresponding defects are corrected.

Once a defect is fixed, its test passes and pytest reports **XPASS(strict)** as a failure. That is the signal to remove its `xfail` marker so that the test becomes a normal regression test:

- AT-001 (BUG-001) should change from XFAIL to **PASS**.
- AT-002 (BUG-003) should change from XFAIL to **PASS**.
- AT-003 (BUG-009) should change from XFAIL to **PASS**.

Recommended additional automated checks (not yet implemented): a double-click on Save adds only one job (BUG-010), and HTML tags typed into text fields are shown as text (BUG-012).

---

# 23. Final QA Conclusion

The Job Request Tracker provides functioning core workflows, including job creation, required-field validation, search, three of its four status filter options, and job-data display.

However, testing identified **16 documented defects**: **4 High**, **8 Medium** and **4 Low**.

The most significant problems are the incorrect Total Budget (it always leaves out the newest job: R87 800 shown against R100 300), the acceptance of negative budgets, duplicate jobs created by a double-click on Save, and HTML typed into text fields being interpreted as page content.

Manual testing provided broad functional and exploratory coverage across **42 documented test cases** (✅ 12 PASS, ⚠️ 10 PASS with known issue, ❌ 20 FAIL). A second, control-by-control session applying the same checklist to every input produced eight additional defects, which shows the value of testing every option and every input rather than one example of each feature.

Targeted automated testing was implemented using Python, pytest, and Playwright to provide repeatable regression coverage for selected high-value functionality. The automated suite reproduces three known defects (two High, one Medium) as expected failures and is ready to become passing regression tests once the defects are fixed.

Based on the evidence collected, the application should **not be released until the High-severity defects have been corrected, retested, and verified**.

After remediation, the relevant manual tests and the complete automated regression suite should be rerun before a final release decision is made.

# Job Request Tracker - QA Test Summary Report

## 1. Document Information

**Project:** Job Request Tracker QA Challenge  
**Document:** QA Test Summary Report  
**Testing Type:** Manual and Automated QA Testing  
**Automation Tools:** Python, pytest and Playwright  
**Status:** Testing Completed

---

# 2. Executive Summary

Quality Assurance testing was performed on the supplied **Job Request Tracker** application to evaluate its functionality, validation, calculations, search and filtering behaviour, usability, and mobile responsiveness.

The testing process combined **manual testing** with a focused **automated regression suite**.

A total of **17 manual test cases** were executed.

Testing identified **8 documented defects**:

- 2 High-severity defects
- 5 Medium-severity defects
- 1 Low-severity defect

The most significant findings relate to financial-data integrity. The application displays an incorrect Total Budget and also allows negative budget values to be saved.

Following manual testing, selected high-value scenarios were automated using **Python, pytest and Playwright**.

The automation suite includes a smoke/setup check and three targeted automated tests.

Current automation results are:

- 2 Passed
- 2 Failed because of known application defects

Based on the testing performed, the application should **not be considered release-ready until the high-severity financial defects have been addressed and successfully retested**.

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
- Zero-value budget boundary testing
- Cancelling a request
- Creating requests with different statuses

### Dashboard and Business Rules

- Open Jobs
- Overdue Jobs
- Total Budget
- Job table information
- Completed-job overdue behaviour

### Search and Filtering

- Search by Client Name
- Search by Job Title
- Search using different letter casing
- Status filtering
- Clear Filters
- Filtered result counts

### Responsive Behaviour

- Mobile dashboard layout
- Horizontal page behaviour
- Mobile access to controls
- Mobile New Request form

### Automation

- Application smoke test
- Valid request creation
- Client Name required validation
- Total Budget calculation

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

A total of **17 manual test cases** were executed.

The test cases covered:

- Core job-request creation
- Form validation
- Budget validation
- Calculation behaviour
- Overdue-job handling
- Search
- Filtering
- Result counts
- Clear Filters behaviour
- Responsive design

Detailed test steps, expected results, actual results, and test outcomes are documented in:

`Docs/test-cases.md`

Supporting screenshots are stored in:

`Evidence/`

---

# 8. Defect Summary

Testing identified **8 documented defects**.

| Bug ID | Defect | Severity | Automation |
|---|---|---|---|
| BUG-001 | Total Budget does not equal the sum of displayed job budgets | High | AT-003 |
| BUG-002 | Client Name validation message contains a spelling error | Low | AT-002 |
| BUG-003 | Negative budget values are accepted | High | Manual |
| BUG-004 | Completed jobs are counted and displayed as overdue | Medium | Manual |
| BUG-005 | Job result count does not update after filtering | Medium | Manual |
| BUG-006 | Search is case-sensitive | Medium | Manual |
| BUG-007 | Clear Filters does not clear Search | Medium | Manual |
| BUG-008 | Poor mobile responsiveness | Medium | Manual |

Detailed reproduction steps and evidence references are documented in:

`Docs/bug-report.md`

---

# 9. High-Severity Findings

## BUG-001 - Incorrect Total Budget

The application displays:

**R87,800**

However, the budgets of the 10 displayed jobs add up to:

**R100,300**

This creates a difference of:

**R12,500**

The issue affects financial-data accuracy and was reproduced independently by automated test **AT-003**.

### Risk

Users may make decisions using an incorrect representation of the total value of tracked work.

### Recommendation

The Total Budget calculation should be corrected and regression tested before release.

---

## BUG-003 - Negative Budget Values Are Accepted

The application allows a negative budget such as:

`-5000`

to be saved.

The application then displays the value as:

`R-5 000`

### Risk

Allowing invalid negative financial values can compromise the accuracy and integrity of the application's financial information.

### Recommendation

Budget validation should prevent negative values from being submitted.

The expected handling of a zero-value budget should also be confirmed with the product owner.

---

# 10. Medium-Severity Findings

Five Medium-severity findings were documented:

- **BUG-004:** Completed jobs are counted and displayed as overdue.
- **BUG-005:** The displayed result count does not update after filtering.
- **BUG-006:** Search is case-sensitive.
- **BUG-007:** Clear Filters does not clear the Search field.
- **BUG-008:** The application is poorly responsive on a phone-sized viewport.

These issues do not necessarily prevent the core application from functioning, but they can cause incorrect information, confusing behaviour, or poor usability.

BUG-004 and BUG-006 are based on documented QA assumptions and should be confirmed against the intended product requirements.

---

# 11. Low-Severity Finding

## BUG-002 - Client Name Validation Spelling

Client Name validation correctly prevents an incomplete request from being submitted.

However, the application displays:

`Client name is requred.`

instead of:

`Client name is required.`

This is a user-facing spelling issue rather than a failure of the validation logic.

The defect was reproduced by automated test **AT-002**.

---

# 12. Automated Testing Summary

A focused automated regression suite was implemented using:

- Python
- pytest
- Playwright
- Chromium

The automated test file is:

`Automation/tests/test_job_tracker.py`

Automation was deliberately focused on selected high-value scenarios rather than duplicating all 17 manual test cases.

---

# 13. Automated Test Results

| Test | Description | Result | Related Defect |
|---|---|---|---|
| Setup Check | Verify the application opens successfully | PASS | None |
| AT-001 | Create a valid job request | PASS | None |
| AT-002 | Required Client Name validation | FAIL | BUG-002 |
| AT-003 | Verify Total Budget calculation | FAIL | BUG-001 |

## Automation Totals

**Total automated checks:** 4  
**Passed:** 2  
**Failed:** 2

The two failed tests represent known application defects.

They are **not automation framework failures**.

The tests intentionally assert the correct expected behaviour so that they can become passing regression tests when the underlying defects are fixed.

---

# 14. Automation Findings

## AT-001 - Valid Job Request

**Result: PASS**

The automated test successfully:

- Opened the New Request form.
- Entered valid request information.
- Saved the request.
- Verified that the new client appeared.
- Verified that the new job appeared.

This confirms that the core valid job-creation workflow functions successfully for the tested scenario.

---

## AT-002 - Client Name Validation

**Result: FAIL**

**Related Defect:** BUG-002

The automation intentionally expects:

`Client name is required.`

The application displays:

`Client name is requred.`

The request is correctly rejected, but the validation text is incorrect.

The test should remain unchanged until the application defect is fixed.

---

## AT-003 - Total Budget

**Result: FAIL**

**Related Defect:** BUG-001

The automated test reads the Budget value from each displayed job and independently calculates the expected total.

**Calculated:** R100,300  
**Displayed:** R87,800  
**Difference:** R12,500

This independently reproduces the financial calculation defect identified during manual testing.

---

# 15. Automated Test Evidence

Automated test execution evidence is stored in the `Evidence/` directory.

| Test | Evidence |
|---|---|
| AT-001 | `Evidence/AT-001-create-valid-job-pass.png` |
| AT-002 | `Evidence/AT-002-client-validation-fail.png` |
| AT-003 | `Evidence/AT-003-total-budget-fail.png` |

---

# 16. Manual Test Evidence

Manual testing evidence is also stored in:

`Evidence/`

Evidence was captured for findings including:

- Incorrect Total Budget
- Client Name validation spelling
- Negative budget acceptance
- Completed jobs included as overdue
- Incorrect filtered result count
- Case-sensitive search
- Clear Filters behaviour
- Mobile responsiveness

The evidence supports the reproduction steps and actual results documented in the bug report.

---

# 17. Traceability

Testing maintains traceability between manual testing, identified defects, automated tests, and supporting evidence.

| Functional Area | Manual Coverage | Defect | Automation | Evidence |
|---|---|---|---|---|
| Valid job creation | Yes | None | AT-001 | Automated |
| Client Name validation | Yes | BUG-002 | AT-002 | Manual + Automated |
| Total Budget | Yes | BUG-001 | AT-003 | Manual + Automated |
| Negative Budget | Yes | BUG-003 | Not automated | Manual |
| Overdue completed jobs | Yes | BUG-004 | Not automated | Manual |
| Result count | Yes | BUG-005 | Not automated | Manual |
| Search case sensitivity | Yes | BUG-006 | Not automated | Manual |
| Clear Filters | Yes | BUG-007 | Not automated | Manual |
| Mobile responsiveness | Yes | BUG-008 | Not automated | Manual |

---

# 18. Assumptions

Where expected behaviour was not explicitly defined by the supplied requirements, QA assumptions were documented rather than treated as confirmed requirements.

Important assumptions included:

1. Displayed summary values should accurately represent the underlying displayed job data.
2. Negative financial values should not be accepted as valid budgets.
3. A valid job budget is assumed to be greater than zero.
4. Completed jobs should not normally continue to be counted as overdue.
5. User-facing search should normally be case-insensitive.

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
- Security testing was not performed.
- Accessibility testing was not performed as a dedicated test phase.
- Backend/API testing was not applicable to the supplied local HTML test build.
- Automation covers selected regression scenarios rather than the complete manual test suite.

These limitations should be considered when interpreting the final QA assessment.

---

# 20. Risk Assessment

The greatest current risk is **financial-data integrity**.

BUG-001 and BUG-003 can result in incorrect financial information being displayed or stored.

Additional risks include:

- Incorrect operational information from overdue calculations.
- Confusing search and filtering behaviour.
- Incorrect result counts.
- Poor usability on mobile devices.
- Minor loss of professionalism from validation-message spelling errors.

---

# 21. Release Recommendation

## Recommendation: NOT READY FOR RELEASE

Based on the testing performed, the current application build should **not be considered release-ready without remediation of the High-severity defects**.

The following defects should be prioritised before release:

### Must Fix

**BUG-001 - Incorrect Total Budget**

Financial summary information must accurately reflect the underlying job data.

**BUG-003 - Negative Budget Values Are Accepted**

Invalid negative financial values should not be accepted.

### Should Review / Fix

- BUG-004 - Completed jobs counted as overdue
- BUG-005 - Incorrect filtered result count
- BUG-006 - Case-sensitive search
- BUG-007 - Clear Filters does not clear Search
- BUG-008 - Poor mobile responsiveness

### Lower Priority

- BUG-002 - Client Name validation spelling error

Although BUG-002 is low severity, it should still be corrected before a polished production release.

---

# 22. Retesting Recommendation

After defects are fixed, QA should perform:

1. Defect verification testing.
2. Regression testing of affected functionality.
3. Full rerun of the automated test suite.
4. Retesting of Total Budget calculations.
5. Negative and boundary testing of Budget validation.
6. Retesting of search and filtering.
7. Retesting of overdue calculations.
8. Responsive testing after mobile-layout changes.

AT-002 and AT-003 should remain unchanged until the corresponding defects are corrected.

Once fixed:

- AT-002 should change from **FAIL** to **PASS**.
- AT-003 should change from **FAIL** to **PASS**.

This provides repeatable regression protection against those defects returning.

---

# 23. Final QA Conclusion

The Job Request Tracker provides functioning core workflows, including job creation, required-field validation, search, filtering, and job-data display.

However, testing identified **8 documented defects**, including **2 High-severity financial-data issues**.

The most significant problem is the incorrect Total Budget. The application displays **R87,800**, while the displayed jobs total **R100,300**.

The application also accepts negative budget values, creating an additional financial-data integrity risk.

Manual testing provided broad functional and exploratory coverage across **17 documented test cases**.

Targeted automated testing was subsequently implemented using Python, pytest, and Playwright to provide repeatable regression coverage for selected high-value functionality.

The automated suite successfully verifies valid job creation and automatically reproduces two known defects.

Based on the evidence collected, the application should **not be released until the High-severity financial defects have been corrected, retested, and verified**.

After remediation, the relevant manual tests and the complete automated regression suite should be rerun before a final release decision is made.
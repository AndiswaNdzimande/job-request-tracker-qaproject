# Job Request Tracker - QA Challenge

## Project Overview

This repository contains my Quality Assurance testing work for the **Job Request Tracker QA Challenge**.

The objective of the project is to evaluate the supplied Job Request Tracker application before release by identifying functional, validation, calculation, usability, and responsive-design issues that could affect users.

The testing approach focuses on the application's core functionality, including:

- Creating new job requests
- Required-field validation
- Budget validation and calculations
- Job status handling
- Overdue-job behaviour
- Search functionality
- Status filtering
- Clear Filters functionality
- Job count and summary information
- Desktop usability
- Mobile/responsive behaviour

The project currently contains the completed **manual testing phase**. Browser automation will be added as the next phase of the challenge.

---

## Testing Approach

Testing was performed using a risk-based approach, with higher-risk functionality tested before lower-impact usability issues.

The following testing techniques were used:

- Functional Testing
- Positive Testing
- Negative Testing
- Boundary Testing
- Exploratory Testing
- Responsive Testing

Automation using Playwright is planned for the next phase.

---

## Test Environment

Manual testing was performed using:

- **Operating System:** Windows
- **Browser:** Google Chrome
- **Application:** Job Request Tracker QA test build
- **Desktop Testing:** Google Chrome desktop browser
- **Mobile Testing:** Chrome DevTools Device Toolbar
- **Mobile Device:** iPhone 16
- **Mobile Viewport:** 393 × 852
- **Application Type:** Local HTML application

---

## Manual Testing Summary

A total of **17 manual test cases** were executed.

The tests covered:

### New Request Form

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

- Total Budget calculation
- Overdue-job calculation
- Treatment of completed jobs with past due dates

### Search and Filtering

- Search by Client Name
- Search by Job Title
- Search using different letter casing
- Status filtering
- Clear Filters functionality
- Filtered job-result count

### Responsive Testing

The application was tested using the Chrome Device Toolbar with an **iPhone 16 viewport of 393 × 852**.

The mobile test included:

- Dashboard visibility
- Summary information
- Search and filter controls
- Job table usability
- Horizontal page behaviour
- Access to the New Request form

---

## Key Findings

Manual testing identified **8 documented defects**.

### BUG-001 - Incorrect Total Budget

**Severity: High**

The 10 displayed jobs have a combined budget of **R100,300**, but the application displays **R87,800**.

The displayed Total Budget is therefore **R12,500 lower** than the sum of the displayed job budgets.

---

### BUG-002 - Client Name validation message contains a spelling error

**Severity: Low**

Client Name validation correctly prevents submission when the field is empty.

However, the validation message displays:

`Client name is requred.`

instead of:

`Client name is required.`

---

### BUG-003 - Negative budget values are accepted

**Severity: High**

The New Request form accepts negative budget values.

For example, a budget of `-5000` can be saved successfully and is displayed as:

`R-5 000`

Invalid financial data should not be accepted as a valid job budget.

---

### BUG-004 - Completed jobs are counted and displayed as overdue

**Severity: Medium**

Based on the documented assumption that a completed job should no longer be considered overdue, the application incorrectly includes completed jobs with past due dates in the Overdue count.

The application displays **5 overdue jobs**, while only **3** of those jobs are unfinished.

This finding is based on a documented business-rule assumption and would require confirmation from the product owner.

---

### BUG-005 - Job result count does not update when filters are applied

**Severity: Medium**

Search and Status filtering correctly reduce the jobs displayed in the table.

However, the result counter continues to display:

`Showing 10 jobs`

even when fewer jobs are visible.

For example, searching for `Kestrel Motors` displays two matching jobs while the counter continues to show 10.

---

### BUG-006 - Search is case-sensitive

**Severity: Medium**

Searching for:

`Kestrel Motors`

returns the expected jobs.

Searching for:

`kestrel motors`

returns:

`No jobs match your filters.`

This finding is based on the documented assumption that a user-facing search should normally be case-insensitive.

---

### BUG-007 - Clear Filters does not clear the Search field

**Severity: Medium**

Clicking **Clear filters** resets the Status filter to `All statuses`, but it does not clear the Search field.

The existing search term remains active and the table therefore remains filtered.

---

### BUG-008 - Application does not adapt correctly to a phone-sized screen

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

| Bug ID | Description | Severity |
|---|---|---|
| BUG-001 | Total Budget does not equal the sum of displayed job budgets | High |
| BUG-002 | Client Name validation message contains a spelling error | Low |
| BUG-003 | Negative budget values are accepted | High |
| BUG-004 | Completed jobs are counted and displayed as overdue | Medium |
| BUG-005 | Job result count does not update after filtering | Medium |
| BUG-006 | Search is case-sensitive | Medium |
| BUG-007 | Clear Filters does not clear Search | Medium |
| BUG-008 | Poor responsiveness on phone-sized screens | Medium |

---

## Assumptions

Where the supplied requirements did not explicitly define expected behaviour, reasonable QA assumptions were documented.

The main assumptions used during testing were:

1. Displayed summary values should accurately reflect the job data displayed by the application.
2. Invalid financial values should not be accepted as valid job budgets.
3. A valid job budget is assumed to be greater than zero.
4. Jobs with a status of `Done` should not continue to be counted as overdue.
5. User-facing search functionality should be case-insensitive.

Findings based on assumptions are documented as such and may require confirmation from the product owner before being treated as confirmed defects.

---

## Project Structure

```text
job-request-tracker-qaproject/
│
├── Docs/
│   ├── test-plan.md
│   ├── test-cases.md
│   └── bug-report.md
│
├── Evidence/
│   ├── BUG-001-after.png
│   ├── BUG-001-before.png
│   ├── BUG-002-client-name-validation.png
│   ├── BUG-003-negative-budget.png
│   ├── BUG-004-completed-jobs-overdue.png
│   ├── BUG-005-search-result-count.png
│   ├── BUG-006-case-sensitive-search.png
│   ├── BUG-007-clear-filters.png
│   ├── BUG-008-mobile-left-view.png
│   ├── BUG-008-mobile-right-view.png
│   ├── BUG-008-mobile-view-new-request-view.png
│   └── Job-title-is-required.png
│
├── Automation/
│   └── Playwright automation to be added
│
├── .gitignore
└── README.md
```

---

## Documentation

Detailed QA documentation can be found in the `Docs` directory.

### Test Plan

`Docs/test-plan.md`

Contains:

- Testing objective
- Scope
- Test approach
- Test priorities
- Test environment
- Entry criteria
- Exit criteria
- Assumptions and limitations

### Test Cases

`Docs/test-cases.md`

Contains the detailed manual test cases, including:

- Test priority
- Test type
- Test data
- Test steps
- Expected results
- Actual results
- Test result
- Related bug references

### Bug Report

`Docs/bug-report.md`

Contains detailed defect reports including:

- Bug ID
- Severity
- Environment
- Steps to reproduce
- Expected result
- Actual result
- Severity reasoning
- Supporting evidence

### Evidence

The `Evidence` directory contains screenshots captured during manual testing to support the documented findings.

---

## Current Project Status

### Completed

- Test plan
- Manual functional testing
- Positive testing
- Negative testing
- Boundary testing
- Exploratory testing
- Desktop testing
- Mobile/responsive testing
- Test case documentation
- Bug reporting
- Screenshot evidence

### Next Phase

The next phase of the project is **browser automation using Playwright**.

The challenge requires approximately **2–3 important automated checks**.

The planned automation will focus on high-value application behaviour rather than attempting to automate the entire manual test suite.

After automation is completed, this README will be updated with:

- Playwright installation instructions
- Automation project structure
- Commands for running the automated tests
- Automated test coverage
- Final project status

---

## Repository Note

The original Job Request Tracker HTML file supplied for the QA challenge is **not included in this repository**.

The supplied application is treated as test material and is kept outside the repository. This repository contains only the QA documentation, test evidence, and automation work created as part of the challenge.

---

## Overall Manual Testing Conclusion

The Job Request Tracker's main functionality is usable, including creating requests, required-field validation, search, status filtering, and displaying job information.

However, manual testing identified several issues that should be addressed before release.

The highest-priority findings are related to **financial accuracy**:

- The Total Budget does not match the sum of the displayed job budgets.
- Negative budget values can be saved.

Additional issues were identified in search behaviour, filtering, overdue-job handling, validation text, and mobile responsiveness.

Based on the manual testing performed, the application would benefit from fixes to the high-severity financial issues before release, followed by improvements to filtering, search behaviour and responsive usability.

The next stage of this QA project is to automate a small set of high-value checks using Playwright.
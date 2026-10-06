# Job Request Tracker - Test Plan

## 1. Objective

The objective of this testing is to evaluate the Job Request Tracker before release and identify functional, validation, calculation, usability, and responsive design issues that could affect users.

Testing will focus on the application's core functionality, particularly creating job requests, displaying accurate job information, searching and filtering jobs, summary calculations, form validation, and behaviour on desktop and mobile screen sizes.

## 2. Scope

### In Scope

- New job request creation
- New request form validation
- Client name, job title, due date, budget and status fields
- Job list/table display
- Search functionality
- Status filtering
- Clear filters functionality
- Summary information including open jobs, overdue jobs and total budget
- Behaviour of overdue jobs
- Desktop usability and layout
- Mobile/responsive behaviour using the browser device toolbar
- Positive, negative and boundary test scenarios
- Exploratory testing of the page
- Automation of 2–3 important checks

### Out of Scope

- Backend services and APIs, as none were provided for testing
- Database testing, as the supplied application does not provide access to a database
- Authentication and user account testing, as login functionality is not part of the supplied build
- Production deployment and hosting
- Performance or load testing
- Security penetration testing
- Browsers other than the browsers required by the challenge

## 3. Test Approach

Testing will use a risk-based approach. Core functionality and data accuracy will be tested first, followed by supporting functionality, usability and responsive behaviour.

The following testing techniques will be used:

1. **Functional Testing** - Verify that features such as creating requests, searching and filtering work as expected.
2. **Positive Testing** - Test the application using valid user input.
3. **Negative Testing** - Test invalid or missing input to verify that the application handles errors correctly.
4. **Boundary Testing** - Test boundary values such as zero and negative financial values.
5. **Exploratory Testing** - Explore the application beyond predefined test cases to identify unexpected behaviour.
6. **Responsive Testing** - Test the application on desktop and phone-sized screens.
7. **Automated Testing** - Automate 2–3 important functional checks using a browser automation framework.

## 4. Test Priorities

### P1 - Critical

These areas will be tested first because failures could prevent users from completing their main tasks or could result in incorrect business information.

- Creating a new job request
- Required field validation
- Budget input and calculation
- Open job count
- Overdue job count
- Correct storage and display of submitted job information

### P2 - High

These features support users in finding and managing job requests.

- Search functionality
- Status filtering
- Clearing filters
- Job table display
- Status display
- Due date behaviour
- Mobile usability

### P3 - Medium

These areas have lower business impact but still affect the overall user experience.

- Text and spelling
- Visual consistency
- Layout and alignment
- Error message clarity
- General usability

## 5. Test Environment

- **Operating System:** Windows
- **Browser:** Google Chrome :Version 154.0.8037.93 (Official Build) (64-bit)
- **Application:** Job Request Tracker QA test build
- **Desktop Testing:** Chrome desktop browser
- **Mobile Testing:** Chrome DevTools device toolbar
- **Test Type:** Local HTML application

## 6. Entry Criteria

Testing can begin when:

- The supplied Job Request Tracker HTML file can be opened successfully.
- The application loads in the supported browser.
- The main page and New Request form are accessible.

## 7. Exit Criteria

Testing will be considered complete when:

- Planned high-priority test scenarios have been executed.
- New Request form test cases have been completed.
- Identified bugs have been documented with reproduction steps, expected and actual results, severity, environment and evidence where applicable.
- Desktop and mobile testing has been completed.
- 2–3 important checks have been automated.
- Test documentation and automation instructions have been reviewed for clarity.

## 8. Assumptions and Limitations

- Testing is based on the supplied Job Request Tracker test build.
- The tester assumes that displayed summary values should accurately reflect the job data shown by the application.
- The tester assumes that invalid financial values should not be accepted as valid job budgets.
- Testing is time-boxed according to the challenge instructions, so higher-risk functionality is prioritised.
- Testing is limited to functionality available in the supplied build.
- No backend, database or production environment was provided for testing.
- The tester assumes that completed (`Done`) jobs should not be counted as overdue.
- The tester assumes that user-facing search functionality should be case-insensitive.

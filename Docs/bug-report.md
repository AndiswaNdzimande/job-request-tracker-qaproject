
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

<<<<<<< HEAD
# Employee Leave Request Tracker

## Overview
Employee Leave Request Tracker is a custom Odoo 17 module that extends the HR
and Leave Management system to provide better visibility, validation, and reporting for employee leave requests.


## Installation
1. Clone the repository into your Odoo `addons` directory:
   ```bash
   git clone https://github.com/KiruGoit/employee_leave_request_tracker.git
   ```
2. Restart your Odoo server.
3. Log in as Administrator.
4. Go to **Apps → Update Apps List**.
5. Search for **Employee Leave Request Tracker** and install it.

## Features
- Computed leave balance per employee
- Leave health indicator (Good / Warning / Low)
- Direct relation between employees and their leave requests
- Validation to prevent requesting more leave than available leave balance
- Extended leave request form with detailed reason and attachments
- Custom HR menu for Leave Tracking
- Tree, form, and kanban views for leave requests
- PDF report for individual leave requests
- Employee, manager and HR Admin security groups

## Usage

1. Employees:
          - Navigate to HR → Leave Tracker → My Leaves.
           - Click "Create" to submit a leave request.
           - Attach documents if needed and enter reason.

2. Managers:
          - Navigate to HR → Leave Tracker → Team Leaves (Kanban view).
          - Approve or refuse leave requests using quick action buttons.
          - Monitor employee leave statuses.

3.HR:
         - Navigate to HR → Leave Tracker → All Leaves.
         - Print leave requests as PDF reports.
         - Use pivot view to analyze leaves by employee or month.

## Notes
- This module follows Odoo inheritance best practices.
=======

>>>>>>> 400e908d63033b2d30d0ffe96b9f37427ebc0caf

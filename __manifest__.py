{
    "name": "Employee Leave Request Tracker",
    "version": "17.0.1.1",
    "summary": "handle leave requests, tracking, analysis, and reporting",
    "author": "Kiru Odoo wizard",
    "category": "Human Resources",
    "license": "LGPL-3",
    "depends": ["base", "hr", "hr_holidays"],
    "data": [
        "security/leave_security.xml",
        "security/ir.model.access.csv",
        "data/leave_mail_template.xml",
        "report/report_leave.xml",
        "report/hr_leave_report_action.xml",
        #  The action view for smart button
        "views/smart_button_action.xml",
        #  views
        "views/employee_leave_tracker.xml",
        "wizard/bulk_leave_wizard_view.xml",
        # All the action
        "views/employee_leave_tracker_action.xml",
        "views/employee_leave_tracker_menu.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}

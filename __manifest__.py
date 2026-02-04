{
    'name': 'Employee Leave Request Tracker',
    'version': '17.0.0.0',
    'summary': 'handle leave requests, tracking, analysis, and reporting',
    'author': 'Kiru Odoo wizard',
    'category': 'Human Resources',
    'license': 'LGPL-3',
    'depends': [
        'hr',
        'hr_holidays',
        'base',
    ],
    'data': [
            "security/leave_security.xml",
            "security/ir.model.access.csv",
            "views/hr_leave_tracker.xml",
            "views/menu.xml"
             ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'icon': 'static/description/icon.png',
}
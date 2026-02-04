from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    leave_balance = fields.Integer(
        string="Leave Balance",
        compute="_compute_leave_balance",
    
    )

    leave_requests_id = fields.One2many(
        'hr.leave',
        'employee_id',
        string="Leave Requests"
    )

    leave_health = fields.Selection(
        [
            ('good', 'Good'),
            ('warning', 'Warning'),
            ('low', 'Low'),
        ],
        string="Leave Health",
        compute="_compute_leave_health",
        
    )


    # DUMMY 

    @api.depends()
    def _compute_leave_balance(self):      
        #  allocation - used_days.
        for employee in self:
            allocated_days = 20   
            used_days = 8         
            employee.leave_balance = allocated_days - used_days

    @api.depends('leave_balance')
    def _compute_leave_health(self):
        for employee in self:
            if employee.leave_balance > 10:
                employee.leave_health = 'good'
            elif employee.leave_balance > 5:
                employee.leave_health = 'warning'
            else:
                employee.leave_health = 'low'

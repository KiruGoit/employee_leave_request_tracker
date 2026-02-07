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
    
    allocation_ids = fields.One2many('hr.leave.allocation', 
                                     'employee_id',
                                     string='allocation')
    leave_health = fields.Selection(
        [
            ('good', 'Good'),
            ('warning', 'Warning'),
            ('low', 'Low'),
        ],
        string="Leave Health",
        compute="_compute_leave_health",
        
    )
    leave_count = fields.Integer(compute="_compute_leave_count")




    
    @api.depends('leave_requests_id.number_of_days',
                 "allocation_ids.number_of_days")
    def _compute_leave_balance(self):      

        for employee in self:
            # Find all validated leave allocations for an employee
            allocation = self.env['hr.leave.allocation'].search([
                ('employee_id', '=', employee.id),
                ('state', '=', 'validate'),
                ])
            # sum allocated days
            allocated_days = sum(allocation.mapped('number_of_days'))
              
            # Find all  validated leave take by an employee
            leaves = self.env['hr.leave'].search([
                ('employee_id', '=', employee.id),
                ('state', '=', 'validate'),
                    ])
            # Sum used leave
            used_days = sum(leaves.mapped('number_of_days'))
           
            # Find the remaining leave and store it in leave balance 
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


    @api.depends('leave_requests_id.state',)
    def _compute_leave_count(self):
        for employee in self:
            leaves = self.env['hr.leave'].search([
                ('employee_id', '=', employee.id),
                ('state', '=', 'validate')

                    ])
            # count leaves
            employee.leave_count = len(leaves)
            
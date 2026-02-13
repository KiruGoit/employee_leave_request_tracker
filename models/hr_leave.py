from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrLeave(models.Model):
    _inherit = "hr.leave"

    reason_leave = fields.Text(string="Detailed Reason")
    binary_file = fields.Binary(string="Uplead File")
    binary_file_name = fields.Char(string="Binary File Name")
    
    leave_count = fields.Integer(
         string="Leave Count",
         compute='_compute_leave_count',
         store=True
    )
    


    @api.constrains('number_of_days')
    def _check_leave_balance(self):
        for leave in self:
            if leave.number_of_days > leave.employee_id.leave_balance:
                raise ValidationError("Sorry,You leave balance is not enough.")


    @api.depends('state')
    def _compute_leave_count(self):
        for employee in self:
            leaves = self.env['hr.leave'].search([
                ('employee_id', '=', employee.id),
                ('state', '=', 'validate')

                    ])
            # count leaves
            employee.leave_count = len(leaves)
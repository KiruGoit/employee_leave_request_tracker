from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrLeave(models.Model):
    _inherit = "hr.leave"

    reason_leave = fields.Text(string="Detailed Reason")
    binary_file = fields.Binary(string="Uplead File")
    binary_file_name = fields.Char(string="Binary File Name")
    leave_type = fields.Selection([("annual", "Annual"),
                                   ("sick", "Sick"),
                                   ("other", "Other")], string="Leave Type")

    @api.constrains('number_of_days')
    def _check_leave_balance(self):
        for leave in self:
            if leave.number_of_days > leave.employee_id.leave_balance:
                raise ValidationError("Sorry,You leave balance is not enough.")
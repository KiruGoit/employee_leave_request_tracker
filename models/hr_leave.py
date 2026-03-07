from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HrLeave(models.Model):
    _inherit = "hr.leave"

    reason_leave = fields.Text(string="Detailed Reason")
    binary_file = fields.Binary(string="Uplead File")
    binary_file_name = fields.Char(string="Binary File Name")

    leave_count = fields.Integer(
        string="Leave Count", related="employee_id.leave_count"
    )
    leave_health = fields.Selection(
        related="employee_id.leave_health",
        string="Leave Health",
    )
    leave_stats_display = fields.Char(
        related="employee_id.leave_stats_display",
        string="Leave Stats",
    )

    @api.constrains("number_of_days")
    def _check_leave_balance(self):
        for leave in self:
            if leave.number_of_days > leave.employee_id.leave_balance:
                raise ValidationError("Sorry,You leave balance is not enough.")

    def action_approve(self):
        res = super().action_approve()

        template = self.env.ref(
            "employee_leave_request_tracker.email_template_leave_approved"
        )

        for leave in self:
            template.with_context(mail_post_autofollow=False).send_mail(
                leave.id, force_send=True, raise_exception=False
            )
        return res

    def action_refuse(self):
        res = super().action_refuse()

        template = self.env.ref(
            "employee_leave_request_tracker.email_template_leave_rejected"
        )

        for leave in self:
            template.with_context(mail_post_autofollow=False).send_mail(
                leave.id, force_send=True, raise_exception=False
            )

        return res

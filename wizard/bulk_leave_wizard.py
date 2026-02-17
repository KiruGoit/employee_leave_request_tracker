from odoo import models, fields


class BulkLeaveWizard(models.TransientModel):
    _name = 'bulk.leave.wizard'
    _description = 'Bulk Leave Approval Wizard'

    leave_ids = fields.Many2many(
        'hr.leave',
        string="Leave Requests"
    )

    def action_bulk_approve(self):

        for leave in self.leave_ids:
            if leave.state in ['confirm', 'validate1']:
                leave.action_approve()

        return 

    def action_bulk_refuse(self):

        for leave in self.leave_ids:
            if leave.state not in ['refuse', 'cancel']:
                leave.action_refuse()

        return

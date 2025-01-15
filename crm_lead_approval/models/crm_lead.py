# Copyright 2024 INVITU SARL
# License AGPL-3 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    approval = fields.Selection(
        [
            ("none", "None"),
            ("done", "Approve"),
            ("normal", "Reserved"),
            ("blocked", "Disapprove"),
        ],
        default="none",
        tracking=True,
    )
    to_be_approved = fields.Boolean(
        string="To be approved",
        compute="_compute_approve",
        help="Indicates whether the record required approval or not",
    )

    def _compute_approve(self):
        for record in self:
            record.to_be_approved = (
                record.team_id in self.env.company.approval_team_ids
                or record.tag_ids in self.env.company.approval_tag_ids
            )

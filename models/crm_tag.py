# Copyright 2024 Invitu SARL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class Tag(models.Model):
    _inherit = [
        'crm.tag',
    ]

    sales_team_ids = fields.Many2many('crm.team', string='Teams',)

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Tag(models.Model):
    _inherit = [
        'crm.tag',
    ]

    sales_team_ids = fields.Many2many('crm.team', string='Teams',)

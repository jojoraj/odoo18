
from odoo import api, fields, models



class ResCompany(models.Model):
    _inherit = 'res.company'

    inventory_validator_ids = fields.Many2many('res.users')

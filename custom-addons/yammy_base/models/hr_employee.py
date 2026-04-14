# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class hrEmployee(models.Model):
    _inherit = "hr.employee"

    CIN = fields.Char('CIN')
    adress = fields.Char('Adresse')
    tel = fields.Char('Téléphone')

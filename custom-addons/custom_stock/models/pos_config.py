# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class custom_stock(models.Model):
      _inherit = 'pos.config'

      def _check_profit_loss_cash_journal(self):
        return True

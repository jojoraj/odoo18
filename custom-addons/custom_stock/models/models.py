# -*- coding: utf-8 -*-

from odoo import models, fields, api


class custom_stock(models.Model):
      _inherit = 'product.template'

      has_group = fields.Boolean(compute="compute_has_group")

      def compute_has_group(self):
            for rec in self:
                if self.env.user.has_group('custom_stock.group_product_create_restriction'):
                    rec.has_group = True
                else:
                    rec.has_group = False

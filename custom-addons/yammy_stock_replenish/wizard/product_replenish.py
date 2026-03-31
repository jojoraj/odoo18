# -*- coding: utf-8 -*-

from odoo import models


class ProductReplenish(models.TransientModel):
    _inherit = 'product.replenish'

    def _get_record_to_notify(self, date):
        record = super()._get_record_to_notify(date)
        self._alma_auto_validate_replenishment_picking(record)
        return record

    def _alma_auto_validate_replenishment_picking(self, record):
        """Valide tout de suite le picking généré par le réapprovisionnement manuel (routes stock)."""
        if not record or record._name != 'stock.move':
            return
        picking = record.picking_id
        if not picking or picking.state in ('done', 'cancel'):
            return
        picking.action_assign()
        picking.with_context(skip_backorder=True).button_validate()

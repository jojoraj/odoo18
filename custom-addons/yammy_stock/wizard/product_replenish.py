# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import UserError
from odoo.tools import clean_context
from odoo import _
class ProductReplenish(models.TransientModel):
    _inherit = 'product.replenish'

    def launch_replenishment(self):
        if not self.route_id:
            pass
        uom_reference = self.product_id.uom_id
        self.quantity = self.product_uom_id._compute_quantity(self.quantity, uom_reference, rounding_method='HALF-UP')
        try:
            now = self.env.cr.now()
            self.env['procurement.group'].with_context(clean_context(self.env.context)).run([
                self.env['procurement.group'].Procurement(
                    self.product_id,
                    self.quantity,
                    uom_reference,
                    self.warehouse_id.lot_stock_id,  # Location
                    _("Manual Replenishment"),  # Name
                    _("Manual Replenishment"),  # Origin
                    self.warehouse_id.company_id,
                    self._prepare_run_values()  # Values
                )
            ])
            move = self._get_record_to_notify(now)
            notification = self._get_replenishment_order_notification(move)
            act_window_close = {
                'type': 'ir.actions.act_window_close',
                'infos': {'done': True},
            }
            if notification:
                notification['params']['next'] = act_window_close
                return notification
            return act_window_close
        except UserError as error:
            raise UserError(error)

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

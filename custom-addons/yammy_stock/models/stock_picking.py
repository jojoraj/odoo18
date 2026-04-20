
from odoo import api, fields, models, _
from markupsafe import Markup


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    can_validate = fields.Boolean(compute='_compute_can_validate')

    def _compute_can_validate(self):
        has_admin = self.env.user.has_groups('stock.group_stock_manager')
        for picking in self:
            if has_admin or self.env.user.id in picking.company_id.inventory_validator_ids.ids:
                picking.can_validate = True
            else:
                picking.can_validate = False


    def get_picking_link(self):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        action = self.sudo().env.ref('stock.action_picking_tree_incoming').path
        return f'{base_url}/odoo/{action}/{self.id}'

    def send_notification_to_partner(self):
        link = self.get_picking_link()
        body = _('Transfer number <a href="%s">%s</a> has been confirmed and requires your validation.' % (link, self.name))
        partner_id = self.partner_id
        subject = _('Validation of transfert %s' % self.name)
        return self.message_post(
            body=Markup(body),
            partner_ids=[partner_id.id],
            subject=subject,
            subtype_xmlid="mail.mt_comment",
            message_type="notification"
        )

    def action_confirm(self):
        result = super(StockPicking, self).action_confirm()
        for rec in self:
            rec.send_notification_to_partner()
        return result

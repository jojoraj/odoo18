
from odoo import api, fields, models, _
from markupsafe import Markup


class StockPicking(models.Model):
    _inherit = 'stock.picking'

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

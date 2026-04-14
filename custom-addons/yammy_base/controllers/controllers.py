# -*- coding: utf-8 -*-
# from odoo import http


# class CustomStock(http.Controller):
#     @http.route('/yammy_custom_sales/yammy_custom_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/yammy_custom_sales/yammy_custom_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('yammy_custom_sales.listing', {
#             'root': '/yammy_custom_sales/yammy_custom_sales',
#             'objects': http.request.env['yammy_custom_sales.yammy_custom_sales'].search([]),
#         })

#     @http.route('/yammy_custom_sales/yammy_custom_sales/objects/<model("yammy_custom_sales.yammy_custom_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('yammy_custom_sales.object', {
#             'object': obj
#         })


# -*- coding: utf-8 -*-
from odoo import http

# class ExtraAddons/scaffold(http.Controller):
#     @http.route('/extra_addons/scaffold/extra_addons/scaffold/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/extra_addons/scaffold/extra_addons/scaffold/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('extra_addons/scaffold.listing', {
#             'root': '/extra_addons/scaffold/extra_addons/scaffold',
#             'objects': http.request.env['extra_addons/scaffold.extra_addons/scaffold'].search([]),
#         })

#     @http.route('/extra_addons/scaffold/extra_addons/scaffold/objects/<model("extra_addons/scaffold.extra_addons/scaffold"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('extra_addons/scaffold.object', {
#             'object': obj
#         })
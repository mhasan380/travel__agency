# -*- coding: utf-8 -*-
from odoo import http

# class TravelAgency(http.Controller):
#     @http.route('/travel__agency/travel__agency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/travel__agency/travel__agency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('travel__agency.listing', {
#             'root': '/travel__agency/travel__agency',
#             'objects': http.request.env['travel__agency.travel__agency'].search([]),
#         })

#     @http.route('/travel__agency/travel__agency/objects/<model("travel__agency.travel__agency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('travel__agency.object', {
#             'object': obj
#         })
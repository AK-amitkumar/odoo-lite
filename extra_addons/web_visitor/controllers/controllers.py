# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.web.controllers.main import Session
from odoo.http import request
from odoo.exceptions import UserError
from odoo.tools.translate import _

class WebVisitor(http.Controller):

    @http.route('/web/visitor/', type='http', auth='none')
    def get_session(self):
        #TODO: remove hard-code of password
        model, res_id = request.env['ir.model.data'].get_object_reference(
            'web_visitor', 'visitor_user')
        user = request.env[model].search([('id', '=', res_id)])
        if not user:
            raise UserError(_('User not found.'))
        session = Session().authenticate(
            db='odoo11', login=user.login, password='visitor_password')
        request.uid = session['uid']

        context = {}
        context['modules'] = request.env['ir.module.module'].search([])
        context['session_info'] = session
        response = request.render('web_visitor.hello', qcontext=context)
        response.headers['X-Frame-Options'] = 'DENY'
        return response

# -*- coding: utf-8 -*-
import functools
import logging
import werkzeug

from odoo import http
from odoo.addons.web.controllers.main import Session
from odoo.http import request, Response
from odoo.exceptions import UserError
from odoo.tools.translate import _
from odoo.tools import pycompat

_logger = logging.getLogger(__name__)


def route(route=None, **kw):
    # for visitor, to be improved
    kw['cors'] = '*'

    routing = kw.copy()
    assert 'type' not in routing or routing['type'] in ("http", "json")
    def decorator(f):
        if route:
            if isinstance(route, list):
                routes = route
            else:
                routes = [route]
            routing['routes'] = routes

        @functools.wraps(f)
        def response_wrap(*args, **kw):
            response = f(*args, **kw)
            if isinstance(response, Response) or f.routing_type == 'json':
                return response

            if isinstance(response, (bytes, pycompat.text_type)):
                return Response(response)

            if isinstance(response, werkzeug.exceptions.HTTPException):
                response = response.get_response(request.httprequest.environ)
            if isinstance(response, werkzeug.wrappers.BaseResponse):
                response = Response.force_type(response)
                response.set_default()
                return response

            _logger.warn(
                "<function %s.%s> returns an invalid response type for an http request" % (f.__module__, f.__name__))
            return response

        response_wrap.routing = routing
        response_wrap.original_func = f
        return response_wrap
    return decorator

http.route = route

class WebVisitor(http.Controller):

    @http.route('/web/visitor/', type='json', auth='none')
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
        context['session_info'] = session
        # response = request.render('web_visitor.hello', qcontext=context)
        # response.headers['X-Frame-Options'] = 'DENY'
        return {'test': 'test'}

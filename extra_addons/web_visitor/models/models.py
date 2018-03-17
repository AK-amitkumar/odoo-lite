# -*- coding: utf-8 -*-

from odoo import models, fields

class WebAllowedOrigin(models.Model):
    _name = 'web.allowed.origin'

    name = fields.Char(
        string='Origin allowed to connect',
        required=True,
    )
    model_ids = fields.Many2many(
        'ir.model',
        string='Models allowed to access',
        required=True,
    )

# -*- coding: utf-8 -*-
{
    'name': 'test-assetsbundle',
    'version': '0.1',
    'category': 'Tests',
    'description': """A module to verify the Assets Bundle mechanism.""",
    'maintainer': 'Odoo SA',
    'depends': ['base'],
    'installable': True,
    'data': [
        "views/web_allowed_origin.xml",
    ],
    'auto_install': False,
}

# -*- coding: utf-8 -*-
{
    'name': "web_visitor",

    'summary': """
        Visitor management""",

    'description': """
        Expose API to visitor to get resources with session of template common user.
        Home page is ./web/visitor/
    """,

    'author': "RawEvan",
    'website': "https://github.com/RawEvan",
    'category': 'web',
    'version': '0.1',
    'depends': ['web'],

    'data': [
        'web_visitor_data.xml',
        'views/templates.xml',
        'views/web_allowed_origin.xml',
    ],
}
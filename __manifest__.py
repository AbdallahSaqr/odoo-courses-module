# -*- coding: utf-8 -*-
{
    'name': "courses",
    'summary': "Short (1 phrase/line) summary of the module's purpose",
    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.8',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}

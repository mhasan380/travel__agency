# -*- coding: utf-8 -*-
{
    'name': "Travel Agency",

    'summary': """
        Travel Agency Management Software""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Xsellence Bangladesh Limited",
    'website': "http://www.xsellencebdltd.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/op_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/Hajj.xml',
        'views/umrah.xml',
        'views/um_guide_view.xml',
        'views/company.xml',
        'views/ticket.xml',
        'views/soudi_info.xml',
        'views/report.xml',
        'views/hajj_guide_view.xml', 
        'menu/trave_agency_menu.xml',       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
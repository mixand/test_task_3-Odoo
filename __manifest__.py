{
    'name': "Odoo_mixand_s",
    'version': '1.0',
    'depends': ['sale'],
    'author': "mixand_s",
    'category': 'Category',
    'description': """
    test application
    """,

    # # data files always loaded at installation
    'data': [
        'views/sale_order_view.xml',
        'views/sale_report_templates.xml',
    ],
    'application': True,

    # # data files containing optionally loaded demonstration data
    'demo': [
    ],
}

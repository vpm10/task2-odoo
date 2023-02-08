{
    'name': 'Customer from',
    'version': '16.0.1.0.0',
    'sequence': '-4',
    'category': 'purchase',
    'summary': 'Add sale order',
    'description': 'Add sale order',

    'installation': True,

    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_form.xml',
        'views/customer_so.xml',
    ]
}

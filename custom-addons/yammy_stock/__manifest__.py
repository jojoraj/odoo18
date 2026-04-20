# -*- coding: utf-8 -*-
{
    'name': 'Yammy – Validation auto du réappro (stock)',
    'version': '18.0.1.0.0',
    'summary': 'Valide automatiquement le transfert créé par le wizard Réapprovisionner (routes stock).',
    'author': 'Yammy',
    'category': 'Inventory',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
        'views/res_company_views.xml'
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
{
    'name': "My pet - minhng.info",
    'summary': """My pet model""",
    'description': """Managing pet information""",
    'author': "minhng.info",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_pet_views.xml',
        'wizard/batch_update.xml',
        # 'views/templates.xml',
        'views/res_config_settings_views.xml',  # <-- add this
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': {
            'mypet/static/src/js/bold.js',
            'mypet/static/src/js/btn_tree_multi_update.js',
        },
        'web.assets_qweb': {
            'mypet/static/src/xml/btn_tree_multi_update.xml',
        },
    },

}

# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'CRM Tags Sales Team',
    'author': 'INVITU, Cyril VINH-TUNG',
    'website': 'https://www.invitu.com',
    'version': '1.0',
    'category': 'CRM',
    'description': """
This module adds a filter by sales_team for crm_tag.
===========================================================================

    """,
    'depends': ['crm'],
    'data': [
        'views/crm_tag_views.xml',
        'views/crm_lead_views.xml',
    ],
    'installable': True,
}

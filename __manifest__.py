# Copyright 2024 Invitu SARL
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "CRM Tags Sales Team",
    "author": "INVITU, Cyril VINH-TUNG",
    "license": "AGPL-3",
    "website": "https://www.invitu.com",
    "version": "17.0.1.0",
    "category": "CRM",
    "summary": "This module adds a filter by sales_team for crm_tag.",
    "depends": [
        "crm",
    ],
    "data": [
        "views/crm_tag_views.xml",
        "views/crm_lead_views.xml",
    ],
    "installable": True,
}

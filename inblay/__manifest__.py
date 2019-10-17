# -*- coding: utf-8 -*-
# Copyright Vauxoo 2019
{
    'name': "Inblay",
    'summary': """Principal module for Inblay.""",
    'author': 'Vauxoo',
    'website': 'https://www.vauxoo.com',
    'license': 'AGPL-3',
    'category': 'Installer',
    'version': '12.0.0.0.3',
    'depends': [
        'account',
        'account_accountant',
        'base_automation',
        'crm',
        'fleet',
        'helpdesk',
        'hr',
        'hr_appraisal',
        'hr_expense',
        'hr_holidays',
        'hr_recruitment',
        'l10n_mx_reports',
        'l10n_mx_edi',
        'product_management',
        'product_management_accounting',
        'product_management_purchase',
        'product_management_website_sale',
        'project',
        'purchase',
        'sale_management',
        'security_user_roles',
        'stock',
        'stock_barcode',
        'survey',
        'timesheet_grid',
        'website_sale',
        'website',
        # 'smart_warnings', uncomment when this branch is merged
    ],
    'test': [
    ],
    'data': [
        "data/ir_cron.xml",
        "data/base_automation.xml",
        "security/ir.model.access.csv",
        "views/product_view.xml",
        "views/hr_employee.xml",
        "views/assets.xml",
        "views/res_company_view.xml"
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': True,
}

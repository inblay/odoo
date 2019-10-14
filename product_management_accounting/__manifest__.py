# -*- coding: utf-8 -*-
{
    "name": "Product Management Interface: Accounting",
    "version": "12.0.1.0.1",
    "category": "Accounting",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/product-management-interface-accounting-294",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "product_management",
        "account"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/update_prm_saletax.xml",
        "wizard/update_prm_purchasetax.xml",
        "wizard/update_prm_incomeaccount.xml",
        "wizard/update_prm_expenseaccount.xml",
        "wizard/update_prm_invoicepolicy.xml",
        "data/data.xml"
    ],
    "qweb": [
        
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {},
    "summary": "The extension for the tool Product Management Interface to add accounting mass actions",
    "description": """
    This is the add-on which adds a few extra mass accounting actions on product templates.

    Modify invoice policy ('Ordered quantities', 'Delivered quantities')
    Add / remove customer taxes
    Add / remove vendor taxes
    Change income account of products
    Change expense account of templates
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "10.0",
    "currency": "EUR",
}
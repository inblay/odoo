# -*- coding: utf-8 -*-
{
    "name": "Product Management Interface: Purchases",
    "version": "12.0.1.0.1",
    "category": "Purchases",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/product-management-interface-purchases-296",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "product_management",
        "purchase"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/add_prm_vendor.xml",
        "wizard/update_purchase_policy.xml",
        "wizard/update_prm_pricedifferenceaccount.xml",
        "views/product_template.xml",
        "data/data.xml"
    ],
    "qweb": [
        
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {},
    "summary": "The extension for the tool Product Management Interface to add purchasing mass actions",
    "description": """
    This is the add-on which adds a few purchases' mass actions on products.

    Update products to be purchasable / not purchasable
    Assign a new vendor to product templates in bulk and make this supplier the most prioritized
    Update purchase method ('On ordered quantities', 'On received quantities')
    Change price difference account
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "10.0",
    "currency": "EUR",
}
# -*- coding: utf-8 -*-
{
    "name": "Product Management Interface: e-Commerce",
    "version": "12.0.1.0.1",
    "category": "eCommerce",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/product-management-interface-e-commerce-295",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "product_management",
        "website_sale"
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizard/update_prm_public_categories.xml",
        "wizard/update_prm_alternatives.xml",
        "wizard/update_prm_accessories.xml",
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
    "summary": "The extension for the tool Product Management Interface to add e-shop mass actions",
    "description": """
    This is the add-on which adds a few e-Shop mass actions on products.

    Publish or unpublish products in batch
    Add / remove public E-shop categories of selected templates
    Add / remove products' alternatives
    Add / remove products' accessories
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "10.0",
    "currency": "EUR",
}
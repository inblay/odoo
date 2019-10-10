# -*- coding: utf-8 -*-
{
    "name": "Product Management Interface",
    "version": "12.0.1.0.4",
    "category": "Sales",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/product-management-interface-293",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "product"
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/security.xml",
        "views/view.xml",
        "views/res_config_settings.xml",
        "wizard/change_prm_category.xml",
        "wizard/update_prm_attributes.xml",
        "wizard/update_prm_followers.xml",
        "wizard/update_prm_product_type.xml",
        "wizard/update_optional_products.xml",
        "views/product_template.xml",
        "views/menu.xml",
        "data/data.xml"
    ],
    "qweb": [
        "static/src/xml/*.xml"
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {},
    "summary": "The tool to search, select and update product templates in batch",
    "description": """
    This is the product management tool aims to improve catalogue administration and to simplify implementation of changes. The app introduces the innovative interface to search, to analyse, to select, and to mass edit Odoo product templates. The tool consists of the core module and four extra optional add-ons:
<ol style="font-size:18px;">
<li><a href='https://apps.odoo.com/apps/modules/12.0/product_management/'>Product Management Interface</a> - the core app. It might be used stand-alone as a system to find, pick up, and update basic product fields. The price is 92 Euro</li>
<li><a href='https://apps.odoo.com/apps/modules/12.0/product_management_website_sale/'>Product Management Interface: e-Commerce</a> - the optional module, which introduces mass products actions to change E-shop related attributes. The features assumed by this add-on are marked by the icon <i class='fa fa-globe'></i>. The price is 10 Euro</li>
<li><a href='https://apps.odoo.com/apps/modules/12.0/product_management_stock/'>Product Management Interface: Warehouse</a> - the optional module to update in batch warehouse characteristics of product templates. The features assumed by this add-on are marked by the icon <i class='fa fa-building'></i>. The price is 10 Euro</li>
<li><a href='https://apps.odoo.com/apps/modules/12.0/product_management_accounting/'>Product Management Interface: Accounting</a> - the optional module to manage accounting traits of products in bulk. The features assumed by this add-on are marked by the icon <i class='fa fa-money'></i>. The price is 10 Euro</li>
<li><a href='https://apps.odoo.com/apps/modules/12.0/product_management_purchase/'>Product Management Interface: Purchases</a> - the optional module offering mass actions on purchase columns of products. The features assumed by this add-on are marked by the icon <i class='fa fa-shopping-cart'></i>. The price is 10 Euro</li>
</ol>

    Structure products by categories just through ticking check boxes. The tool let you select one or multiple ones, choose only parent category or all children recursively
    Systematize product templates by available attributes values. Now it is not a trouble to select all templates which might be both white and metal
    <i><strong><span style="color: #483d8b">New</span></strong></i> <i class='fa fa-globe'></i> Navigate by E-commerce categories to search products from E-shop perspective 
    Apply standard product filters using Odoo regular search to narrow results 
    Choose an unlimited number of products step by step. A current selection is not spoilt with a new search or when you opened a record. You may also select all products found by you criteria (not only ones displayed on a current page)
    Configure the list of mass actions through selecting among multiple ones offered by the tool. Look for the whole list at the section <a href='#mass_actions'>Mass Actions List</a>
    Execute any of chosen multiple mass actions and observe results in real-time. <i><strong><span style="color: #483d8b">New</span></strong></i> you might define by your own which product fields should be shown on a kanban card in addition to standard columns
    The interface is available for any user which has rights for products (e.g. sales, warehouse or purchase manager) and who has the group 'Product manager' assigned. Configuration might be done only by the group Administration / Settings
    The tool supports multiple click events. To open a product form - click on a image area, to select an item for mass update – click on any other area of this Kanban card
    # <a name='mass_actions'>Mass Actions List</a> 
    Mass actions are operations which might be proceeded for a number of products in batch. The tool offers multiple actions, among which you can select required ones. 
<ul style="font-size:18px;"> 
<li>Archive products in bulk</li>
<li>Restore selected products which have been previously archived</li>
<li>Change product category of all selected items</li>
<li>Add / remove an attribute value to all found templates</li>
<li>Export chosen items (the setting 'Export products' should be turned on)</li>
<li>Mass edit product type (consumable, service, storable)</li>
<li><i class='fa fa-globe'> </i> Publish or unpublish products in batch</li>
<li>Update products to be saleable / not saleable</li>
<li><i class='fa fa-shopping-cart'> </i> Update products to be purchasable / not purchasable</li>
<li><i class='fa fa-globe'> </i> Add / remove public E-shop categories of selected templates</li>
<li><i class='fa fa-globe'> </i> Add / remove products' alternatives</li>
<li><i class='fa fa-globe'> </i> Add / remove products' accessories</li>
<li><i class='fa fa-shopping-cart'> </i> Assign a new vendor to product templates in bulk and make this supplier the most prioritized</li>
<li><i class='fa fa-building'> </i> Add / remove logistic routes</li>
<li><i class='fa fa-money'> </i> Modify invoice policy ('Ordered quantities', 'Delivered quantities')</li>
<li>Duplicate a few product templates simultaneously</li>
<li><i class='fa fa-money'> </i> Add / remove customer taxes</li>
<li><i class='fa fa-money'> </i> Add / remove vendor taxes</li>
<li>Subscribe to / unsubscribe from products' discussions</li>
<li>Add / remove templates' followers</li>
<li>Add / remove optional products</li>
<li><i class='fa fa-shopping-cart'> </i> Update purchase method ('On ordered quantities', 'On received quantities')</li>
<li><i class='fa fa-building'> </i> Update tracking method</li>
<li><i class='fa fa-shopping-cart'> </i> Change price difference account</li>
<li><i class='fa fa-money'> </i> Change income account of products</li>
<li><i class='fa fa-money'> </i> Change expense account of templates</li>
<li><i class='fa fa-building'>  </i> Change inventory location</li>
<li><i class='fa fa-building'> </i> Change production location</li>
</ul>
<p style="font-size:18px;">Beside the list above you can also prepare your own mass actions. Look at the configuration tab.</p>
<div class="alert alert-warning"> <span style="font-size:18px"> <i class="fa fa-book"></i> Take into acount that update of high number of product templates (e.g. 1000) might take significant time. In such a case you should increase your Odoo configuration timeouts. Besides, some operations might be impossible in Odoo: for instance, creating of more than 1000 variants for a single template.</span> </div>
    Products by categories filtered by attributes and standard search for mass update
    Product templates to be found quickly
    Product management configuration
    Mass actions list for products
    Mass action example: update attribute values
    Mass action example: change internal category
    Place any template field to each kanban card
    E-commerce categories hierarchy in the navigation panel
    Product management: security group
    Mass action example: export
    Mass action example: edit optional products
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "92.0",
    "currency": "EUR",
}
# -*- coding: utf-8 -*-
{
    "name": "Smart Alerts",
    "version": "12.0.1.0.1",
    "category": "Productivity",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/smart-alerts-303",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "web"
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/view.xml",
        "views/smart_warning.xml",
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
    "summary": "The tool to draw users' attention to important document warnings and details",
    "description": """
    Smart alerts are used to advise and warn users who work with documents of certain types and kinds. The tool let you prepare an alarm for almost any use case and catch attention at the most suitable moment: when users work with a document form view. Despite of real simplicity to configure alerts, the app will become a powerful tool to caution and to communicate any message.

    Prepare alerts for any Odoo document type: sale orders, opportunities, contacts, pickings, so, <strong>any existing</strong> in your database. There might be an unlimited number of warnings for a record
    Choose which documents of this type should have alerts using the dynamic domain constructor. You can apply restrictions by any storable field. For example, make announcements only for quotations (not sale orders), warn of invoices with total between 500 and 1000, pay attention only for suppliers (not customers), and so on.
    Alerts are located above a form view to always meet the eye of any user who opens this document. Such warnings are updated each time a form is reloaded: when you open a record, when you save a document (including any button clicked), when you switch to a next record, etc. 
    There are 4 types of alert styles: danger (red), warning (yellow), info (blue), and success (green)
    Display alerts, if you want, only for pre-defined user groups. For instance, show a warning not for all sales people, but only for sales managers. Take into account, however, that any sales manager always has rights of sales user
    Alerts might be translated and, then, would be shown on a current user language
    The tool is compatible with multi companies: each branch has an own list of alerts
    The right to configure alerts belongs to the special user group – 'Other / Smart Alerts Admin'. You can assign any user to do that job, but make sure he/she has read rights for a target Odoo model
    Beside text warnings, you may use simple HTML tags like links, underlining, etc. Look at the tab 'Configuration'
    # <a name='use_cases'> Typical use cases</a>
    Smart alerts might be of use in any sphere. You decide criteria when a warning should be shown. Simply choose a document type, filter them by any storable data, and prepare a catchy warning text. Here are just a few examples: 
<ul>
<li><i>Sales orders:</i> to warn of the certain peculiarities of a sold product. E.g. that a product is not any more manufactured and can be sold only from existing stocks</li>
<li><i>Purchases:</i> to make announcement for accountants that invoices with total more than 5000 should be approved by a financial manager</li>
<li><i>Opportunities:</i> to attract attention to company policies in relation to a chosen customer, for example</li>
<li><i>Contacts:</i> to caution a user of entering or checking certain information</li>
<li><i>Manufacturing:</i> to remind users of relying upon new production technology while manufacturing a definite product</li>
</ul>
    List of smart alerts: the number is not limited!
    Smart alerts: example of invoices
    Smart alerts rule: example of invoices
    Assign a responsible user for smart alerts
    Smart alert rule: example of sale orders
    Smart alerts: example of sale orders
    Smart alert rule: example of opportunities
    Smart alerts: example of opportunities
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "44.0",
    "currency": "EUR",
}
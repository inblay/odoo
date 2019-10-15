# -*- coding: utf-8 -*-
{
    "name": "Security User Roles",
    "version": "12.0.1.0.1",
    "category": "Extra Tools",
    "author": "Odoo Tools",
    "website": "https://odootools.com/apps/12.0/security-user-roles-318",
    "license": "Other proprietary",
    "application": True,
    "installable": True,
    "auto_install": False,
    "depends": [
        "base"
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "views/res_users.xml",
        "views/security_role.xml"
    ],
    "qweb": [
        
    ],
    "js": [
        
    ],
    "demo": [
        
    ],
    "external_dependencies": {},
    "summary": "The tool to combine users in roles and to simplify security group assigning",
    "description": """
    As your Odoo database grows, either vertically or horizontally, you face an issue of how to manage users efficiently. Each new app installed and each employee hired become a headache for Odoo administrators. Which rights should have a sales manager? What checkbox have I again missed? This is the tool to forget about such questions. The app is to manage users from a role perspective not based on security rights. Simply to start, easy to maintain, safe to administrate.

    It is simple to start: the tool let you create roles based on existing users. To that end push the button 'Create role' on a user form view
    It saves time to administrate users: just select a role on a user form and save. All security groups will be automatically applied 
    It is comfortable in a changing environment: you do not have to open each form to update security groups. Modify only a role and all related users would immediately have proper rights
    The tool allows to configure as many roles for a single user as you need: it let fully reflect your organizational structure
    You are not obliged to assign a role for all users. For specific ones you might leave this field empty and select security groups manually
    Rights to configure user roles are the same as for configuring users
    Assign roles for users to automatically apply security rights
    Combine security groups in roles for repeated use
    Each user might have multiple roles
    Reflect your own organizational structure in user roles
""",
    "images": [
        "static/description/main.png"
    ],
    "price": "36.0",
    "currency": "EUR",
    "post_init_hook": "post_init_hook",
}
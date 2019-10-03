from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    back_background = fields.Char(
        "Company Backend Background",
        help="URL of an image that will be the background of the main screen "
        "of the backend. Allowed formats: jpg, jpge, png, gif, svg")

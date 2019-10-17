from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    supplier_number = fields.Char("Supplier's Number")

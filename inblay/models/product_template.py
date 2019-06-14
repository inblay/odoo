# coding: utf-8
# Copyright 2019 Vauxoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_code = fields.Char(
        'Internal Reference', compute='_compute_default_code',
        inverse='_set_default_code', required=False, store=True)

    @api.multi
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        default['default_code'] = default.get('default_code', '.')

        return super(ProductTemplate, self).copy(default=default)

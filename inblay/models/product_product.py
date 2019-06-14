# coding: utf-8
# Copyright 2019 Vauxoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    default_code = fields.Char(
        'Internal Reference', index=True, required=False)

    @api.model_create_multi
    def create(self, vals_list):
        product_template_obj = self.env['product.template']
        for val in vals_list:
            product_code = val.get('default_code')
            if not product_code:
                val['default_code'] = product_template_obj.browse(
                    val.get('product_tmpl_id')).default_code
        return super(ProductProduct, self.with_context(
            create_product_product=True)).create(vals_list)

    @api.multi
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        default['default_code'] = '.'

        return super(ProductProduct, self).copy(default=default)

# coding: utf-8
# Copyright 2019 Vauxoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.addons import decimal_precision as dp
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    default_code = fields.Char(
        'Internal Reference', compute='_compute_default_code',
        inverse='_set_default_code', required=False, store=True)

    sale_price_usd = fields.Float(
        'Sale Price in USD',
        digits=dp.get_precision('Product Price'),
        help="Sale price of the product in USD currency")

    @api.multi
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        if default is None:
            default = {}
        default['default_code'] = default.get('default_code', '.')

        return super(ProductTemplate, self).copy(default=default)

    @api.onchange('sale_price_usd')
    def _onchange_sale_price(self):
        usd_currency = self.env.ref('base.USD')
        company = self.env.user.company_id
        local_currency = company.currency_id
        pricelist = self.env.ref('product.list0')
        for product in self:
            local_currency_value = usd_currency._convert(
                product.sale_price_usd, local_currency, company,
                fields.Date.today())
            product.list_price = local_currency_value

            items = pricelist.item_ids.filtered(
                lambda r: r.compute_price == 'fixed'
                and r.product_tmpl_id == product)

            for item in items:
                item.fixed_price = product.sale_price_usd

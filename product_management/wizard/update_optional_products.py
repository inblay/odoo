# -*- coding: utf-8 -*-

from odoo import api, fields, models

class update_prm_optionalproducts(models.TransientModel):
    _name = "update.prm.optionalproducts"
    _inherit = "product.sample.wizard"
    _description = "Update optional products"

    optional_to_add_ids = fields.Many2many(
        "product.template",
        "product_template_add_prm_optionalproducts_rel_table",
        "product_template_id",
        "update_prm_optionalproducts_id",
        string="Add optional products",
    )
    optional_to_exclude_ids = fields.Many2many(
        "product.template",
        "product_template_exclude_prm_optionalproducts_rel_table",
        "product_template_id",
        "update_prm_optionalproducts_id",
        string="Remove optional products",
    )

    @api.multi
    def _update_products(self, product_ids):
        """
        The method to prepare new vals for public categories

        Args:
         * product_ids - product.template recordset

        Extra info:
         * Expected singleton
        """
        self.ensure_one()
        if self.optional_to_add_ids:
            to_add = []
            for categ in self.optional_to_add_ids.ids:
                to_add.append((4, categ))
            product_ids.write({"optional_product_ids": to_add,})
        if self.optional_to_exclude_ids:
            to_exclude = []
            for categ in self.optional_to_exclude_ids.ids:
                to_exclude.append((3, categ))
            product_ids.write({"optional_product_ids": to_exclude,})

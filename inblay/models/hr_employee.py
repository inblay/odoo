# coding: utf-8
# Copyright 2019 Vauxoo
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class HrChild(models.Model):

    _name = 'hr.child'
    _description = 'Hr Child'

    name = fields.Char()
    parent_id = fields.Many2one('hr.employee')


class HrEmployee(models.Model):

    _inherit = 'hr.employee'

    first_name = fields.Char()
    middle_name = fields.Char()
    first_last_name = fields.Char()
    second_last_name = fields.Char()
    significant_other = fields.Char()
    anniversary = fields.Date()
    children_ids = fields.One2many('hr.child', 'parent_id')
    pant_size = fields.Char()
    shirt_size = fields.Char()
    weight = fields.Char()
    imss_number = fields.Char()
    ine_number = fields.Char()

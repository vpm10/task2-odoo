from odoo import fields, models, api


class ProductsTree(models.Model):
    _name = 'product.tree'

    product_id = fields.Many2one('product.product')

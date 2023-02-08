from odoo import fields, models, api


class ProductSaleCount(models.Model):
    _inherit = 'product.template'

    sale_count = fields.Integer(compute='compute_sale_count')

    def compute_sale_count(self):
        self.sale_count = self.env['sale.order'].search_count([('order_line.product_template_id', '=', self.id), ('state', '=', 'sale')])

    @api.onchange('list_price')
    def change_price(self):
        records = self.env['sale.order.line'].search([('state', '=', 'draft')])
        for rec in records:
            rec.price_unit = self.list_price




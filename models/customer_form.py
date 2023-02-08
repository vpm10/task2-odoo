from odoo import fields, models, api


class CustomerForm(models.Model):
    _inherit = 'res.partner'

    customer_so_ids = fields.One2many('sale.order', 'partner_id',
                                      readonly=True)
    count_products = fields.Char(compute='customer_products', string='Total products')

    # def customer_sale_order(self):
    #     self.write({
    #         'customer_so_ids': [(5, 0)]
    #     })
    #     records = self.env['sale.order'].search([('partner_id.id', '=', self.id)])
    #     for record in records:
    #         self.write({
    #             'customer_so_ids': [(0, 0, {
    #                 'sale_order_id': record,
    #             }
    #             )]
    #         })

    def customer_products(self):
        records = self.customer_so_ids.order_line.product_template_id
        self.count_products = str(len(records)) + "    " + 'Products'
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'view_type': 'tree,form',
            'res_model': 'product.template',
            'domain': [('id', '=', [m.id for m in records])],

        }
        # print(records)
        # for rec in records:
        #     lists = []
        #     list = rec.order_line.product_template_id
        #     lists.append(list)
            # print(lists)
        # return records

        # for record in records:
        #     list = {
        #         ''
        #     }


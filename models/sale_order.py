from odoo import api, models, fields
import random
import json
from datetime import timezone
from pytz import timezone
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"
    test = fields.Char(default=random.randrange(1000), compute="_compute_test", store=True,  states={'draft': [('readonly', False)]})
    date_value = fields.Datetime(default=fields.Datetime.now)


    @api.onchange('tax_totals_json', 'date_order', 'date_value', 'order_line')
    def _compute_test(self):
        for record in self:
            if record.date_order != record.date_value or record.order_line:
                record.test = f"{'%.2f' % json.loads(record.tax_totals_json)['amount_total']} - {record.date_order.astimezone(timezone('Europe/Moscow')).strftime('%m/%d/%Y %H:%M:%S')}"

    @api.constrains('test')
    def _check_description(self):
        for record in self:
            if record.test:
                if len(record.test) >= 50:
                    raise ValidationError("Длина текста должна быть меньше 50 символов!")

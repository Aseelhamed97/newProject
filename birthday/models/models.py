# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleExtend(models.Model):
  _inherit = 'sale.order'

  reference_number = fields.Char('Reference Number')
  insurance_number = fields.Char('Insurance Number')
 
  @api.multi
  def _prepare_invoice(self):
        res = super(SaleExtend, self).prepare_invoice()
        res['reference_number'] = self.reference_number
        res['insurance_number'] = self.insurance_number
        return res

class InvoiceExtend(models.Model):
  _inherit = 'account.invoice'

  reference_number = fields.Char('Reference Number')
  insurance_number = fields.Char('Insurance Number')    
    

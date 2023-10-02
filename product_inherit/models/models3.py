# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
import requests
import json

class category_inherit(models.Model):
    _inherit = 'product.public.category'
    _description = 'category_inherit'

    @api.model_create_multi
    def create(self, vals):
       product = super(category_inherit, self).create(vals)
       URL = "https://depotsarl.com/ecomerce/odoo/api.php"
       PARAMS = {'action':'category_add','id':product.id}
       #raise UserError(_(product.id))
       requests.get(url = URL, params = PARAMS)         

       return product

    def write(self, vals):
        
        product = super(category_inherit, self).write(vals)
        URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        PARAMS = {'action':'category_edit','id':self.id}
        #raise UserError(_(self.id))
        requests.get(url = URL, params = PARAMS)
        return product

    def unlink(self):
        product = super(category_inherit, self).unlink()
        URL = "https://depotsarl.com/ecomerce/odoo/api.php"
        PARAMS = {'action':'category_delete','id':self.id}
        requests.get(url = URL, params = PARAMS)
        #raise UserError(_(self.id))
        return product

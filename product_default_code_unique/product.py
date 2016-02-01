# -*- coding: utf-8 -*-
# © 2016 Alessio Gerace - Agile Business Group
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp import models, api, _
from openerp.exceptions import Warning as UserError


class Product(models.Model):
    _inherit = 'product.product'

    @api.model
    @api.constrains('default_code')
    def _check_description(self):
        if self.default_code in self.search([]).mapped('default_code'):
            raise UserError(_("Internal Reference must be unique"))

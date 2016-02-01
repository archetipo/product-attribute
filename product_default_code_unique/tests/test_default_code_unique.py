# -*- coding: utf-8 -*-
# © 2016 Alessio Gerace - Agile Business Group
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestDefaultCodeUnique(TransactionCase):

    def setUp(self):
        super(TestDefaultCodeUnique, self).setUp()

        self.ProdModel = self.env['product.product']

    def test_1(self):
        self.product = self.ProdModel.create(
            {
                'name': 'test1',
                'default_code': 'test1'
            }
        )
        self.assertEqual(
            'test1',
            self.product.default_code
        )

    def test_2(self):
        with self.assertRaises(ValidationError):
            self.product = self.ProdModel.create(
                {
                    'name': 'test2',
                    'default_code': 'test1'
                }
            )

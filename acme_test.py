#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_stealability(self):
        """Test ability detect stealability"""
        # Test value 0.4
        prod = Product('Test Product', weight=1, price=0.4)
        self.assertEqual(prod.stealability(), "Not so stealable...")

        # Test value 0.5
        prod = Product('Test Product', weight=1, price=0.5)
        self.assertEqual(prod.stealability(), "Kinda stealable.")

        # Test value 1.0
        prod = Product('Test Product', weight=1, price=1.0)
        self.assertEqual(prod.stealability(), "Very stealable!")

        # Test value 1.1
        prod = Product('Test Product', weight=1, price=1.1)
        self.assertEqual(prod.stealability(), "Very stealable!")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        pass

    def test_legal_names(self):
        pass

if __name__ == '__main__':
    unittest.main()

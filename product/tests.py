from django.test import TestCase

from product.models import Product


# Create your tests here.
# create unit test for customer models
class ProductModelTestCase(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title="iphong", description="st job", active=True, product_tag=None
        )

    def test_customer_name(self):
        product = Product.objects.last()

        self.assertIsNone(self.product.id)
        self.assertIsNone(self.product.name)
        self.assertIsNone(self.product.description)
        self.assertTrue(self.product.active)
        self.assertEqual(self.product.id, product.id)
        self.assertEqual(self.product.title, product.title)
        self.assertEqual(self.product.description, product.description)

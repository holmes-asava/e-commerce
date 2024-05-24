from django.test import TestCase


# Create your tests here.
# create unit test for customer models
class CustomerModelTestCase(TestCase):

    def setUp(self):
        from django.contrib.auth.models import User

        from .models import Customer

        self.user = User.objects.create_user(
            username='johndoe',
        )
        # Create test data for Customer model
        self.customer = Customer.objects.create(
            user=self.user,
            first_name='first_name',
            last_name='last_name',
        )

    def test_customer_name(self):
        self.assertEqual(self.customer.first_name, 'first_name')

    def test_customer_email(self):
        self.assertEqual(self.customer.last_name, 'last_name')


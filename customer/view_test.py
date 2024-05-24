from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

from .models import Customer


class CustomerViewTest(TestCase):
    def setUp(self):
        pass

    def test_create_customer(self):
        # Define the data for the new customer
        data = {
            'first_name': 'Test',
            'last_name': 'Customer',
            'email': 'test@gmail.com',
            'password': 'testpassword'
            # Add other fields as necessary
        }

        # Call the customer creation API
        response = self.client.post(reverse('customer-list'), data, format='json')
        # Check that the response has a status code of 201 (created)
        self.assertEqual(response.status_code, 201)

        # Check that a customer was added to the database
        self.assertEqual(Customer.objects.count(), 1)

        # Check that the customer's name was correctly saved
        self.assertEqual(Customer.objects.first().name, 'Test Customer')

    def test_login(self):
        data = {'email': 'test@gmail.com', 'password': 'testpassword'}
        user = User.objects.create_user(email=data['email'],username=data['email'], password=data['password'])
        Token.objects.create(user=user)

        response = self.client.post(reverse('customer-login'), data, format='json')
        print(user.auth_token.key)
        print(response.json())
        # Check that the response has a status code of 201 (created)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['email'], data['email'])
        self.assertEqual(response.data['token'], user.auth_token.key)


from rest_framework.test import APITestCase
from rest_framework import status
from .models import txte

class txteAPITestCase(APITestCase):
    def setUp(self):
        self.txte = txte.objects.create(date='2024-01-01', customer_name='Test Customer')

    def txte_create_txte(self):
        data = {'date': '2024-01-02', 'customer_name': 'New Customer'}
        response = self.client.post('/api/txte/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(txte.objects.count(), 2)

    def test_get_txte_list(self):
        response = self.client.get('/api/txte/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_txte_detail(self):
        response = self.client.get(f'/api/txte/{self.txte.pk}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['customer_name'], 'Test Customer')

    # Add more test cases for update, delete, invoice details APIs, etc.


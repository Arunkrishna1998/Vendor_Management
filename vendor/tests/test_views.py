from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Vendors, PurchaseOrder, HistoricalPerformance
from ..serializers import VendorSerializer, PurchaseOrderSerializer
from ..views import TokenAPI, VendorCreateView, VenderManagementView, PurchaseOrderView, PurchaseManagementView, HistoricalPerformanceView

class TokenAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='admin123')
        self.client = APIClient()

    def test_token_generation(self):
        response = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin123'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

class VendorAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test123')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_vendor_creation(self):
        response = self.client.post('/api/vendors/', {'name': 'Vendor 1', 'contact_details': '9876543210', 'address': 'Address', 'vendor_code': 'V001'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendors.objects.count(), 1)

    def test_vendor_list(self):
        Vendors.objects.create(name='Vendor 1', contact_details='9876543210', address='Address', vendor_code='V001')
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

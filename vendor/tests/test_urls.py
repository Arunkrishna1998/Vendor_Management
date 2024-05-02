from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import TokenAPI, VendorCreateView, VenderManagementView, PurchaseOrderView, PurchaseManagementView, HistoricalPerformanceView

class TestUrls(SimpleTestCase):
    def test_token_url_resolves(self):
        url = reverse('token')
        self.assertEqual(resolve(url).func.__name__, TokenAPI.as_view().__name__)

    def test_vendor_create_url_resolves(self):
        url = reverse('vendors')
        self.assertEqual(resolve(url).func.__name__, VendorCreateView.as_view().__name__)


    def test_purchase_order_url_resolves(self):
        url = reverse('purchase_orders')
        self.assertEqual(resolve(url).func.__name__, PurchaseOrderView.as_view().__name__)

    
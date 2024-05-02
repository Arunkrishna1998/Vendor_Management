from django.test import TestCase
from ..models import Vendors, PurchaseOrder, HistoricalPerformance

class VendorsModelTestCase(TestCase):
    def test_vendor_creation(self):
        vendor = Vendors.objects.create(
            name='Test Vendor',
            contact_details='Test Contact Details',
            address='Test Address',
            vendor_code='TEST001'
        )
        self.assertEqual(Vendors.objects.count(), 1)
        self.assertEqual(vendor.name, 'Test Vendor')
        self.assertEqual(vendor.contact_details, 'Test Contact Details')
        self.assertEqual(vendor.address, 'Test Address')
        self.assertEqual(vendor.vendor_code, 'TEST001')

class PurchaseOrderModelTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendors.objects.create(
            name='Test Vendor',
            contact_details='Test Contact Details',
            address='Test Address',
            vendor_code='TEST001'
        )

    def test_purchase_order_creation(self):
        purchase_order = PurchaseOrder.objects.create(
            po_number='PO001',
            vendor=self.vendor,
            delivery_date='2024-05-01',
            items='[{"name": "Item1", "price": 100}, {"name": "Item2", "price": 200}]',
            quantity=5,
            status='pending'
        )
        self.assertEqual(PurchaseOrder.objects.count(), 1)
        self.assertEqual(purchase_order.po_number, 'PO001')
        self.assertEqual(purchase_order.vendor, self.vendor)
        self.assertEqual(purchase_order.quantity, 5)
        self.assertEqual(purchase_order.status, 'pending')

class HistoricalPerformanceModelTestCase(TestCase):
    def setUp(self):
        self.vendor = Vendors.objects.create(
            name='Test Vendor',
            contact_details='Test Contact Details',
            address='Test Address',
            vendor_code='TEST001'
        )

    def test_historical_performance_creation(self):
        historical_performance = HistoricalPerformance.objects.create(
            vendor=self.vendor,
            date='2024-05-01',
            on_time_delivery_rate=90.5,
            quality_rating_avg=4.5,
            average_response_time=10.2,
            fulfillment_rate=95.2
        )
        self.assertEqual(HistoricalPerformance.objects.count(), 1)
        self.assertEqual(historical_performance.vendor, self.vendor)
        self.assertEqual(historical_performance.date, '2024-05-01')
        self.assertEqual(historical_performance.on_time_delivery_rate, 90.5)
        self.assertEqual(historical_performance.quality_rating_avg, 4.5)
        self.assertEqual(historical_performance.average_response_time, 10.2)
        self.assertEqual(historical_performance.fulfillment_rate, 95.2)

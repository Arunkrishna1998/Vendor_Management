from datetime import timedelta
from .models import PurchaseOrder, HistoricalPerformance
from django.db.models import F, Avg

def calculate_on_time_delivery_rate(vendor_id):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor_id, status='completed')
    on_time_deliveries = completed_orders.filter(delivery_date__lte=F('acknowledgment_date'))
    total_completed_orders = completed_orders.count()
    if total_completed_orders > 0:
        on_time_delivery_rate = (on_time_deliveries.count() / total_completed_orders) * 100
    else:
        on_time_delivery_rate = 0
    return on_time_delivery_rate

def calculate_quality_rating_avg(vendor_id):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor_id, status='completed').exclude(quality_rating__isnull=True)
    if completed_orders.exists():
        quality_rating_avg = completed_orders.aggregate(avg_quality_rating=Avg('quality_rating'))['avg_quality_rating']
    else:
        quality_rating_avg = 0
    return quality_rating_avg

def calculate_response_time(vendor_id):
    acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor_id, acknowledgment_date__isnull=False)
    if acknowledged_orders.exists():
        total_response_time = sum((order.acknowledgment_date - order.issue_date).total_seconds() for order in acknowledged_orders)
        average_response_time = total_response_time / acknowledged_orders.count()
    else:
        average_response_time = 0
    return average_response_time

def calculate_fulfillment_rate(vendor_id):
    total_orders = PurchaseOrder.objects.filter(vendor=vendor_id)
    successful_orders = total_orders.filter(status='completed', issue_date__lte=F('acknowledgment_date'))
    if total_orders.exists():
        fulfillment_rate = (successful_orders.count() / total_orders.count()) * 100
    else:
        fulfillment_rate = 0
    return fulfillment_rate

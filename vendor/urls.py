from django.urls import path
from .views import (VendorCreateView, VenderManagementView, TokenAPI,
                    PurchaseOrderView, PurchaseManagementView, HistoricalPerformanceView)


urlpatterns = [
    path('token/', TokenAPI.as_view(), name="token"),
    path('vendors/', VendorCreateView.as_view(), name="vendors"),
    path('vendors/<int:pk>/', VenderManagementView.as_view()),
    path('purchase_orders/', PurchaseOrderView.as_view(), name="purchase_orders"),
    path('purchase_orders/<int:pk>/', PurchaseManagementView.as_view()),
    path('vendors/<int:vendor_id>/performance', HistoricalPerformanceView.as_view()),

]

from django.contrib import admin
from .models import Vendors, PurchaseOrder, HistoricalPerformance


admin.site.register(Vendors)
admin.site.register(PurchaseOrder)
admin.site.register(HistoricalPerformance)
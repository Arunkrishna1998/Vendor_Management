from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Vendors, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from .utils import (calculate_on_time_delivery_rate, calculate_quality_rating_avg,
                    calculate_response_time, calculate_fulfillment_rate)
from django.utils import timezone



class TokenAPI(APIView):
    """
    To generate token,
    use login credentials of superuser to generate token
    """
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)



class VendorCreateView(APIView):
    """
    Create Vendors,
    Get Vendor List
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = VendorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        vendor_list = Vendors.objects.all()
        serializer = VendorSerializer(vendor_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class VenderManagementView(generics.RetrieveUpdateDestroyAPIView):
    # To Fetch, Update,  delete Vendor details
    permission_classes = [IsAuthenticated]

    queryset = Vendors.objects.all()
    serializer_class = VendorSerializer



class PurchaseOrderView(APIView):
    """
    Create Purchase,
    Get Purchase List
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = PurchaseOrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        vendor_list = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(vendor_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



class PurchaseManagementView(generics.RetrieveUpdateDestroyAPIView):
    # To Fetch, Update,  delete Purchase Order details
    permission_classes = [IsAuthenticated]

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer



class HistoricalPerformanceView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, vendor_id):
        # Calculate performance metrics
        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor_id)
        quality_rating_avg = calculate_quality_rating_avg(vendor_id)
        average_response_time = calculate_response_time(vendor_id)
        fulfillment_rate = calculate_fulfillment_rate(vendor_id)

        # Create or update historical performance record
        historical_performance, created = HistoricalPerformance.objects.update_or_create(
            vendor_id=vendor_id,
            date=timezone.now().date(),
            defaults={
                'on_time_delivery_rate': on_time_delivery_rate,
                'quality_rating_avg': quality_rating_avg,
                'average_response_time': average_response_time,
                'fulfillment_rate': fulfillment_rate
            }
        )

       
        response_data = {
            "message": "Historical performance record created successfully." if created else "Historical performance record updated successfully.",
            "performance": {
                "on_time_delivery_rate": on_time_delivery_rate,
                "quality_rating_avg": quality_rating_avg,
                "average_response_time": average_response_time,
                "fulfillment_rate": fulfillment_rate
            }
        }

        return Response(response_data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
    
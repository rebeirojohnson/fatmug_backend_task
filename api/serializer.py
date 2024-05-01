from rest_framework import serializers
from . import models


class VendorSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['vendor_code','name','contact_details','address']
        read_only_fields = ['vendor_code']          

class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']
   

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['vendor_code','name',]
        read_only_fields = ['vendor_code']  
        
class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrder
        fields = '__all__'
        read_only_fields = ['vendor_code']           

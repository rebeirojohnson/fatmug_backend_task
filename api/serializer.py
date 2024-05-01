from rest_framework import serializers
from . import models


class VendorSerializerList(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['vendor_code','name']
        read_only_fields = ['vendor_code']          


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = '__all__'
        read_only_fields = ['vendor_code']          

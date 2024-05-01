from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializer
# Create your views here.
from rest_framework import status

@api_view(['GET','POST'])
def VendorViews(request):
    try:
        
        if request.method == 'GET':
            vendors = models.Vendor.objects.all()
            
            serializer_obj = serializer.VendorSerializerList(vendors, many=True)
                                        
            return Response(serializer_obj.data)

        elif request.method == 'POST':
            
            serializer_obj = serializer.VendorSerializer(data=request.data)
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status=201)
            else:
                return Response(serializer_obj.errors, status=400)
        
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send)
    

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def VendorDetailViews(request,vendor_code):
    try:
        try:
            vendor = models.Vendor.objects.get(pk=vendor_code)
        except Exception as e:
            raise Exception("No Vendors Found")
        
        if request.method == 'GET':
            
            if not vendor_code:
                return Response({"error": "vendor_code parameter is required in the request"}, status=status.HTTP_400_BAD_REQUEST)
            
            
            serializer_obj = serializer.VendorSerializer(vendor, many=False)
                                        
            return Response(serializer_obj.data)

        elif request.method in ['POST','PUT','PATCH']:
            
            serializer_obj = serializer.VendorSerializer(vendor, data=request.data, partial=request.method == 'PATCH')
            
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status=status.HTTP_200_OK)
            
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE':
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send)


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def VendorPerformanceViews(request,vendor_code):
    try:
        try:
            vendor = models.Vendor.objects.get(pk=vendor_code)
        except Exception as e:
            raise Exception("No Vendors Found")
        
        if request.method == 'GET':
            
            if not vendor_code:
                return Response({"error": "vendor_code parameter is required in the request"}, status=status.HTTP_400_BAD_REQUEST)
            
            
            serializer_obj = serializer.VendorPerformanceSerializer(vendor, many=False)
                                        
            return Response(serializer_obj.data)

        elif request.method in ['POST','PUT','PATCH']:
            
            serializer_obj = serializer.VendorPerformanceSerializer(vendor, data=request.data, partial=request.method == 'PATCH')
            
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status=status.HTTP_200_OK)
            
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE':
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send)
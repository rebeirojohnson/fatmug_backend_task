from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializer
# Create your views here.

@api_view(['GET','POST'])
def VendorViews(request):
    try:
        
        if request.method == 'GET':
            vendors = models.Vendor.objects.all()
            
            serializer_obj = serializer.VendorSerializer(vendors, many=True)
                                        
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
    
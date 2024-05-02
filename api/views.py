import datetime
from django.shortcuts import render
import pytz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializer
# Create your views here.
from rest_framework import status
from . import dbcon

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
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

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
                return Response(serializer_obj.data, status=status.HTTP_202_ACCEPTED)
            
            return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE':
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
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

            
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
@api_view(['GET','POST'])
def PurchaseOrderViews(request):
    try:
        
        if request.method == 'GET':
            vendor_name = request.GET.get('vendor_name')  # Assuming you are passing the vendor name as a query parameter

            if vendor_name:
                orders = models.PurchaseOrder.objects.filter(vendor_id=vendor_name)
            else:
                orders = models.PurchaseOrder.objects.all()
            
            serializer_obj = serializer.PurchaseOrderSerializer(orders, many=True)
                                        
            return Response(serializer_obj.data)

        elif request.method == 'POST':
            
            vendor_id = request.data.get("vendor")
            
            is_product_delivered_on_time = False
            
            if request.data.get('delivery_date') is not None:
                delivery_date = datetime.datetime.strptime(request.data.get('delivery_date'),"%Y-%m-%dT%H:%M:%SZ")
                
               
                
                if request.data.get('status') == 'completed' and delivery_date >= datetime.datetime.now():
                    is_product_delivered_on_time = True
        
                    
            request.data['is_product_delivered_on_time'] = is_product_delivered_on_time
            
            print(request.data)
            
            serializer_obj = serializer.PurchaseOrderSerializer(data=request.data)
            
            if serializer_obj.is_valid():
                
                serializer_obj.save()
                
                
                print(vendor_id)
                
                query_to_find_average_quality = f"""select * from django_data.update_vendor_performance('{vendor_id}') """
                
                dbcon.excute_query(query=query_to_find_average_quality)
                
                return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def PurchaseOrderAcknoledgeView(request,po_id):
    try:
        # Fetch the PurchaseOrder instance from the database based on its primary key (po_number)
        purchase_order = models.PurchaseOrder.objects.get(po_number=po_id)
        
        
        # Update the acknowledgment_date field to the current datetime
        purchase_order.acknowledgment_date = datetime.datetime.now(tz=pytz.timezone(zone='Asia/Kolkata'))
        
        # Save the updated instance back to the database
        purchase_order.save()
        
        vendor_id = purchase_order.vendor

        query_to_find_average_quality = f"""select * from django_data.update_vendor_performance('{vendor_id}') """
                
        dbcon.excute_query(query=query_to_find_average_quality)
        
        # Return success response
        return Response({"message": "Acknowledgment date updated successfully"}, status=status.HTTP_200_OK)
    
    except models.PurchaseOrder.DoesNotExist:
        # Handle case where PurchaseOrder instance is not found
        return Response({"error": "PurchaseOrder instance not found"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

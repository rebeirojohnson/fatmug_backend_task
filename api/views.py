import datetime
from django.shortcuts import render
import pytz
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models,serializer
# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import dbcon
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings

@api_view(['POST'])
def LoginView(request):
    print(request.data)
    serializer_obj = serializer.LoginSerializer(data=request.data)
    if serializer_obj.is_valid():
        username = serializer_obj.validated_data['username']
        password = serializer_obj.validated_data['password']
        user = authenticate(username=username, password=password)
        if user:
            request.session['username'] = username
            request.session['is_authenticated'] = True
            request.session.save()
          
            return Response({'message': 'Login Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer_obj.errors, status=400)

@api_view(['GET','POST'])
def VendorViews(request):

    """This View is to handle the vendor retrival and creation

    Returns:
        GET : Return The list of all Vendors 
        POST : Createa new Vendor 
    """
    
    try:
        
        if request.method == 'GET':
            
            vendors = models.Vendor.objects.all()
            
            serializer_obj = serializer.VendorSerializerList(vendors, many=True)
                                        
            return Response(serializer_obj.data)

        elif request.method == 'POST':
            
            serializer_obj = serializer.VendorSerializerList(data=request.data)
            
            if serializer_obj.is_valid():
                serializer_obj.save()
                return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def VendorDetailViews(request,vendor_code):
    """This View is to handle retrival, creation, updation and deletion of a particular vendor by specifying the vendor details

    Returns:
        GET : Return The Detail of a Vendor 
        PUT,PATCH : Updates the details of a vendor
        Delete : Removes a vendor from the database
    """
    
    try:
        try:
            vendor = models.Vendor.objects.get(pk=vendor_code)
        except Exception as e:
            raise Exception("No Vendors Found")
        
        if request.method == 'GET':
            
            if not vendor_code:
                return Response({"error": "vendor_code parameter is required in the request"}, status=status.HTTP_400_BAD_REQUEST)
            
            serializer_obj = serializer.VendorSerializerList(vendor, many=False)
                                        
            return Response(serializer_obj.data,status=status.HTTP_200_OK)

        elif request.method in ['POST','PUT','PATCH']:
            
            serializer_obj = serializer.VendorSerializerList(vendor, data=request.data, partial=request.method == 'PATCH')
            
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
    """This View is to returns the performance metrics of a vendor Such as
        On-Time Delivery Rate
        Quality Rating Average
        Average Response Time
        Fulfilment Rate
        
    Returns:
        GET : Return The Performance of a Vendor.
    """
    try:
        try:
            vendor = models.Vendor.objects.get(pk=vendor_code)
        except Exception as e:
            raise Exception("No Vendors Found")
        
        if request.method == 'GET':
            
            if not vendor_code:
                return Response({"error": "vendor_code parameter is required in the request"}, status=status.HTTP_400_BAD_REQUEST)
                        
            serializer_obj = serializer.VendorPerformanceSerializer(vendor, many=False)
                                        
            return Response(serializer_obj.data,status=status.HTTP_200_OK)

            
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET','POST'])
def PurchaseOrderListViews(request):
    """This View is to handle the purchase order retrival and creation

    Parameter : vendor_name (Optional) Filter the orders for a particular vendor
    
    Returns:
        GET : Return The list of all purchase order 
        POST : Createa new purchase order  
    """
    try:
        
        if request.method == 'GET':
            vendor_name = request.GET.get('vendor_name')  # Assuming you are passing the vendor name as a query parameter

            if vendor_name:
                orders = models.PurchaseOrder.objects.filter(vendor_id=vendor_name)
            else:
                orders = models.PurchaseOrder.objects.all()
            
            serializer_obj = serializer.PurchaseOrderListSerializer(orders, many=True)
                                        
            return Response(serializer_obj.data,status=status.HTTP_200_OK)

        elif request.method == 'POST':
            
            vendor_id = request.data.get("vendor")
            
            is_product_delivered_on_time = False
            
            if request.data.get('delivery_date') is not None:
                delivery_date = datetime.datetime.strptime(request.data.get('delivery_date'),"%Y-%m-%dT%H:%M:%SZ")
                
                if request.data.get('status') == 'completed' and delivery_date >= datetime.datetime.now():
                    is_product_delivered_on_time = True
        
                    
            request.data['is_product_delivered_on_time'] = is_product_delivered_on_time
            
            serializer_obj = serializer.PurchaseOrderSerializer(data=request.data)
            
            if serializer_obj.is_valid():
                
                serializer_obj.save()
                
                dbcon.update_vendor_perfomance_by_vendor_id(vendor_id=vendor_id)
                
                return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET','POST','PATCH','PUT','DELETE'])
def PurchaseOrderDetailViews(request,po_id):
    """This View is to handle the  retrival, modification and delete purchase order

    Returns:
        GET : Return The detail of a purchase order 
        PUT,PATCH : Updates a purchase order  details. Patch - Partial Update
        DELETE : Deletes a purchase order  details.
    """
    
    try:
        
        order = models.PurchaseOrder.objects.get(pk=po_id)
        
        
        if request.method == 'GET':
            
            serializer_obj = serializer.PurchaseOrderSerializer(order, many=False)
                                        
            return Response(serializer_obj.data)

        elif request.method in ['POST','PUT','PATCH']:
                        
            is_product_delivered_on_time = False
            
            if request.data.get('delivery_date') is not None:
                delivery_date = datetime.datetime.strptime(request.data.get('delivery_date'),"%Y-%m-%dT%H:%M:%S%z")
                
                if request.data.get('status','pending').lower() == 'completed' and delivery_date >= datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE)):
                    is_product_delivered_on_time = True
           
            request.data['is_product_delivered_on_time'] = is_product_delivered_on_time
            
            serializer_obj = serializer.PurchaseOrderSerializer(order, data=request.data, partial=request.method == 'PATCH')
            
            if serializer_obj.is_valid():
                
                serializer_obj.save()
                
                print(order)
                dbcon.update_vendor_perfomance_by_vendor_id(vendor_id=order.vendor.vendor_code)
                
                return Response(serializer_obj.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer_obj.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            order.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def PurchaseOrderAcknoledgeView(request,po_id):
    """This View is to handle the  retrival, modification and delete purchase order.
    Updates the acknowledge time to the current time.

    Returns:
        POST : Used to acknowledge the purchase order using the purchase order number
         
    """
    try:
        purchase_order = models.PurchaseOrder.objects.get(po_number=po_id)
        
        purchase_order.acknowledgment_date = datetime.datetime.now(tz=pytz.timezone(zone='Asia/Kolkata'))
        
        purchase_order.save()
        
        vendor_id = purchase_order.vendor

        query_to_find_average_quality = f"""select * from django_data.update_vendor_performance('{vendor_id}') """
                
        dbcon.excute_query(query=query_to_find_average_quality)
        
        return Response({"message": "Acknowledgment date updated successfully"}, status=status.HTTP_200_OK)
    
    except models.PurchaseOrder.DoesNotExist:
        return Response({"error": "PurchaseOrder instance not found"}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send,status=status.HTTP_500_INTERNAL_SERVER_ERROR)

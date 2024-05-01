from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def index_view(request):
    try:
        
        data_to_send = {"message":"Success"}
        return Response(data_to_send)
    except Exception as e:
        data_to_send = {"message":"Something Went Wrong","error":str(e)}
        return Response(data_to_send)
    
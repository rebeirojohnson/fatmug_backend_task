from django.urls import path
from . import views 

urlpatterns = [
	path('', views.VendorViews, name="base"),
 
	path('vendors/', views.VendorViews, name="VendorViews"),
	path('vendors/<str:vendor_code>/', views.VendorDetailViews, name="VendorDetailViews"),
 
	path('vendors/<str:vendor_code>/performance/', views.VendorPerformanceViews, name="VendorDetailViews"),
 
	path('purchase_orders/', views.PurchaseOrderViews, name="PurchaseOrderViews"),
	path('purchase_orders/<str:po_id/', views.PurchaseOrderViews, name="PurchaseOrderViews"),
]
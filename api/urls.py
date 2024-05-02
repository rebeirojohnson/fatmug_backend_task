from django.urls import path
from . import views 

urlpatterns = [
    
	
	path('login/', views.LoginView, name="VendorViews"),
 
	path('vendors/', views.VendorViews, name="VendorViews"),
	path('vendors/<str:vendor_code>/', views.VendorDetailViews, name="VendorDetailViews"),
 
	path('vendors/<str:vendor_code>/performance/', views.VendorPerformanceViews, name="VendorDetailViews"),
 
	path('purchase_orders/', views.PurchaseOrderListViews, name="PurchaseOrderViews"),
	path('purchase_orders/<str:po_id>/', views.PurchaseOrderDetailViews, name="PurchaseOrderViews"),
 
	path('purchase_orders/<str:po_id>/acknowledge/', views.PurchaseOrderAcknoledgeView, name="PurchaseOrderViews"),
]
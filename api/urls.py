from django.urls import path
from . import views 

urlpatterns = [
	path('', views.VendorViews, name="base"),
	path('vendors/', views.VendorViews, name="base"),
	# path('vendors/<str:vendor_code>/', views.index_view, name="base"),
	# path('purchase_orders/', views.index_view, name="base"),
	# path('purchase_orders /<str:po_id>/', views.index_view, name="base"),
	# path('', views.index_view, name="base"),
	# path('', views.index_view, name="base"),
]
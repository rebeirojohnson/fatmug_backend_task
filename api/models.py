from django.db import models

# Create your models here.

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=100,unique=True,auto_created=True,primary_key=True)
    name = models.CharField(max_length=100)
    contact_details = models.TextField(null=True)
    address = models.TextField(null=True)
    on_time_delivery_rate = models.FloatField(null=True)
    quality_rating_avg = models.FloatField(null=True)
    average_response_time = models.FloatField(null=True)
    fulfillment_rate = models.FloatField(null=True)

    def __str__(self):
        return self.name


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=200,primary_key=True,auto_created=True,unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField()

    def __str__(self):
        return self.title

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


    def __str__(self):
        return self.title
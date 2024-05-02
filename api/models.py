import uuid
from django.db import models
import random
import random
import string

# Create your models here.

def generate_vendor_code(vendor_name):
    return vendor_name

class Vendor(models.Model):
    vendor_code = models.CharField(max_length=100,unique=True,primary_key=True)
    name = models.CharField(max_length=100)
    contact_details = models.TextField(null=True)
    address = models.TextField(null=True)
    on_time_delivery_rate = models.FloatField(null=True,default=0)
    quality_rating_avg = models.FloatField(null=True,default=0)
    average_response_time = models.FloatField(null=True,default=0)
    fulfillment_rate = models.FloatField(null=True,default=0)
    
    def generate_vendor_code(self):
        vendor_code = ''
        for each_word in self.name.split(" "):
            vendor_code += each_word[0]
            
        vendor_code += ''.join(random.choices(string.ascii_letters, k=3)).upper()
        return vendor_code

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            self.vendor_code = self.generate_vendor_code()
            
        super().save(*args, **kwargs)
        

    def __str__(self):
        return self.vendor_code


class PurchaseOrder(models.Model):
    po_number = models.UUIDField(default=uuid.uuid4, editable=False,primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField()
    issue_date = models.DateTimeField(auto_now=True)
    acknowledgment_date = models.DateTimeField(null=True)
    is_product_delivered_on_time = models.BooleanField()

        
    # def __str__(self):
    #     return (self.po_number)

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


    def __str__(self):
        return self.title
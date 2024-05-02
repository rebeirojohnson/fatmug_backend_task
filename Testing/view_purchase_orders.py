import json
import requests

def view_purchase_orders(vendor_code=None):
    
    if vendor_code:
        url = "http://127.0.0.1:8000/api/purchase_orders/?vendor_code={vendor_code}"
    else:
        url = "http://127.0.0.1:8000/api/purchase_orders/"
    
    list_of_vendors = requests.get(url=url).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    vendor_code = 'NSLZO' 
    
    vendor_code = None
    
    view_purchase_orders(vendor_code = vendor_code)
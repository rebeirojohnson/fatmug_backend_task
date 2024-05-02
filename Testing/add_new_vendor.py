import json
import requests

def add_new_vendor(vendor_name:str,contact_details:str,address:str):
    
    if vendor_name == '':
        raise Exception('Provide a Valid vendor name')
    
    if contact_details == '':
        contact_details = None
    
    if address == '':
        address = None  
        
    url = "http://127.0.0.1:8000/api/vendors/"
    
    payload = {
        "name": vendor_name,
        "contact_details": contact_details,
        "address": address
    }
    
    list_of_vendors = requests.post(url=url,json=payload).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    vendor_name = 'Tapei Solutiions'
    
    contact_details = '7899404714'
    
    address = 'India'
    
    add_new_vendor(vendor_name=vendor_name,contact_details=contact_details,address=address)
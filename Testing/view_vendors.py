import json
import requests

def address(vendor_name:str,contact_details:str,address:str):
    
    url = "http://127.0.0.1:8000/api/vendors/"
    
    payload = {
        "name": vendor_name,
        "contact_details": contact_details,
        "address": address
    }
    
    list_of_vendors = requests.get(url=url,json=payload).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    view_all_vendors()
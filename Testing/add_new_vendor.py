import json
import requests
from login import get_session_id_from_local_file
import os

server_ip = os.getenv('SERVER_IP','127.0.0.1:8000')

def add_new_vendor(vendor_name:str,contact_details:str,address:str):
    
    session_id = get_session_id_from_local_file()
    
    cookies = {
        "sessionid":session_id
    }
    
    if vendor_name == '':
        raise Exception('Provide a Valid vendor name')
    
    if contact_details == '':
        contact_details = None
    
    if address == '':
        address = None  
        
    url = f"http://{server_ip}/api/vendors/"
    
    payload = {
        "name": vendor_name,
        "contact_details": contact_details,
        "address": address
    }
    
    response = requests.post(url=url,json=payload,cookies=cookies)
    
    list_of_vendors = response.json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    vendor_name = 'Tapei New Solutiions'
    
    contact_details = '7899404714'
    
    address = 'India'
    
    add_new_vendor(vendor_name=vendor_name,contact_details=contact_details,address=address)
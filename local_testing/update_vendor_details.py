import json
import requests
from login import get_session_id_from_local_file
import os

server_ip = os.getenv('SERVER_IdP','127.0.0.1:8000')

def view_vendor_details(vendor_code,new_vendor_name,new_vendor_address,new_vendor_contact):
    
    if new_vendor_name == '':
        raise Exception("Vendor name is not valid")
    
    if new_vendor_address == '':
        new_vendor_address = None
    
    if new_vendor_contact == '':
        new_vendor_contact = None
        
    session_id = get_session_id_from_local_file()
    
    payload = {
        "name": new_vendor_name,
        "contact_details": new_vendor_address,
        "address": new_vendor_contact
    }
    
    print(json.dumps(payload,indent=4))
     
    cookies = {
        "sessionid":session_id
    }
    
    url = f"http://{server_ip}/api/vendors/{vendor_code}/"

    list_of_vendors = requests.post(url=url,cookies=cookies,json=payload).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    vendor_code = 'NVFCH'
    
    new_vendor_name = 'New Tech Name'
    
    new_vendor_address = 'New Address'
    
    new_vendor_contact = '777777'
    
    view_vendor_details(vendor_code=vendor_code,new_vendor_name=new_vendor_name,new_vendor_address=new_vendor_address,new_vendor_contact=new_vendor_contact)
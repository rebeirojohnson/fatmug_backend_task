import json
import requests
from login import get_session_id_from_local_file
import os

server_ip = os.getenv('SERVER_IP','127.0.0.1:8000')

def delete_vendor_by_vendor_code(vendor_code):
    session_id = get_session_id_from_local_file()
    
    cookies = {
        "sessionid":session_id
    }
    
    url = f"http://{server_ip}/api/vendors/{vendor_code}/"

    response = requests.delete(url=url,cookies=cookies)
    
    if response.status_code == 204:
        print(f"Vendor Deleted Successfully")
    
if __name__ == '__main__':
    
    vendor_code = 'TNSXXI'
    
    delete_vendor_by_vendor_code(vendor_code)
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

    list_of_vendors = requests.delete(url=url,cookies=cookies).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    vendor_code = 'NVOOV'
    
    delete_vendor_by_vendor_code(vendor_code)
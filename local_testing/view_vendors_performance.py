import json
import requests
from login import get_session_id_from_local_file
import os

server_ip = os.getenv('SERVER_IP','127.0.0.1:8000')

def view_vendor_performance(vendor_code):
    session_id = get_session_id_from_local_file()
    
    cookies = {
        "sessionid":session_id
    }
    
    url = f"http://{server_ip}/api/vendors/{vendor_code}/performance/"

    list_of_vendors = requests.get(url=url,cookies=cookies).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    vendor_code = 'NVOOV'
    
    view_vendor_performance(vendor_code)
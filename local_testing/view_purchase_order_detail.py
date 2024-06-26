import json
import requests
from login import get_session_id_from_local_file
import os

server_ip = os.getenv('SERVER_IP','127.0.0.1:8000')

def view_purchase_orders(po_number=None):
    session_id = get_session_id_from_local_file()
    
    if po_number == '':
        raise Exception("Provide valid Purchase order Number")
    cookies = {
        "sessionid":session_id
    }
    
    url = f"http://{server_ip}/api/purchase_orders/{po_number}/"
  
    list_of_vendors = requests.get(url=url,cookies=cookies).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    po_number = 'f1e0f118-1714-45e5-876b-11b549060922' 

    view_purchase_orders(po_number= po_number)
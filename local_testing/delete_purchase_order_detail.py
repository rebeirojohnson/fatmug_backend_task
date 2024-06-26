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
  
    response = requests.delete(url=url,cookies=cookies)
    
    if response.status_code == 204:
        
        print("Product Order Deleted Successfully")
    else:
        print(response.content)
        
if __name__ == '__main__':
    
    po_number = '150750f9-d369-4de9-a030-fccbd30eb3c7' 

    view_purchase_orders(po_number= po_number)
import json
import requests
from login import get_session_id_from_local_file

def acknowledge_order_by_order_id(order_id):
    session_id = get_session_id_from_local_file()
    
    cookies = {
        "sessionid":session_id
    }

    url = f"http://127.0.0.1:8000/api/purchase_orders/{order_id}/acknowledge/"

    
    list_of_vendors = requests.post(url=url,cookies=cookies).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    order_id = 'f1e0f118-1714-45e5-876b-11b549060922' 
    
    acknowledge_order_by_order_id(order_id = order_id)
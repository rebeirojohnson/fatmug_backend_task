import json
import requests
from login import get_session_id_from_local_file

def view_purchase_orders(vendor_code=None):
    session_id = get_session_id_from_local_file()
    
    cookies = {
        "sessionid":session_id
    }
    
    if vendor_code:
        url = "http://127.0.0.1:8000/api/purchase_orders/?vendor_code={vendor_code}"
    else:
        url = "http://127.0.0.1:8000/api/purchase_orders/"
    
    list_of_vendors = requests.get(url=url,cookies=cookies).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    vendor_code = 'NSLZO' 
    
    vendor_code = None
    
    view_purchase_orders(vendor_code = vendor_code)
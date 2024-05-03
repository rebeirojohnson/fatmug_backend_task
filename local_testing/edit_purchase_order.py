import json
import requests
from login import get_session_id_from_local_file
import os

server_ip = os.getenv('SERVER_IdP','127.0.0.1:8000')

def create_new_purchase_order(po_number,vendor_code,order_date,delivery_date,items=[],status='pending',rating=0):
    
    if po_number == '' or vendor_code == '':
        raise Exception("Vendor Code is not valid")
    
    if delivery_date == '':
        delivery_date = None
    
        
    session_id = get_session_id_from_local_file()
    
    payload =  {
        "order_date": order_date,
        "delivery_date": delivery_date,
        "items": items,
        "quantity": len(items),
        "status": status,
        "quality_rating": rating,
        "vendor": vendor_code
    }
    
    print(json.dumps(payload,indent=4))
     
    cookies = {
        "sessionid":session_id
    }
    
    url = f"http://{server_ip}/api/purchase_orders/{po_number}"

    list_of_vendors = requests.patch(url=url,cookies=cookies,json=payload).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    po_number = '258a9267-b337-458f-99d6-dbc3fcd77fdd'
    
    vendor_code = 'NVFCH'
    
    order_date = '2025-01-01T00:00:00Z'
    
    delivery_date = '2025-02-01T00:00:00Z'
    
    items = []
    
    status = 'completed'
    
    rating = 8.5
    
    create_new_purchase_order(po_number=po_number,vendor_code=vendor_code,order_date=order_date,delivery_date=delivery_date,items=items,status=status,rating=rating)
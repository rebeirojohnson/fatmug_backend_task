import json
import requests

def acknowledge_order_by_order_id(order_id):
    

    url = f"http://127.0.0.1:8000/api/purchase_orders/{order_id}/acknowledge/"

    
    list_of_vendors = requests.post(url=url).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    order_id = 'f1e0f118-1714-45e5-876b-11b549060922' 
    
    acknowledge_order_by_order_id(order_id = order_id)
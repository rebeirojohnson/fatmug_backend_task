import json
import requests

def view_vendor_performance(vendor_code):
    
    url = f"http://127.0.0.1:8000/api/vendors/{vendor_code}/performance/"

    list_of_vendors = requests.get(url=url).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    
    vendor_code = 'NSLZO'
    
    view_vendor_performance(vendor_code)
import json
import requests

def view_all_vendors():
    
    url = "http://127.0.0.1:8000/api/vendors/"

    
    list_of_vendors = requests.get(url=url).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    view_all_vendors()
import json
import requests
from login import get_session_id_from_local_file



def view_all_vendors():
    session_id = get_session_id_from_local_file()
    
    cookies = {
        "sessionid":session_id
    }
    
    url = "http://127.0.0.1:8000/api/vendors/"

    
    list_of_vendors = requests.get(url=url,cookies=cookies).json()
    
    print(json.dumps(list_of_vendors,indent=4))
    
if __name__ == '__main__':
    view_all_vendors()
import json
import requests

def get_session_id_from_local_file():
    with open('.session_id','r') as file:
        session_id = file.read()

        return session_id
    
def login():
    
    url = "http://127.0.0.1:8000/api/login/"

    payload = {
        "username":"admin",
        "password":"admin"
    }
    
    response = requests.post(url=url,json=payload)
    
    session_id = response.cookies.get('sessionid')
    
    with open('.session_id','w') as file:
        file.write(session_id)
        
    response = response.json()
    
    print(json.dumps(response,indent=4))
    
if __name__ == '__main__':
    login()
    
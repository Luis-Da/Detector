import requests
import json

def request_netflix():
    netflix_response = dict()
    response = requests.get('https://rickandmortyapi.com/api/character/787').json()
    netflix_response ['name'] = response.get('name', 'none name')
    netflix_response ['status'] = response.get('status', 'none status')
    netflix_response ['type'] = response.get('type', 'none type')
    location_object = response.get('location', [])
    url_location = location_object.get('url', '')
    
    if url_location:
        
        response = requests.get(url_location).json()
        dict_location = dict()
        dict_location['name_location'] = response.get('name', 'none name')
        dict_location ["dimension"]=response.get ("dimension","none dimension")
        dict_location ["residentes_url"]=response.get ("residents","none dimension")

        netflix_response['location'] = dict_location
      
    json_string = json.dumps(netflix_response, indent=2)
    print( json_string )

request_netflix()
import json
import requests

def request_api_star():
    space_x_response = dict()
    response = requests.get('https://swapi.dev/api/planets/59/').json()
    space_x_response['planet_name'] = response.get('name', 'No planet name')
    url_residentes = response.get('residents', [])
    if url_residentes:
        url = url_residentes[0]
        response = requests.get(url).json()
        dict_resident = dict()
        dict_resident['residents_name'] = response.get('name', 'No resident name')
        dict_resident['residents_mass'] = response.get('mass', 'No resident mass')
        dict_resident['skin_color'] = response.get('skin_color', 'No skin color')
        space_x_response['residents'] = dict_resident
        url_species = response.get('species', [])
        vehicles = response.get('vehicles', [])
        if url_species:
            url_species = url_species[0]
            response = requests.get(url_species).json()
            dict_species = dict()
            dict_species['clasification'] = response.get('classification', 'No species classification')
            dict_species['language'] = response.get('language', 'No species language')
            space_x_response['species'] = dict_species
        if vehicles:
            url_vehicles = vehicles[0]
            response = requests.get(url_vehicles).json()
            dict_vehicles = dict()
            dict_vehicles['vehicle_name'] = response.get('name', 'No vehicle name')
            dict_vehicles['manufacturer'] = response.get('manufacturer', 'No vehicle manufacturer')
            space_x_response['vehicles'] = dict_vehicles

    print(space_x_response)
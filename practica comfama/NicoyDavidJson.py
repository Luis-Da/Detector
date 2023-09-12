import requests
import json

url = "https://swapi.dev/api/planets/59"
response = requests.get(url)
planeta = response.json()  

#residentes
url = "https://swapi.dev/api/people/79"
response = requests.get(url)
residentes = response.json() 

#especie
url = "https://swapi.dev/api/species/36/"
response = requests.get(url)
especie = response.json() 


#vehiculo
url = "https://swapi.dev/api/vehicles/60/"
response = requests.get(url)
vehiculo = response.json() 

Newdata = {}
Newdata["Datos"] = []

Newdata["Datos"].append({
    "planet_name": planeta["name"],
    "residents_name": residentes["name"],
     "residents_mass": residentes["mass"],
    "skin_color": residentes["skin_color"], 
    "clasification": especie["classification"],
    "specie_languaje":  especie["language"],
    "vehicle_name": vehiculo["name"],
     "manufacturer" :  vehiculo["manufacturer"]
})

json_string = json.dumps(Newdata, indent=2)



print(json_string)
#print(Newdata)




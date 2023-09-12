# Space X encontró el planeta 59 y quiere saber unos datos sobre el 🪐 , para eso contrato a unos desarrolladores de Cadena Santa Fe para esta misión, el desarrollador o desarrolladora tendrá que hacer un consumo a una API de star wars “**https://swapi.dev/api/planets/59/**” y estando en este planeta tendrá que averiguar los siguiente:
	
# El nombre del planeta 🪐

# Estando en el planeta averiguar quienes son sus residentes(Ojos bien abiertos 👀)

# Nombre de los residentes
# Masa de los residentes
# Color de piel
# Luego de esto necesita saber cual es la especie:
# Clasificación de la especie
# Lenguaje de la especie
# Por último Space X necesita saber si tienen vehículos:
# Nombre del vehículo
# Fabricante del vehículo
# Esta información debemos entregarla en formato JSON con los datos anteriormente solicitados por Space X.

# "El nombre del planeta": "",
#     "Nombre de los residentes": "",
#     "Masa de los residentes": "",
#     "Color de piel": "", 
#     "Clasificacion de la especie": "",
#     "Lenguaje de la especie": "",
#     "Nombre del vehiculo": "",
#     "Fabricante del vehiculo": ""



# refuerzo




# De Netflix nos contrataron para que realicemos un desarrrollo en Python que consta de lo siguiente:
# Realizar una petición HTTP tipo GET a la siguiente URL: “https://rickandmortyapi.com/api/character/787”
# de allí debemos obtener la siguiente información:


	
# Nombre	
# Estado	
# tipo


# También debemos conocer su ubicación y sacar los siguientes datos:


	
# Nombre	
# Dimensión	
# Las URL de los residentes


# Netflix espera que le retornemos la información de la siguiente manera:

# {
#     "name": "Nombre",
#     "status": "Estado ",
#     "type": "Tipo de personaje",
#     "location": {
#         "name_location": "ubicación",
#         "dimension": "Dimension",
#         "residentes_url": [
#             "url1", "url2", "N cantidad de URLS"
#         ]
#     }
# }
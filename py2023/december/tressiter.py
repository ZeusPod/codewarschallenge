import requests



api_key = 'MovVT3sN3dbEisybYM4EyUR0LxaSoS7b'


# URL base para la API de inversión geográfica de TomTom
base_url = "https://api.tomtom.com/search/2/reverseGeocode/"

# Coordenadas que deseas invertir (ejemplo: Mountain View, CA)
latitud = 10.171684  
longitud = -67.547072
# Parámetros de la solicitud
params = {
    'key': api_key,
    'position': f"{latitud},{longitud}",
    'returnSpeedLimit': 'true',  # Puedes ajustar según tus necesidades
    'language': 'es',  # Puedes ajustar según tus necesidades
    # Agrega más parámetros según la documentación si es necesario
}

# Realiza la solicitud GET a la API de TomTom
response = requests.get(base_url, params=params)

# Verifica el código de estado de la respuesta
if response.status_code == 200:
    # La solicitud fue exitosa
    data = response.json()
    
    # Accede a la información de la dirección
    direccion = data['addresses'][0]['address']['freeformAddress']
    print(f"Dirección: {direccion}")
else:
    # La solicitud falló
    print(f"Error {response.status_code}: {response.text}")

# importando libreria requests
import requests
import json

url = 'https://reqres.in/api/users' # url de la API

payload = {}
headers = {}

def api_desafio(verbo, url, headers=headers, data=payload):

    # Creando una variable con la solicitud de toda la informacion.
    response = requests.request(verbo, url, headers=headers, data=payload)
    return response


if __name__ == '__main__':

    url = 'https://reqres.in/api/users' # url de la API

    # Obteniendo toda la informacion con 'GET'
    users_data = api_desafio('GET', url)
    print(f'{"Obteniendo toda la informacion":=^100}') # titulo
    print(f"{users_data}") # muestra el codigo de la respuesta. |<Response [200]>|
    #print(type(users_data)) # muestra la class del codigo. |<class 'requests.models.Response'>|
    print('---------------------')
    print(users_data.text) # response text muestra el contenido del response.
    print(type(users_data.text)) # el contenido es <calss 'str'>

    # Creando un usuario con POST
    print(f'{"Creando un usuario":=^100}') # titulo
    # Creando variable con los keys y values solicitados
    created_user = '''{
        "email":"ignacio.profesor@gmail.com",
        "first_name": "Ignacio", "last_name":
        "Correa", "avatar": "profesor"
        }'''
    response = api_desafio('POST', url, data = created_user) # incorporando el usuario con la API
    print(response)
    print(response.text)

    # Actualizando un usuario
    print(f'{"Modificando un usuario":=^100}') # titulo
    update_data = {"name": "morpheus", "residence": "zion"} # datos que se modificaran del usuario
    update_user = api_desafio('PUT', 'https://reqres.in/api/users/3', data = update_data) # la url es para el usuario 3
    print(update_user)
    print(update_user.text)

    print(f'{"Eliminando un usuario":=^100}') # titulo
    deleted_user = api_desafio('DELETE','https://reqres.in/api/users/4') # la url es para el usuario 4
    print(deleted_user)
    print(deleted_user.text)

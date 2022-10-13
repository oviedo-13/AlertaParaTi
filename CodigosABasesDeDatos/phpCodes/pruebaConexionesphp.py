import requests
import json

clima_url = "https://alerta-para-ti.azurewebsites.net/recuperarClima.php"

keys = {
    'fecha': '2022-10-03'
}
clima_response = requests.request("GET", clima_url, params=keys)
clima_response_data = json.loads(clima_response.text)

for x in clima_response_data:
    print(x)
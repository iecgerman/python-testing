# primero activamos el venv
# .\venv\Scripts\activate

#Instalamos requests
# pip install requests -q (la -q es para que nos muestre los procesos de instalacion)

# pip list (para verificar que se instalo)

# creamos un archivo requirements.txt
# (venv) PS C:\Users\info\github\python-testing> pip freeze | grep requests
# requests==2.32.3 (esto lo copiamos al requirements.txt)

import requests

def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    # para salir de la terminal en ipdb, ponemos "q + enter"
    # import ipdb; ipdb.set_trace()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"],
    }

if __name__ == "__main__":
    print (get_location("8.8.8.8"))

# Resultado

# (venv) PS C:\Users\info\github\python-testing> python src/api_client.py
# {'country': 'United States of America', 'region': 'California', 'city': 'Mountain View'}
# (venv) PS C:\Users\info\github\python-testing> 

# en el seg. 10,07 dice el profe que en clases previas instalamos una libreria llamada ipdb, como estamos en otra computadora hay que instalar de nuevo ipdb

# pip install ipdb

# compiamos el requirements.txt
# pip freeze | grep ipdb
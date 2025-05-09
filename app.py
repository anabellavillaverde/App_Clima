from flask import Flask, render_template, request
import requests

app = Flask(__name__) # inicia aplicacion web

ciudades = {        #diccionario de ciudades
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Córdoba": {"lat": -31.4201, "lon": -64.1888},
    "Madrid": {"lat": 40.4168, "lon": -3.7038},
    "Nueva York": {"lat": 40.7128, "lon": -74.0060},
    "Tokio": {"lat": 35.6895, "lon": 139.6917},
    "París": {"lat": 48.8566, "lon": 2.3522},
    "Londres": {"lat": 51.5074, "lon": -0.1278},
    "Sídney": {"lat": -33.8688, "lon": 151.2093},
    "Ciudad de México": {"lat": 19.4326, "lon": -99.1332},
    "El Cairo": {"lat": 30.0444, "lon": 31.2357}
}

@app.route("/") #Ruta raíz / – Página inicial
def index():
    return render_template("index.html", ciudades=ciudades)

@app.route("/clima")    #Ruta /clima – Consulta a la API
def clima():
    ciudad = request.args.get("ciudad")
    if ciudad not in ciudades:      #Verifica que la ciudad exista en el diccionario, si no muestra error 404.
        return "Ciudad no encontrada", 404

    lat = ciudades[ciudad]["lat"] #latitud
    lon = ciudades[ciudad]["lon"] #longitud
    
    #  API Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    datos = response.json()
    clima_actual = datos["current_weather"]

import os
import random
import requests
import flask
from flask import jsonify, request

OPENWEATHER_KEY = os.environ['OPENWEATHER_KEY']
OPENWEATHER_URL = \
    f'https://api.openweathermap.org/data/2.5/weather?appid={OPENWEATHER_KEY}'

TRACKS = {
    "party": [
        "Wake Me Up - Avicii",
        "One More Time - Daft Punk",
        "One Kiss - Calvin Harris",
    ],
    "pop": [
        "test drive - Ariana Grande",
        "Starboy - The Weeknd",
        "Shape of You - Ed Sheeran",
    ],
    "rock": [
        "Another One Bites The Dust - Queen",
        "Stairway to Heaven - Led Zeppelin",
        "Dreams - Fleetwood Mac",
    ],
    "classical": [
        "Hungarian Rhapsody - Liszt", 
        "Grande valse brillante - Chopin",
        "Minuet in G major - Letzold",
        "Piano Sonata No. 16 - Mozart",
        "La Campanella - Liszt",
    ],
}

app = flask.Flask(__name__)
db = []

def pick_track(temp):
    temp -= 273.15 # K -> C
    genre = None
    if temp > 30: genre = "party"
    elif 15 <= temp <= 30: genre = "pop"
    elif 10 <= temp < 15: genre = "rock"
    else: genre = "classical"
    return random.choice(TRACKS[genre])
    

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "up"})

@app.route('/processPathData/<pathParameter>', methods=['GET'])
def echo_path(pathParameter):
    return jsonify({"pathParam": pathParameter})

@app.route('/processQueryData', methods=['GET'])
def process_query_data():
    kv = list(request.args.items())[0]
    return jsonify({"key": str(kv[0]), "value": str(kv[1])})

@app.route('/processPOSTData', methods=['POST'])
def post_body():
    req = request.json
    return jsonify({"values": [req["value1"], req["value2"], req["value3"], req["value4"]]})

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'GET':
        return jsonify(db)
    else:
        db.append(request.json["newString"])
        return "", 201

@app.route('/data/<int:index>', methods=['DELETE'])
def data_delete(index):
    db.pop(index)
    return "", 200

@app.route('/music', methods=['GET'])
def music():
    if 'city' in request.args:
        url = f'{OPENWEATHER_URL}&q={request.args["city"]}'
        r = requests.get(url)
        temp = r.json()["main"]["temp"]
        return pick_track(temp)
    elif 'lat' in request.args and 'lon' in request.args:
        lat = request.args['lat']
        lon = request.args['lon']
        url = f'{OPENWEATHER_URL}&lat={lat}&lon={lon}'
        temp = requests.get(url).json()["main"]["temp"]
        return pick_track(temp)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

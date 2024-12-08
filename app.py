from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/events', methods=['GET'])
def get_events():
    # Placeholder for event data
    events =[
        {"name": "Gravel Race", "location": "Austin, TX", "date": "2024-12-15"},
        {"name": "Mountain Ride", "location": "Denver, CO", "date": "2024-12-20"}
    ]
    return jsonify(events)

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('location')  # Example: ?location=London
    api_key = os.getenv('WEATHER_API_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Unable to fetch weather data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
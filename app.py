from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Ride Events API! Use the endpoints to get data."

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
    # Get location coordinates from user input
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    # Check if latitude and longitude are provided
    if not latitude or not longitude:
        return jsonify({"error": "Please provide latitude and longitude"}), 400

    # Construct the Open-Meteo API URL
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"

    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
        data = response.json()
        return jsonify(data)  # Return the weather data as JSON
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
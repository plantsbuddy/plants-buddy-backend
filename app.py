from flask import Flask, request, jsonify
import requests
import json
import controllers.plants as plants
import controllers.diseases as diseases
import controllers.pests as pests
import controllers.plant_suggestions as plant_suggestions
import controllers.plantation_suggestions as plantation_suggestions
import controllers.general_plantation_tips as general_plantation_tips

app = Flask(__name__)


@app.route('/chatbot', methods=['POST'])
def get_plant_details():
    body = request.get_json()
    data = body['data']
    intent = body['intent']

    response = None

    if intent == 'plant-all-details':
        response = plants.get_all_details(data)

    elif intent == 'plant-scientific-name':
        response = plants.get_scientific_name(data)

    elif intent == 'plant-common-names':
        response = plants.get_common_names(data)

    elif intent == 'plant-genus':
        response = plants.get_genus(data)

    elif intent == 'plant-family':
        response = plants.get_family(data)

    elif intent == 'plant-description':
        response = plants.get_description(data)

    elif intent == 'plant-uses':
        response = plants.get_uses(data)

    elif intent == 'plant-seasons':
        response = plants.get_seasons(data)

    elif intent == 'plant-blooming-time':
        response = plants.get_blooming_time(data)

    elif intent == 'plant-soil-requirement':
        response = plants.get_soil_requirement(data)

    elif intent == 'plant-growth-environment':
        response = plants.get_growth_environment(data)

    elif intent == 'plant-watering-requirements':
        response = plants.get_watering_requirements(data)

    elif intent == 'disease-all-details':
        response = diseases.get_all_details(data)

    elif intent == 'disease-common-name':
        response = diseases.get_common_name(data)

    elif intent == 'disease-class':
        response = diseases.get_disease_class(data)

    elif intent == 'disease-scientific-name':
        response = diseases.get_scientific_name(data)

    elif intent == 'disease-brief-summary':
        response = diseases.get_brief_summary(data)

    elif intent == 'disease-symptoms':
        response = diseases.get_symptoms(data)

    elif intent == 'disease-host-plants':
        response = diseases.get_host_plants(data)

    elif intent == 'disease-causes':
        response = diseases.get_causes(data)

    elif intent == 'disease-organic-control':
        response = diseases.get_organic_control(data)

    elif intent == 'disease-chemical-control':
        response = diseases.get_chemical_control(data)

    elif intent == 'disease-preventive-measures':
        response = diseases.get_preventive_measures(data)

    elif intent == 'pest-all-details':
        response = pests.get_all_details(data)

    elif intent == 'pest-common-name':
        response = pests.get_common_name(data)

    elif intent == 'pest-class':
        response = pests.get_pest_class(data)

    elif intent == 'pest-scientific-name':
        response = pests.get_scientific_name(data)

    elif intent == 'pest-brief-summary':
        response = pests.get_brief_summary(data)

    elif intent == 'pest-symptoms':
        response = pests.get_symptoms(data)

    elif intent == 'pest-host-plants':
        response = pests.get_host_plants(data)

    elif intent == 'pest-causes':
        response = pests.get_causes(data)

    elif intent == 'pest-organic-control':
        response = pests.get_organic_control(data)

    elif intent == 'pest-chemical-control':
        response = pests.get_chemical_control(data)

    elif intent == 'pest-preventive-measures':
        response = pests.get_preventive_measures(data)

    return jsonify(response)


@app.route('/plantation-guides', methods=['GET'])
def plantation_guides():
    guides = None

    with open('plantation_guides.json', 'r') as f:
        # Load the JSON data from the file
        guides = json.load(f)

    # Print the data
    return guides


@app.route('/random-plantation-suggestion', methods=['GET'])
def random_suggestion():
    return general_plantation_tips.get_random_plantation_tip()


@app.route('/weather-data', methods=['POST'])
def weather_data():
    weather_data = get_weather_data(request.get_json())

    weather_details = {
        'temperature': round(weather_data['main']['temp'] - 273.15, 1),
        'city': weather_data['name'],
        'weather_status_title': weather_data['weather'][0]['main'],
        'weather_status_description': weather_data['weather'][0]['description'],
        'weather_status_icon': f'https://openweathermap.org/img/wn/{weather_data["weather"][0]["icon"]}.png',
        'humidity': weather_data['main']['humidity'],
        'wind_speed': weather_data['wind']['speed'],
        'precipitation': weather_data['rain']['1h'] if 'rain' in weather_data else 0,
    }

    return jsonify(weather_details)


@app.route('/weather-based-suggested-plants', methods=['POST'])
def weather_based_suggested_plants():
    weather_data = get_weather_data(request.get_json())

    suggested_plants = plant_suggestions.get_plant_suggestions(weather_data)
    return jsonify(suggested_plants)


@app.route('/weather-based-plantation-suggestions', methods=['POST'])
def weather_based_plantation_suggestions():
    weather_data = get_weather_data(request.get_json())
    gardening_suggestions = plantation_suggestions.get_weather_based_plantation_suggestions(
        weather_data)

    return jsonify(gardening_suggestions)


def get_weather_data(request_body):
    longitude = request_body['longitude']
    latitude = request_body['latitude']

    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=8e2fa5ebb383d5cd7dd42e1a5bf4d449'
    response = requests.get(url)
    data = response.json()
    return data

    # if __name__ == '__main__':
    #     # Threaded option to enable multiple instances for multiple user access
    #     app.run(port=process.env.PORT)

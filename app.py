from flask import Flask, request, jsonify
import requests
import controllers.plants as plants
import controllers.diseases as diseases
import controllers.pests as pests
import controllers.plant_suggestions as plant_suggestions
import controllers.plantation_suggestions as plantation_suggestions

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


@app.route('/random-suggestion', methods=['GET'])
def random_suggestion():
    return jsonify({'suggestion': 'Hello There'})


@app.route('/weather-data', methods=['POST'])
def weather_data():
    pass


@app.route('/weather-based-suggested-plants', methods=['POST'])
def weather_based_suggested_plants():
    body = request.get_json()
    longitude = body['longitude']
    latitude = body['latitude']

    weather_data = get_weather_data(longitude, latitude)

    suggested_plants = plant_suggestions.get_plant_suggestions(weather_data)
    return jsonify(suggested_plants)


@app.route('/weather-based-plantation-suggestions', methods=['POST'])
def weather_based_plantation_suggestions():
    body = request.get_json()
    longitude = body['longitude']
    latitude = body['latitude']
    weather_data = get_weather_data(longitude, latitude)

    gardening_suggestions = plantation_suggestions.get_weather_based_plantation_suggestions(
        weather_data)

    return jsonify(gardening_suggestions)


def get_weather_data(longitude, latitude):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid=8e2fa5ebb383d5cd7dd42e1a5bf4d449'
    response = requests.get(url)
    data = response.json()
    return data

    # if __name__ == '__main__':
    #     # Threaded option to enable multiple instances for multiple user access
    #     app.run(port=process.env.PORT)

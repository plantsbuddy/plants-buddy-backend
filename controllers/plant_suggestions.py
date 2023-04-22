# Define the weather conditions
def get_plant_suggestions(weather_data):
    temperature = round(weather_data['main']['temp'] - 273.15, 1)
    humidity = weather_data['main']['humidity']
    precipitation = weather_data['rain']['1h'] if 'rain' in weather_data else 0

    # Define the plant suggestions for different weather conditions
    drought_tolerant_plants = ['cactus', 'succulent', 'yucca',
                               'thyme', 'lavender', 'agave', 'echeveria', 'sedum', 'olive tree']
    cold_tolerant_plants = ['fir', 'cedar', 'spruce', 'holly',
                            'heather', 'dogwood', 'birch', 'juniper', 'rhododendron']
    water_loving_plants = ['rice', 'watermelon', 'lotus', 'bamboo',
                           'cattail', 'papyrus', 'sedge', 'bullrush', 'arrowhead']
    moderate_plants = ['tomato', 'basil', 'rosemary', 'mint',
                       'marjoram', 'thyme', 'oregano', 'sage', 'parsley']

    # Apply rules for plant suggestions based on weather conditions
    if temperature > 30 and humidity < 40:
        suggestions = {"plants": drought_tolerant_plants,
                       "weather_type": "Weather at your location is dry, here is a list of drought tolerant plants that could grow well in this weather"}

    elif temperature < 10 and humidity > 70:
        suggestions = {"plants": cold_tolerant_plants,
                       "weather_type": "Weather at your location is cool, here is a list of cold tolerant plants that could grow well in this weather"}
    elif precipitation > 5 and humidity > 80:
        suggestions = {"plants": water_loving_plants,
                       "weather_type": "Weather at your location is humid, here is a list of water loving plants that could grow well in this weather"}
    else:
        suggestions = {"plants": moderate_plants,
                       "weather_type": "Weather at your location is moderate, here is a list of plants that could grow well in this weather"}

    # Display the plant suggestions to the user

    return suggestions

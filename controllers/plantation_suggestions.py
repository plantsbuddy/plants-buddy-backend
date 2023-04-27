import random

# Gardening tips for different weather conditions
clear_tips = ['Make sure your plants are getting enough water and sun exposure.',
              'Remove any dead leaves or branches from your plants.', 'Prune your plants to encourage healthy growth.']
cloudy_tips = ['Your plants may not need as much water, but still ensure they are getting adequate sunlight.',
               'Use this time to plant shade-loving plants, such as ferns or hostas.', 'Fertilize your plants to encourage growth.']
rainy_tips = ['You may not need to water your plants today. However, make sure they are not getting too much water and are well-drained.',
              'Cover your plants with plastic bags to protect them from heavy rain.', 'Avoid pruning your plants on a rainy day.']
snowy_tips = ['Protect your plants from frost damage by covering them with blankets or sheets.',
              'Do not attempt to remove snow from plants, as it can damage them.', 'Avoid planting new plants during the winter season.']
thunderstorm_tips = ['Move potted plants indoors to avoid damage from strong winds and hail.',
                     'Water your plants a few hours before the storm to help them withstand the wind and rain.', 'Check your plants for damage after the storm has passed.']

# Gardening tips for different temperature ranges
cold_tips = ['Protect your plants from frost by covering them with blankets or sheets.',
             'Water your plants early in the day to allow time for the water to soak in before it freezes.', 'Move potted plants indoors to protect them from freezing temperatures.']
moderate_tips = ['Make sure your plants are getting enough water and sun exposure.',
                 'Fertilize your plants to encourage healthy growth.', 'Prune your plants to keep them in good shape.']
hot_tips = ['Make sure your plants are getting enough water and shade.',
            'Water your plants early in the morning or late in the evening to avoid evaporation.', 'Add mulch to your garden to help retain moisture.']

low_humidity_low_wind_tips = ['Water your plants more frequently and consider using a humidifier to increase humidity.',
                              'Choose plants that thrive in dry conditions, such as cacti or succulents.']
low_humidity_high_wind_tips = ['Water your plants more frequently and use a windbreak to protect them from strong winds.',
                               'Choose plants that are drought-tolerant and can withstand windy conditions, such as lavender or thyme.']
high_humidity_low_wind_tips = ['Ensure good air circulation around your plants and avoid over-watering.',
                               'Choose plants that thrive in high humidity, such as ferns or orchids.']
high_humidity_high_wind_tips = ['Ensure good air circulation around your plants and use a windbreak to protect them from strong winds.',
                                'Choose plants that can withstand both high humidity and windy conditions, such as bamboo or palms.']

# Function to get current weather data from OpenWeatherMap API


# Function to provide gardening tips based on weather data
def get_weather_based_plantation_suggestions(weather_data):
    weather = weather_data['weather'][0]['main'].lower()
    # Convert temperature from Kelvin to Celsius
    temp = round(weather_data['main']['temp'] - 273.15)
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    # Provide gardening tips based on weather conditions
    if weather == 'clear':
        tips = clear_tips
    elif weather == 'clouds':
        tips = cloudy_tips
    elif weather == 'rain':
        tips = rainy_tips
    elif weather == 'snow':
        tips = snowy_tips
    elif weather == 'thunderstorm':
        tips = thunderstorm_tips
    else:
        tips = []

    # Add gardening tips based on temperature range
    if temp < 5:
        tips += cold_tips
    elif temp > 30:
        tips += hot_tips
    else:
        tips += moderate_tips

    if humidity < 50 and wind_speed < 10:
        tips += low_humidity_low_wind_tips
    elif humidity < 50 and wind_speed >= 10:
        tips += low_humidity_high_wind_tips
    elif humidity >= 50 and wind_speed < 10:
        tips += high_humidity_low_wind_tips
    elif humidity >= 50 and wind_speed >= 10:
        tips += high_humidity_high_wind_tips

    # Randomly pick 3 gardening tips from the list and return them
    if tips:
        return {'suggestions': random.sample(tips, 3)}

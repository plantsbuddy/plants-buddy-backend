from db_config import db
import requests
import json
import random

plants_collection = db.collection('chatbot_plants_data')


def get_plant_document(name: str):
    name = name.strip().lower()
    plant = plants_collection.document(document_id=name).get()

    if plant is None:
        plant = plants_collection.where(
            'common_names_for_search', 'array_contains', name).limit(1).get()

    if plant is None:
        plant = plants_collection.where(
            'scientific_name_for_search', '==', name).limit(1).get()

    plant_dict = plant.to_dict()

    if plant_dict is not None:
        del plant_dict['name_for_search']
        del plant_dict['scientific_name_for_search']
        del plant_dict['common_names_for_search']

    return plant_dict


def get_all_details(name: str):
    plant = get_plant_document(name)

    response = None
    if plant is not None:
        response = f'''
        Here are the details of your requested plant {name}:
        <br><br>
        <b>Name</b>
        <br>
        {plant['name']}
        <br><br>
        <b>Scientific name</b>
        <br>
        {plant['scientific_name']}
        <br><br>
        <b>Common names</b>
        <br>
        {plant['common_names']}
        <br><br>
        <b>Description</b>
        <br>
        {plant['description']}
        '''

        if 'seasons' in plant:
            response += f'''
            <br><br>
            <b>Seasons</b>
            <br>
            {plant['seasons']}
            '''

        if 'soil_requirement' in plant:
            response += f'''
            <br><br>
            <b>Soil requirements</b>
            <br>
            {plant['soil_requirement']}
            '''

        if 'growth_environment' in plant:
            response += f'''
            <br><br>
            <b>Growth environment</b>
            <br>
            {plant['growth_environment']}
            '''

        if 'watering' in plant:
            response += f'''
            <br><br>
            <b>Watering requirements</b>
            <br>
            {plant['watering']}
            '''

        if 'uses' in plant:
            response += f'''
            <br><br>
            <b>Uses</b>
            <br>
            {plant['uses']}
            '''
    else:
        url = f'https://trefle.io/api/v1/plants/search?token=p463NVxlv9_r8WUsHXts_JVNCwWx5U54WXElhcaNOps&q={name}.'

        api_response = requests.get(url)
        data = json.loads(api_response.text)

        response = None
        if len(data["data"]) > 0:
            api_response = data["data"][0]

            response = f'''
            Here are the details of your requested plant {name}:
            <br><br>
            <b>Common name</b>
            <br>
            {api_response['common_name']}
            <br><br>
            <b>Scientific name</b>
            <br>
            {api_response['scientific_name']}
            <br><br>
            <b>Genus</b>
            <br>
            {api_response['genus']}
            <br><br>
            <b>Family</b>
            <br>
            It's family is {api_response['family']}, and the common name of family is {api_response['family']}
            <br><br>
            <b>Family</b>
            <br>
            It's family is {api_response['family']}, and the common name of family is {api_response['family']}
            '''

            if len(api_response['synonyms']) > 0:
                response += f'''
                <br><br>
                <b>Synonyms of plant</b>
                <br>
                {", ".join(api_response['synonyms'])}
                '''

    return process_response(name, response)


def get_scientific_name(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        scientific_name = plant.get('scientific_name')
        response = f'The scientific name of the plant {name} is {scientific_name}.'
    return process_response(name, response)


def get_common_names(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        common_names = plant.get('common_names')
        response = f'The common names for plant {name} are:<br><br>{common_names}.'
    return process_response(name, response)


def get_genus(name: str) -> str:
    url = f'https://trefle.io/api/v1/plants/search?token=p463NVxlv9_r8WUsHXts_JVNCwWx5U54WXElhcaNOps&q={name.strip().replace(" ", "+")}'

    api_response = requests.get(url)
    data = json.loads(api_response.text)

    response = None
    if len(data["data"]) > 0:
        response = f'The genus of plant {name} is {data["data"][0]["genus"]}.'

    return process_response(name, response)


def get_family(name: str) -> str:
    url = f'https://trefle.io/api/v1/plants/search?token=p463NVxlv9_r8WUsHXts_JVNCwWx5U54WXElhcaNOps&q={name.strip().replace(" ", "+")}'

    api_response = requests.get(url)
    data = json.loads(api_response.text)

    response = None
    if len(data["data"]) > 0:
        family = data['data'][0]['family']
        family_common_name = data['data'][0]['family_common_name']
        response = f'The family of the plant {name} is {family}, and the common name of the family is {family_common_name}.'
    return process_response(name, response)


def get_description(name: str) -> str:
    plant = get_plant_document(name)
    description = None
    if plant is not None:
        description = plant.get('description')
    return process_response(name, description)


def get_uses(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        uses = plant.get('uses')
        response = f'The uses of the plant {name} are:<br><br>{uses}'
    return process_response(name, response)


def get_seasons(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        seasons = plant.get('seasons')
        response = f'The growth season of the plant {name} is {seasons}.'
    return process_response(name, response)


def get_blooming_time(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        blooming_time = plant.get('blooming_time')
        response = f'The blooming time of the plant {name} is {blooming_time}.'
    return process_response(name, response)


def get_soil_requirement(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        soil_requirement = plant.get('soil_requirement')
        response = f'The soil requirement for the plant {name} is:<br><br>{soil_requirement}'
    return process_response(name, response)


def get_growth_environment(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        growth_environment = plant.get('growth_environment')
        response = f'The growth environment for the plant {name} is:<br><br>{growth_environment}'
    return process_response(name, response)


def get_watering_requirements(name: str) -> str:
    plant = get_plant_document(name)
    response = None
    if plant is not None:
        watering_requirements = plant.get('watering')
        response = f'The watering requirement of the plant {name} is:<br><br>{watering_requirements}'
    return process_response(name, response)


def process_response(plant_name, response):
    if response is not None:
        return response
    else:
        fallback_responses = [
            "I'm afraid I couldn't find information about that plant.",
            "Hmm, I'm not sure what you're asking about.",
            "I don't have your asked details on that plant.",
            "I'm not able to find your requested information on that specific plant.",
            "Unfortunately, I don't have the information on that particular plant.",
            "I'm sorry, but I couldn't find the information you're looking for.",
            "I'm afraid I don't have the requested information of that plant.",
            "I'm sorry, I wasn't able to find the details on that plant.",
            "I'm not able to find the information about that plant.",
            "I couldn't find the information on that plant.",
            "I'm sorry, but I don't have the information about that plant.",
            "I'm afraid I couldn't find the details on that specific plant.",
            "Unfortunately, I don't have the information on that plant.",
            "I'm sorry, I don't have the information on that plant at this time.",
            "I'm not able to find the details about that plant.",
            "I'm afraid I don't have the information on that specific plant.",
            "I'm sorry, I couldn't find the information about that plant.",
            "I'm not able to find the information on that particular plant.",
            "I'm sorry, but I don't have the details on that plant.",
            "I'm afraid I couldn't find the information on that plant."
        ]

        random_number = random.randint(0, len(fallback_responses) - 1)

        return fallback_responses[random_number]

from db_config import db
import random


pests_collection = db.collection('chatbot_pests_data')


def get_pest_document(name: str):
    name = name.strip().lower()
    pest = pests_collection.document(document_id=name).get()

    if pest is None:
        pest = pests_collection.where(
            'scientific_name_for_search', '==', name).limit(1).get()

    pest_dict = pest.to_dict()

    if pest_dict is not None:
        del pest_dict['scientific_name_for_search']

    return pest_dict


def get_all_details(name: str):
    pest = get_pest_document(name)

    response = None
    if pest is not None:
        response = f'''
        Here are the details of your requested pest {name}:
        <br><br>
        <b>Common name</b>
        <br>
        {pest['name']}
        <br><br>
        <b>Scientific name</b>
        <br>
        {pest['scientific_name']}
        <br><br>
        <b>pest class</b>
        <br>
        {pest['pest_class']}
        <br><br>
        <b>In a nutshell</b>
        <br><ul>
        '''

        for point in pest['in_a_nutshell']:
            response += f'<li>{point}</li>'

        response += f'''
        </ul>
        <br><br>
        <b>Symptoms</b>
        <br>
        {pest['symptoms']}
        <br><br>
        <b>Causes</b>
        <br>
        {pest['causes']}
        <br><br>
        <b>Organic control</b>
        <br>
        {pest['organic_control']}
        <br><br>
        <b>Chemical control</b>
        <br>
        {pest['chemical_control']}
        <br><br>
        <b>Preventive measures</b>
        <br><ul>
        '''

        for measure in pest['preventive_measures']:
            response += f'<li>{measure}</li>'

        response += '</ul>'

        if 'host_plants' in pest:
            response += f'''
            <br><br>
            <b>Host plants</b>
            <br>
            {', '.join(pest['host_plants'])}
            '''

    return process_response(name, response)


def get_scientific_name(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        scientific_name = pest.get('scientific_name')
        response = f'The scientific name of the pest {name} is {scientific_name}.'
    return process_response(name, response)


def get_pest_class(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        pest_class = pest.get('pest_class')
        response = f'The class of the pest {name} is {pest_class}.'
    return process_response(name, response)


def get_common_name(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        common_name = pest.get('name')
        response = f'The common name of the pest {name} is {common_name}.'
    return process_response(name, response)


def get_brief_summary(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        brief_summary = pest.get('in_a_nutshell')
        response = f'Here is a brief summary of the pest {name}:<br><br><ul>'

        for point in brief_summary:
            response += f'<li>{point}</li>'

        response += '</ul>'

    return process_response(name, response)


def get_symptoms(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        symptoms = pest.get('symptoms')
        response = f'The symptoms of the pest {name} are:<br><br>{symptoms}'
    return process_response(name, response)


def get_host_plants(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        host_plants = pest.get('host_plants')
        response = f'Here are the host pests of the pest {name}:<br><br> {", ".join(host_plants)}'
    return process_response(name, response)


def get_causes(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        causes = pest.get('causes')
        response = f'The causes of the pest {name} are:<br><br>{causes}'
    return process_response(name, response)


def get_organic_control(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        organic_control = pest.get('organic_control')
        response = f'The organic control procedure of the pest {name} is:<br><br>{organic_control}'
    return process_response(name, response)


def get_chemical_control(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        chemical_control = pest.get('chemical_control')
        response = f'The chemical control procedure of the pest {name} is:<br><br>{chemical_control}'
    return process_response(name, response)


def get_preventive_measures(name: str) -> str:
    pest = get_pest_document(name)
    response = None
    if pest is not None:
        preventive_measures = pest.get('preventive_measures')

        response = f'Here are some preventive measures for the pest {name}:<br><br><ul>'

        for measure in preventive_measures:
            response += f'<li>{measure}</li>'

        response += '</ul>'
    return process_response(name, response)


def process_response(pest_name, response):
    if response is not None:
        return response
    else:
        fallback_responses = [
            "I'm afraid I couldn't find information about that pest.",
            "Hmm, I'm not sure what you're asking about.",
            "I don't have your asked details on that pest.",
            "I'm not able to find your requested information on that specific pest.",
            "Unfortunately, I don't have the information on that particular pest.",
            "I'm sorry, but I couldn't find the information you're looking for.",
            "I'm afraid I don't have the requested information of that pest.",
            "I'm sorry, I wasn't able to find the details on that pest.",
            "I'm not able to find the information about that pest.",
            "I couldn't find the information on that pest.",
            "I'm sorry, but I don't have the information about that pest.",
            "I'm afraid I couldn't find the details on that specific pest.",
            "Unfortunately, I don't have the information on that pest.",
            "I'm sorry, I don't have the information on that pest at this time.",
            "I'm not able to find the details about that pest.",
            "I'm afraid I don't have the information on that specific pest.",
            "I'm sorry, I couldn't find the information about that pest.",
            "I'm not able to find the information on that particular pest.",
            "I'm sorry, but I don't have the details on that pest.",
            "I'm afraid I couldn't find the information on that pest."
        ]

        random_number = random.randint(0, len(fallback_responses) - 1)

        return fallback_responses[random_number]

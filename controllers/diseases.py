from db_config import db
import random


diseases_collection = db.collection('chatbot_diseases_data')


def get_disease_document(name: str):
    name = name.strip().lower()
    disease = diseases_collection.document(document_id=name).get()

    if disease is None:
        disease = diseases_collection.where(
            'scientific_name_for_search', '==', name).limit(1).get()

    disease_dict = disease.to_dict()

    if disease_dict is not None:
        del disease_dict['scientific_name_for_search']

    return disease_dict


def get_all_details(name: str):
    disease = get_disease_document(name)

    response = None
    if disease is not None:
        response = f'''
        Here are the details of your requested disease {name}:
        <br><br>
        <b>Common name</b>
        <br>
        {disease['name']}
        <br><br>
        <b>Scientific name</b>
        <br>
        {disease['scientific_name']}
        <br><br>
        <b>disease class</b>
        <br>
        {disease['disease_class']}
        <br><br>
        <b>In a nutshell</b>
        <br><ul>
        '''

        for point in disease['in_a_nutshell']:
            response += f'<li>{point}</li>'

        response += f'''
        </ul>
        <br><br>
        <b>Symptoms</b>
        <br>
        {disease['symptoms']}
        <br><br>
        <b>Causes</b>
        <br>
        {disease['causes']}
        <br><br>
        <b>Organic control</b>
        <br>
        {disease['organic_control']}
        <br><br>
        <b>Chemical control</b>
        <br>
        {disease['chemical_control']}
        <br><br>
        <b>Preventive measures</b>
        <br><ul>
        '''

        for measure in disease['preventive_measures']:
            response += f'<li>{measure}</li>'

        response += '</ul>'

        if 'host_plants' in disease:
            response += f'''
            <br><br>
            <b>Host plants</b>
            <br>
            {', '.join(disease['host_plants'])}
            '''

    return process_response(name, response)


def get_scientific_name(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        scientific_name = disease.get('scientific_name')
        response = f'The scientific name of the disease {name} is {scientific_name}.'
    return process_response(name, response)


def get_disease_class(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        disease_class = disease.get('disease_class')
        response = f'The class of the disease {name} is {disease_class}.'
    return process_response(name, response)


def get_common_name(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        common_name = disease.get('name')
        response = f'The common name of the disease {name} is {common_name}.'
    return process_response(name, response)


def get_brief_summary(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        brief_summary = disease.get('in_a_nutshell')
        response = f'Here is a brief summary of the disease {name}:<br><br><ul>'

        for point in brief_summary:
            response += f'<li>{point}</li>'

        response += '</ul>'

    return process_response(name, response)


def get_symptoms(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        symptoms = disease.get('symptoms')
        response = f'The symptoms of the disease {name} are:<br><br>{symptoms}'
    return process_response(name, response)


def get_host_plants(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        host_plants = disease.get('host_plants')
        response = f'Here are the host diseases of the disease {name}:<br><br> {", ".join(host_plants)}.'
    return process_response(name, response)


def get_causes(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        causes = disease.get('causes')
        response = f'The causes of the disease {name} are:<br><br>{causes}'
    return process_response(name, response)


def get_organic_control(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        organic_control = disease.get('organic_control')
        response = f'The organic control procedure of the disease {name} is:<br><br>{organic_control}'
    return process_response(name, response)


def get_chemical_control(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        chemical_control = disease.get('chemical_control')
        response = f'The chemical control procedure of the disease {name} is:<br><br>{chemical_control}'
    return process_response(name, response)


def get_preventive_measures(name: str) -> str:
    disease = get_disease_document(name)
    response = None
    if disease is not None:
        preventive_measures = disease.get('preventive_measures')

        response = f'Here are some preventive measures for the disease {name}:<br><br><ul>'

        for measure in preventive_measures:
            response += f'<li>{measure}</li>'

        response += '</ul>'
    return process_response(name, response)


def process_response(disease_name, response):
    if response is not None:
        return response
    else:
        fallback_responses = [
            "I'm afraid I couldn't find information about that disease.",
            "Hmm, I'm not sure what you're asking about.",
            "I don't have your asked details on that disease.",
            "I'm not able to find your requested information on that specific disease.",
            "Unfortunately, I don't have the information on that particular disease.",
            "I'm sorry, but I couldn't find the information you're looking for.",
            "I'm afraid I don't have the requested information of that disease.",
            "I'm sorry, I wasn't able to find the details on that disease.",
            "I'm not able to find the information about that disease.",
            "I couldn't find the information on that disease.",
            "I'm sorry, but I don't have the information about that disease.",
            "I'm afraid I couldn't find the details on that specific disease.",
            "Unfortunately, I don't have the information on that disease.",
            "I'm sorry, I don't have the information on that disease at this time.",
            "I'm not able to find the details about that disease.",
            "I'm afraid I don't have the information on that specific disease.",
            "I'm sorry, I couldn't find the information about that disease.",
            "I'm not able to find the information on that particular disease.",
            "I'm sorry, but I don't have the details on that disease.",
            "I'm afraid I couldn't find the information on that disease."
        ]

        random_number = random.randint(0, len(fallback_responses) - 1)

        return fallback_responses[random_number]

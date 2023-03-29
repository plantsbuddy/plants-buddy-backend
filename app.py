from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/plant',methods = ['POST'])
def get_plant_details():
    data = request.get_json()
    return jsonify(
        plant=data['plant_name'],
        scientific_name='Trofolium stellatum',
        id='48486454',
    )


# @app.route('/students')
# def other():
#     # A welcome message to test our server
#     return jsonify(
#         username='Mohsin Ismail',
#         scientific_name='Trofolium stellatum',
#         id='48486454',
#     )


# if __name__ == '__main__':
#     # Threaded option to enable multiple instances for multiple user access support
#     app.run(port=process.env.PORT)

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(
        username='Mohsin Ismail',
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

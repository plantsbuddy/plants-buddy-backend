from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our Mibalo!</h1>"


@app.route('/students')
def index():
    # A welcome message to test our server
    return "<h1>Here are some students!</h1>"


# if __name__ == '__main__':
#     # Threaded option to enable multiple instances for multiple user access support
#     app.run(port=process.env.PORT)

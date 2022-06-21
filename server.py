from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"


@server.route("/visualizePrediction", methods=["GET","POST"])
def visualizePrediction():
    if request.method == "GET":
        return "found visualizePrediction"
    elif request.method == "POST":
        requestJson = request.get_json()
        return jsonify(requestJson["prediction"])


if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)

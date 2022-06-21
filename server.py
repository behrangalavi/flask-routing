from flask import Flask, request, jsonify
server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    server.run(host='0.0.0.0', port=1337)

@server.route("/visualizePrediction", methods=["GET","POST"])
def visualizePrediction():
    if request.method == "GET":
        return "found visualizePrediction %s" % (request.method)
    else:
        requestJson = request.get_json()
        return jsonify(requestJson["prediction"])


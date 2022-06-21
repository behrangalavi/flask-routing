from flask import Flask
from flask import request
from flask import render_template
from flask.json import jsonify

server = Flask(__name__)


@server.route("/")
def hello():
    encoded_plots = [
        generate_view("monday", get_mock_data_server('testoutput2.json')),
        generate_view("tuesday", get_mock_data_server('testoutput2.json')),
        generate_view("wednesday", get_mock_data_server('testoutput2.json')),
        generate_view("thursday", get_mock_data_server('testoutput2.json')),
        generate_view("friday", get_mock_data_server('testoutput2.json')),
        generate_view("saturday", get_mock_data_server('testoutput2.json')),
        generate_view("combined", get_mock_data_server('testoutput2.json'))
    ]

    dropdown_values = [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Donnerstag",
        "Freitag",
        "Samstag",
        "Wochenansicht"
    ]

    return render_template("marktseite.html", list=encoded_plots, labels=dropdown_values)



@server.route("/visualizePrediction", methods=["GET", "POST"])
def visualizePrediction():
    if request.method == "GET":
        return "found visualizePrediction %s" % (request.method)
    else:
        requestJson = request.get_json()
        return jsonify(requestJson["prediction"])

@server.route("/visualizePredictionForWholeWeek", methods=["GET", "POST"])
def visualizePredictionForWholeWeek():
    if request.method == "GET":
        return "found visualizePrediction %s" % (request.method)
    else:
        generate_view("combined", request.get_json)
        requestJson = request.get_json()
        return jsonify(requestJson["prediction"])



if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)


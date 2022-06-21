from flask import Flask
from flask import request

server = Flask(__name__)

@server.route("/")
def hello():
    return "Hello World!"


@server.route("/visualizePrediction", methods=["GET","POST"])
def visualizePrediction():
    return "found visualizePrediction %s" % (request.method)
    


if __name__ == "__main__":
   server.run(host='0.0.0.0', port=1337)

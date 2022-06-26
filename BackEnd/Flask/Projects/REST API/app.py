from flask import Flask, jsonify
from requests import request

app = Flask(__name__)


@app.route('/<string:n>')
def home(n):
    if True:
        Restaurent = {
            "itemName" : n,
            "restaurentName" : "Rinsho",
        }

        return jsonify(Restaurent)
    else:
        pass


if __name__ == "__main__":
    app.run(debug=True)